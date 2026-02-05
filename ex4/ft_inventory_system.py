import sys


def create_inventory() -> dict[str, int] | None:
    try:
        argc = len(sys.argv)
        inventory: dict[str, int] = {}
        i = 1
        while i < argc:
            parts: list[str] = sys.argv[i].split(":")
            if len(parts) != 2:
                raise ValueError("Invalid item format")
            key: str = parts[0]
            value: int = int(parts[1])
            inventory[key] = value
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
    for qty in inventory.values():
        total += qty
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory.keys())}")
    print()
    print("=== Current Inventory ===")
    for name, qty in inventory.items():
        print(f"{name}: {qty} units ({(qty / total * 100):.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    most_item: str
    least_item: str
    for name, qty in inventory.items():
        if most_item is None or qty > inventory.get(most_item):
            most_item = name
        if least_item is None or qty < inventory.get(least_item):
            least_item = name
    print(f"Most abundant: {most_item} ({inventory.get(most_item)} units)")
    print(f"Least abundant: {least_item} ({inventory.get(least_item)} unit)")
    print()
    print("=== Item Categories ===")

    print()
    print("=== Management Suggestions ===")

    print()
    print("=== Dictionary Properties Demo ===")




if __name__ == "__main__":
    ft_inventory_system()
