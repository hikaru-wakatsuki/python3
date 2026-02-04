import math


def distance_3d(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    x1, y1, z1, = p1
    x2, y2, z2, = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinate(coord_str: str) -> tuple[int, int, int] | None:
    try:
        parts: list[str] = coord_str.split(",")
        x: int = int(parts[0])
        y: int = int(parts[1])
        z: int = int(parts[2])
        return (x, y, z)
    except Exception as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    origin: tuple[int, int, int] = (0, 0, 0)
    position: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {position}")
    print("Distance between %s and %s: %.2f"
          % (origin, position, distance_3d(origin, position)))
    print()
    print('Parsing coordinates: "3,4,0"')
    parsed: tuple[int, int, int] = parse_coordinate("3,4,0")
    print(f"Position created: {parsed}")
    print("Distance between %s and %s: %.1f"
          % (origin, parsed, distance_3d(origin, parsed)))
    print()
    print('Parsing invalid coordinates: "abc,def,ghi"')
    parse_coordinate("abc,def,ghi")
    print()
    print("Unpacking demonstration:")
    x: int
    y: int
    z: int
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
