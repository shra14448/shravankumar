import os

def check_reachability(ip):
    response=os.system(f"ping -n 3 {ip}")
    if response==0:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")

ip_list=["192.168.10.1","8.8.8.8","1.1.1.1"]

for ip in ip_list:
    check_reachability(ip)