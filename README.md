# 📡 Automatización de Red con Python y Netmiko

## 🎯 Objetivo

Automatizar tareas repetitivas de administración y documentación de red sobre una topología basada en switches multicapa, utilizando Python y la librería Netmiko. Este sistema centralizado corre desde un servidor Debian y permite interactuar por SSH con dispositivos Cisco en una red simulada mediante GNS3.

---

## ⚙️ Funcionalidades de los scripts

| Script                        | Función principal                                                                 |
|------------------------------|------------------------------------------------------------------------------------|
| `conectar_swX.py`            | Conecta a un switch específico (SW1, SW2, etc.) y muestra el estado de interfaces |
| `crear_vlanXX_swX.py`        | Crea VLANs específicas en el switch destino con nombre definido                   |
| `ver_vecinos_ospf.py`        | Consulta y muestra los vecinos OSPF en todos los switches                         |
| `ver_cdp_neighbors.py`       | Extrae información de vecinos mediante CDP                                        |
| `exportar_config_swX.py`     | Obtiene y guarda el running-config del switch en un archivo local                 |
| `ver_vlans.py`               | Muestra las VLANs activas en cada switch                                          |

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

