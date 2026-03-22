device_name1 = "CoreSwitch"
device_name2 = "Firewall"
device_name3 = "WLC"

Management_IP1 = "10.1.1.1"
Management_IP2 = "10.1.1.2"
Management_IP3 = "10.1.1.3"

Role1 = "核心交换机"
Role2 = "防火墙"
Role3 = "无线控制器"

labels = [
    (device_name1,Management_IP1,Role1),
    (device_name2,Management_IP2,Role2),    
    (device_name3,Management_IP3,Role3)
]

print("="*15, "IP地址规划表", "="*16)
print(f"{"设备名称":<{11}}{"管理地址":<{11}}{"角色":<13}")
print("-" * 45)

for name, ip , role in labels:
    print(f"{name:<{15}}{ip:<{15}}{role:<15}")

print("=" * 45)



# max_name_len = 0
# for Name, _ , _ in labels:
#     current_name_len = len(Name)
#     if current_name_len > max_name_len:
#         max_name_len = current_name_len
# print(max_name_len)

# max_ip_len = 0
# for _, ip , _ in labels:
#     current_ip_len = len(ip)
#     if current_ip_len > max_ip_len:
#         max_ip_len = current_ip_len
# print(max_ip_len)

# max_role_len = 0
# for _ , _ , role in labels:
#     current_role_len = len(role)
#     if current_role_len > max_role_len:
#         max_role_len = current_role_len
# max_role_len = max_role_len * 2
# print(max_role_len)

# total_line_len = max_name_len + max_ip_len + max_ip_len

