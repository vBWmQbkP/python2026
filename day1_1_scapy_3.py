import os
import time
from threading import Thread

from scapy.all import ICMP, IP, Raw, send, sniff

from dotenv import load_dotenv
import os

load_dotenv()

target_ip = "223.5.5.5"
my_ip = os.getenv("MYDEVICE_IP")
interface = os.getenv("INTERFACE")

print(f"Sending ping from {my_ip} to {target_ip} via {interface}...")

# 2. 构造数据包
# 默认 ICMP() 的 id=0，部分公网主机（如 223.5.5.5）对 id=0 的 Echo 不回包；与系统 ping 类似使用非零 id。
icmp_id = os.getpid() & 0xFFFF or 1
pkt = (
    IP(src=my_ip, dst=target_ip)
    / ICMP(type=8, id=icmp_id, seq=1)
    / Raw(b"\x00" * 56)
)

# 3. 先嗅探、后发送（或并发）：若先 send 再 sniff，公网 RTT 往往只有几毫秒，
#    回包可能在 sniff 绑定网卡之前就已到达，导致永远抓不到。
print("Waiting for reply...")
captured = []

def _sniff_reply():
    captured.extend(
        sniff(
            iface=interface,
            filter=f"icmp and src host {target_ip}",
            count=1,
            timeout=3,
        )
    )


t = Thread(target=_sniff_reply)
t.start()
time.sleep(0.05)  # 等 libpcap 在本网卡上开始抓包
send(pkt, verbose=0)
t.join()

reply = captured

if reply:
    print("✅ 收到回复！")
    # reply 是一个列表，取第一个元素
    reply[0].show()
else:
    print("❌ 依然没有收到回复。")
    print("💡 用 tcpdump 看是否有回包；若 ping 命令正常而本脚本无回复，核对 ICMP 的 id/seq、源地址与过滤器。")