import os
import re

result = os.popen("route -n").read()
# print(result)

pattern = re.compile(
    r"(?P<destination>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"(?P<gateway>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"(?P<genmask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"(?P<flags>UG)\s+"
    r"(?P<metric>\d+)\s+"
    r"(?P<ref>\d+)\s+"
    r"(?P<use>\d+)\s+"
    r"(?P<iface>\w+)"
)

match = pattern.search(result)

if match:
    gateway = match.group("gateway")
    print(f"Gateway: {gateway}")
else:
    print("No match found.")
