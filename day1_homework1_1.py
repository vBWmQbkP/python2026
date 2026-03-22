hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"

print("=" * 10, "设备信息", "=" * 10)

#f-string
print(f"{'设备名称:':<5} {hostname}")
print(f"{'管理地址:':<5} {ip}")
print(f"{'厂商:':<7} {vendor}")
print(f"{'型号:':<7} {model}")
print(f"{'系统版本:':<5} {os_version}")

print("=" * 30)