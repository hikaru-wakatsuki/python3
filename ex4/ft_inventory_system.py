import sys


def create_inventory() -> dict[str, int] | None:
    try:
        argc = len(sys.argv)
        if argc == 1:
            return None
        inventory: dict[str, int] = {}
        i = 1
        while i < argc:
            parts: list[str] = sys.argv[i].split(":")
            if len(parts) != 2:
                raise ValueError("Invalid item format")
            key: str = parts[0]
            value: int = int(parts[1])
            if inventory.get(key) is None:
                inventory[key] = 0
            inventory[key] += value
            i += 1
        return inventory
    except ValueError as e:
        print(e)
        return None


def ft_inventory_system() -> None:
    inventory: dict[str, int] = create_inventory()
    if inventory is None:
        return
    print("=== Inventory System Analysis ===")
    total: int = 0
    for value in inventory.values():
        total += value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory.keys())}")
    print()
    print("=== Current Inventory ===")
    for key, value in inventory.items():
        print(f"{key}: {value} units ({(value / total * 100):.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    most_item: str | None = None
    least_item: str | None = None
    for key, value in inventory.items():
        if most_item is None or value > inventory.get(most_item):
            most_item = key
        if least_item is None or value < inventory.get(least_item):
            least_item = key
    print(f"Most abundant: {most_item} ({inventory.get(most_item)} units)")
    print(f"Least abundant: {least_item} ({inventory.get(least_item)} unit)")
    print()
    print("=== Item Categories ===")
    categories: dict[str, dict[str, int]] = {
        "Moderate": {},
        "Scarce": {}
    }
    for key, value in inventory.items():
        if value >= 5:
            categories["Moderate"].update({key: value})
        else:
            categories["Scarce"].update({key: value})
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")
    print()
    print("=== Management Suggestions ===")
    restock: list[str] = []
    for key, value in inventory.items():
        if value <= 1:
            restock += [key]
    print(f"Restock needed: {restock}")
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
