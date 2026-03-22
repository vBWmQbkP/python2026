hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"

labels = [
    ("Device Name", hostname),
    ("Management IP Address", ip),
    ("Vendor", vendor),
    ("Model", model),
    ("Software Version", os_version)
]

# 1. 找出最长标签和最长值的长度
max_label_len = max(len(label) for label, _ in labels)
max_val_len = max(len(value) for _, value in labels)

# 2. 定义分隔符样式 (这里用 " : " 共3个字符宽度)
separator = " : "
sep_len = len(separator) # 3

# 3. 计算整行的最大显示宽度
# 公式：最长标签 + 分隔符 + 最长值
max_row_width = max_label_len + sep_len + max_val_len

# 4. 打印顶部标题
# " 设备信息 " 的显示宽度是 10 (2空格 + 4中文*2)
title = " 设备信息 "
title_width = 10 
# 计算两边需要补多少个 '='
side_len = (max_row_width - title_width) // 2

print("=" * side_len + title + "=" * side_len)

# 5. 打印内容
for label, value in labels:
    # 标签左对齐，宽度固定为 max_label_len
    # 然后打印分隔符 " : "
    # 最后打印值
    print(f"{label:<{max_label_len}}{separator}{value}")

# 6. 打印底部横线
# 直接使用计算好的最大行宽
print("=" * max_row_width)