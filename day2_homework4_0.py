intf1 = "Gi0/0"
status1 = "up"
speed1 = "1G"

intf2 = "Gi0/1"
status2 = "down"
speed2 = "1G"

intf3 = "Gi0/2"
status3 = "up"
speed3 = "10G"

template1= "{:10}{:10}{:10}"

template2= "{:8}{:8}{:8}"

print(template2.format("接口","状态","速率"))
print("-" * 30)
print(template1.format(intf1,status1,speed1))
print(template1.format(intf2,status2,speed2))
print(template1.format(intf3,status3,speed3))