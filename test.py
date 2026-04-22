import ipaddress
ip=input("Enter an IP address: ")
if ipaddress.ip_address(ip):
    print("test")
