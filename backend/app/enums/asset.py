from enum import Enum


class AssetType(str, Enum):
    PC = "PC"
    SERVER = "Server"
    SWITCH = "Switch"
    ROUTER = "Router"
    FIREWALL = "Firewall"
    PRINTER = "Printer"


class AssetStatus(str, Enum):
    ONLINE = "Online"
    OFFLINE = "Offline"
    MAINTENANCE = "Maintenance"
    UNKNOWN = "Unknown"

