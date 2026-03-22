import unicodedata

hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"

# 定义标签和对应的值（去掉手动补空格，靠程序自动对齐）
labels = [
    ("Device Name", hostname),
    ("Management IP", ip),
    ("Vendor", vendor),
    ("Model", model),
    ("Software Version", os_version)
]

# labels = [
#     ("设备名称", hostname),
#     ("管理IP", ip),
#     ("厂商", vendor),
#     ("型号", model),
#     ("系统版本", os_version)
# ]

# 1. 初始化一个变量，假设最小长度为 0
max_label_len = 0

# 2. 遍历列表
for label, _ in labels:
    # 3. 获取当前标签的长度
    current_label_len = len(label)
    # 4. 如果当前长度比记录的最大长度还大，就更新它
    if current_label_len > max_label_len:
        max_label_len = current_label_len
# 此时 max_label_len 就是结果
print(max_label_len)

# 🔢 动态计算最佳列宽：找最长标签
# max_label_len = max(len(label) for label, _ in labels)


max_val_len = 0
for _, value in labels:
    current_value_len = len(value)
    if current_value_len > max_val_len:
        max_val_len = current_value_len
print(max_val_len)
# 📏 计算底部横线总长度：列宽 + 1空格 + 最长值的长度
# max_val_len = max(len(value) for _, value in labels)



total_line_len = max_label_len + 4 + max_val_len

if total_line_len%2 == 1:
    left_line_half = ( total_line_len - 10 ) // 2
    right_line_half = ( total_line_len - 10 ) // 2 + 1
else:
    left_line_half = ( total_line_len - 10 ) // 2
    right_line_half = ( total_line_len - 10 ) // 2

# 🖨️ 打印顶部标题
print("=" *left_line_half, "设备信息", "=" *right_line_half)

# 🖨️ 打印内容（核心改进：使用动态宽度）
for label, value in labels:
    print(f"{label:<{max_label_len}} {":"} {value}")

# 🖨️ 打印底部横线（与实际内容等长）
print("=" * total_line_len)
# print(total_line_len)