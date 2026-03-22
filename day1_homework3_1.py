# 1. 定义设备数据 (使用列表存储字典，方便扩展)
devices = [
    {"name": "CoreSwitch", "ip": "10.1.1.1", "role": "核心交换机"},
    {"name": "Firewall",   "ip": "10.1.1.2", "role": "防火墙"},
    {"name": "WLC",        "ip": "10.1.1.3", "role": "无线控制器"}
]

# 2. 定义列宽 (根据内容长度手动设定，或者动态计算)
# 观察数据：
# 名称最长 "CoreSwitch" (10字符) -> 设为 16
# IP最长 "10.1.1.1" (8字符)     -> 设为 16
# 角色最长 "无线控制器" (5汉字=10宽) -> 设为 12
col_name_width = 16
col_ip_width   = 16
col_role_width = 12

# 3. 计算分隔线总长度
# 总长 = 列宽1 + 列宽2 + 列宽3 + 间隔空格(假设每列间2个空格)
separator_len = col_name_width + col_ip_width + col_role_width + 4 
title_text = " IP地址规划表 "
title_width = sum(2 if ord(c) > 127 else 1 for c in title_text) # 动态计算标题显示宽度

# 4. 打印顶部标题
side_padding = (separator_len - title_width) // 2
print("=" * side_padding + title_text + "=" * side_padding)

# 5. 打印表头
# {:<16} 表示左对齐，占用16个字符宽度
print(f"{'设备名称':<{col_name_width}} {'管理地址':<{col_ip_width}} {'角色':<{col_role_width}}")

# 6. 打印分隔线
print("-" * separator_len)

# 7. 打印每一行数据
for dev in devices:
    print(f"{dev['name']:<{col_name_width}} {dev['ip']:<{col_ip_width}} {dev['role']:<{col_role_width}}")

# 8. 打印底部横线
print("=" * separator_len)