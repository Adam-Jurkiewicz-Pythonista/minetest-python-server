"""
Test connnection to the server
"""
import mcpi.minecraft as minecraft  # import modułu minecraft

server_ip = "192.168.1.192"
server_port = 4711

try:
    mc = minecraft.Minecraft.create(server_ip, server_port)  # podaj adres IP
    message = f"SUPER! Serwer Minetest pod {server_ip=} działa poprawnie !"
    mc.postToChat(message)  # wysłanie komunikatu do mc
    print(message)
except Exception as e:
    print(f"Error dla {server_ip} ->", e)
