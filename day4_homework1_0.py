import os
import re
result = os.popen("ifconfig ens160").read()

pattern = re.compile(
    r"[\S\s]+inet\s+(?P<ipv4_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"netmask\s+(?P<netmask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"broadcast\s+(?P<broadcast>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\S\s]+"
    r"ether\s+(?P<mac_addr>\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2})"
)

match = pattern.search(result)

if match:
    ipv4_add = match.group("ipv4_add")
    netmask = match.group("netmask")
    broadcast = match.group("broadcast")
    mac_addr = match.group("mac_addr")

    # print(f"IPv4 Address: {ipv4_add}")
    # print(f"Netmask: {netmask}")
    # print(f"Broadcast: {broadcast}")
    # print(f"MAC Address: {mac_addr}")
    print("{:<13} {}".format("IPv4 Address:", ipv4_add))
    print("{:<13} {}".format("Netmask:", netmask))
    print("{:<13} {}".format("Broadcast:", broadcast))
    print("{:<13} {}".format("MAC Address:", mac_addr))
else:
    print("No match found.")

parts = ipv4_add.split(".")
# print(parts)
parts[-1] = str(2)
gw_ipv4_add = ".".join(parts)
# print(gw_ipv4_add)
print(f"假设网关是: {gw_ipv4_add} ")
ping_result = os.popen("ping " + gw_ipv4_add + " -c 4").read()
# print(ping_result)
re_ping_result = re.search(r"4 received, 0% packet loss", ping_result)

if re_ping_result:
    print(f"Ping {gw_ipv4_add} ... reachable！")
else:
    print(f"Ping {gw_ipv4_add} ... unreachable！")