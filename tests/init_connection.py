"""
Test connnection to the server
"""
import mcpi.minecraft as minecraft  # import modułu minecraft
import ini  # config parser

try:
    config = ini.parse(open('../configuration.ini').read())
    server_ip = config['server']['server_ip']
    server_port = config['server']['server_port']
    print("INI file readed.")
except:
    server_ip = "192.168.1.192"
    server_port = 4711

try:
    mc = minecraft.Minecraft.create(server_ip, server_port)  # podaj adres IP
    message = f"SUPER! Serwer Minetest pod {server_ip=} działa poprawnie !"
    mc.postToChat(message)  # wysłanie komunikatu do mc
    print(message)
except Exception as e:
    print(f"Error dla {server_ip} ->", e)
