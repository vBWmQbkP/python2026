from scapy.all import IP, ICMP, sr1
from dotenv import load_dotenv
import os

load_dotenv()

target_ip = os.getenv("GATEWAY_IP")
# print(target_ip)

print(f"Sending ping to {target_ip}...")

# 发送包
ping_one_reply = sr1(IP(dst=target_ip)/ICMP(), timeout=2, verbose=0)

# 【关键修改】先判断是否有回复
if ping_one_reply is not None:
    print("✅ Received reply:")
    ping_one_reply.show()
else:
    print("❌ No reply received (Timeout or Network Unreachable).")
    print("💡 提示：检查目标 IP 是否存活，或是否存在网络隔离/防火墙问题。")