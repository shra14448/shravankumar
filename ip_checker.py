import ipaddress
ip=input("Enter your ip:")

try:
    ip_obj=ipaddress.ip_address(ip)
    print("The entered IP address is valid")

    if ip_obj.is_private:
        print("Private IP address")
    elif ip_obj.is_global:
        print("Public IP address")
    elif ip_obj.is_loopback:
        print("Loopback IP address")
    elif ip_obj.is_multicast:
        print("Multicast IP address")
    else:
        print("Unknown IP address type")
except ValueError:
    print("Invalid IP address, Please check the ip")             