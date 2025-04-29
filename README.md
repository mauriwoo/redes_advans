# 📡 Automatización de Red con Python y Netmiko

## 🎯 Objetivo

Automatizar tareas repetitivas de administración y documentación de red sobre una topología basada en switches multicapa, utilizando Python y la librería Netmiko. Este sistema centralizado corre desde un servidor Debian y permite interactuar por SSH con dispositivos Cisco en una red simulada mediante GNS3

---

## ⚙️ Funcionalidades de los scripts

| Script                | Función principal                                                                 |
|-----------------------|------------------------------------------------------------------------------------|
| `menu_comandos.py`    | Menú interactivo para ejecutar tareas como ver interfaces, vecinos OSPF o CDP, y generar inventario |
| `inventario_red.py`   | Conecta por SSH a los switches y genera un inventario de interfaces, IPs, VLANs y configuraciones clave |


---

## 📌 Tecnologías utilizadas

- 🐍 Python 3
- 🔌 Netmiko
- 🖥️ GNS3 (entorno de red virtual)
- 🐧 Debian 12 (servidor de automatización)

---

## 🧠 Beneficios

- ✅ Ahorro de tiempo en tareas repetitivas
- ✅ Centralización de comandos y monitoreo
- ✅ Compatibilidad con switches Cisco
- ✅ Expansión modular (fácil agregar nuevas tareas)

