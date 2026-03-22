hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"

label_width = 5

print("=" * 10, "设备信息", "=" * 10)

#f-string
print(f"{'设备名称:':<{label_width}} {hostname}")
print(f"{'管理地址:':<{label_width}} {ip}")
print(f"{'厂商:':<{label_width+2}} {vendor}")
print(f"{'型号:':<{label_width+2}} {model}")
print(f"{'系统版本:':<{label_width}} {os_version}")

print("=" * 30)