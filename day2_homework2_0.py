interface = "GigabitEthernet0/0/1"

interface_type = interface[:15]

interface_number = interface[15:]

print("接口类型: " + interface_type)
print("接口编号: " + interface_number)