from netmiko import ConnectHandler
import json

switches = [
   {"device_type": "cisco_ios", "ip": f"10.10.10.{i}", "username": "admin", "password": "admin123"} for i in range(1, 5)
]

inventario = {}

for sw in switches:
    net_connect = ConnectHandler(**sw)

    hostname = net_connect.send_command("show run | include hostname").split()[1]
    cdp = net_connect.send_command("show cdp neighbors detail")
    interfaces = net_connect.send_command("show ip intefaces brief")
    config = net_connect.send_command("show run")

    inventario[hostname] = {
         "ip": sw["ip"],
         "cdp_neighbors": cdp,
         "interfaces": interfaces,
         "running_config": config

}

net_connect.disconnect()

with open("inventario_red.json", "w") as f:
     json.dump(inventario, f, indent=4)

print("inventario guardado en inventario_red.json")
