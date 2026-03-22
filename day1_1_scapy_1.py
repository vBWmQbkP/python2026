# 1. 导入模块
# 从 scapy.all 导入所有必要的功能。
# 这包括：IP (构建IP层), ICMP (构建ICMP层), sr1 (发送并接收单个包) 等。
# "*" 表示导入该模块下的所有公开类和函数。
from scapy.all import *

from dotenv import load_dotenv
import os

load_dotenv()

target_ip = os.getenv("GATEWAY_IP")

# 2. 构建并发送数据包
# sr1 函数含义: "Send and Receive 1" (发送并接收一个包)
# 它的工作流程是：
#   a. 构造数据包：IP(dst="...")/ICMP()
#      - IP(dst="172.18.6.2"): 设置目标 IP 地址为 172.18.6.2
#      - / : 操作符，用于将上层协议 (ICMP) 堆叠在下层协议 (IP) 之上
#      - ICMP(): 创建一个默认的 ICMP 请求包 (即 Ping 请求)
#   b. 发送数据包到网络接口。
#   c. 等待回复。
#
# 参数说明:
#   timeout=1: 设置超时时间为 1 秒。如果 1 秒内没收到回复，就停止等待。
#   verbose=0: 关闭详细输出模式 (0 表示安静，不打印发送/接收的调试信息)。
#
# 返回值:
#   - 如果收到回复：返回一个包含回复数据的 Packet 对象。
#   - 如果超时或未收到回复：返回 None (空值)。
ping_one_reply = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)

# 3. 处理结果 (关键步骤：防止报错)
# 在调用 .show() 之前，必须先检查 ping_one_reply 是否为 None。
# 如果网络不通，sr1 返回 None，直接调用 .show() 会导致 AttributeError 崩溃。
if ping_one_reply:
    # 如果有回复，打印详细的数据包结构信息
    # .show() 方法会以人类可读的格式分层展示数据包的各个字段 (如 IP头、ICMP头、载荷等)
    print("✅ 收到回复，数据包详情如下：")
    ping_one_reply.show()
else:
    # 如果没有回复 (超时或目标不可达)
    print("❌ 未收到回复 (请求超时或目标主机不可达)。")
    print("💡 提示：请检查目标 IP 是否正确、防火墙是否拦截，或尝试使用 sudo 运行脚本。")