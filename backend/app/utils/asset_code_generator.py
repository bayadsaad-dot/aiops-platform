from app.models.asset import Asset

PREFIXES = {
    "PC": "PC",
    "Server": "SRV",
    "Switch": "SW",
    "Router": "RTR",
    "Firewall": "FW",
    "Printer": "PRN",
}


def generate_asset_code(last_asset: Asset | None, asset_type: str) -> str:
    prefix = PREFIXES.get(asset_type, "AST")

    if not last_asset:
        return f"{prefix}-0001"

    try:
        last_number = int(last_asset.asset_code.split("-")[1])
    except (IndexError, ValueError):
        last_number = 0

    return f"{prefix}-{last_number + 1:04d}"