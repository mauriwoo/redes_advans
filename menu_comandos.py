from netmiko import ConnectHandler

# Diccionario: nombre del switch → IP
switches = {
    "SW1": "10.10.10.1",
    "SW2": "10.10.10.2",
    "SW3": "10.10.10.3",
    "SW4": "10.10.10.4"
}

# Diccionario: número de opción → comando
comandos = {
    "1": "show run",
    "2": "show ip interface brief",
    "3": "show ip vlan brief",
    "4": "show ip ospf neighbor",
    "5": "show version",
    "6": "show spanning-tree",
    "7": "show cdp neighbors detail",
    "8": "Otro (escribir manualmente)"
}

# Menú de comandos
print("\n🛠 COMANDOS DISPONIBLES:")
for key, cmd in comandos.items():
    print(f"  {key}) {cmd}")

opcion_comando = input("\nElige el número del comando que quieres ejecutar: ")

if opcion_comando not in comandos:
    print("❌ Opción de comando no válida.")
    exit()

# Si elige opción 8, pedir comando personalizado
if opcion_comando == "8":
    comando_seleccionado = input("✍️ Escribe el comando que deseas ejecutar: ")
else:
    comando_seleccionado = comandos[opcion_comando]

# Menú de switches por nombre
print("\n🌐 SWITCHES DISPONIBLES:")
for idx, sw in enumerate(switches.keys(), start=1):
    print(f"  {idx}) {sw}")
print("  5) Todos los switches")

opcion_switch = input("\nElige el número del switch (o 5 para todos): ")

# Si elige la opción 5: ejecutar en todos los switches
if opcion_switch == "5":
    for sw_nombre, ip_destino in switches.items():
        print(f"\n🔐 Conectando a {sw_nombre} ({ip_destino})...")
        dispositivo = {
            "device_type": "cisco_ios",
            "host": ip_destino,
            "username": "admin",
            "password": "admin123",
            "secret": "admin123"
        }

        try:
            conexion = ConnectHandler(**dispositivo)
            conexion.enable()

            salida = conexion.send_command(comando_seleccionado)

            print(f"\n✅ Resultado de '{comando_seleccionado}' en {sw_nombre}:\n")
            print(salida)

            conexion.disconnect()

        except Exception as e:
            print(f"\n❌ Error al conectar o ejecutar el comando en {sw_nombre}: {e}")

# Si elige un solo switch
else:
    try:
        sw_nombre = list(switches.keys())[int(opcion_switch) - 1]
    except (ValueError, IndexError):
        print("❌ Opción de switch no válida.")
        exit()

    ip_destino = switches[sw_nombre]

    dispositivo = {
        "device_type": "cisco_ios",
        "host": ip_destino,
        "username": "admin",
        "password": "admin123",
        "secret": "admin123"
    }

    print(f"\n🔐 Conectando a {sw_nombre} ({ip_destino})...")

    try:
        conexion = ConnectHandler(**dispositivo)
        conexion.enable()

        salida = conexion.send_command(comando_seleccionado)

        print(f"\n✅ Resultado de '{comando_seleccionado}' en {sw_nombre}:\n")
        print(salida)

        conexion.disconnect()

    except Exception as e:
        print(f"\n❌ Error al conectar o ejecutar el comando: {e}")

