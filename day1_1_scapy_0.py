from scapy.all import *

from dotenv import load_dotenv
import os

load_dotenv()

target_ip = os.getenv("GATEWAY_IP")

ping_one_reply = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)

print(ping_one_reply.show())