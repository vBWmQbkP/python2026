version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

version_strip = version_raw.strip()

version_upper = version_strip.upper()

version_replace = version_strip.replace("17.03.04","17.06.01")

print("去掉空格: " + version_strip)
print("转大写:   " + version_upper)
print("替换版本: " + version_replace)