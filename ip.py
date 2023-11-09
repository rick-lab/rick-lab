#-*- codeing = utf-8 -*-
#@Time : 2023/4/18 16:34
#@Author : Rick
#@File : ip.py
#@Software:PyCharm
import socket

# 读取主机名列表文件
with open("hostnames.txt", "r") as f:
    hostnames = f.read().splitlines()

try:
    # 获取所有主机名的IP地址
    ip_addresses = [socket.gethostbyname(hostname) for hostname in hostnames]

    # 将IP地址写入文件
    with open("ip_addresses.txt", "w") as f:
        for ip_address in ip_addresses:
            f.write(f"{ip_address}\n")

    print("IP addresses saved to file.")
except socket.gaierror:
    print("Hostname could not be resolved.")
