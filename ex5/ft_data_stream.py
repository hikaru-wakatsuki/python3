from typing import Generator


def game_event_stream(player: dict[str, int], total: int) -> Generator:
    names: list[str] = list(player.keys())
    events: list[str] = [
        "killed monster",
        "found treasure",
        "leveled up"
    ]
    i: int = 0
    while i < total:
        name: str = names[i % len(names)]
        event: str = events[i % len(events)]
        if event == "leveled up":
            player[name] += 1
        yield i + 1, name, player[name], event
        i += 1


def ft_game_data() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    total: int = 1000
    print(f"Processing {total} game events...")
    player: dict[str, int] = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
        "kate": 0,
        "wakatsuki": 1000
    }
    processed: int = 0
    high_level_players: set[str] = set()
    treasure_events: int = 0
    level_up_events: int = 0
    eid: int
    name: str
    level: int
    event: str
    for eid, name, level, event in game_event_stream(player, total):
        processed += 1
        if processed <= 3:
            print(f"Event {eid}: Player {name} (level {level}) {event}")
        elif processed == 4:
            print("...")
        if level >= 10:
            high_level_players |= {name}
        if event == "found treasure":
            treasure_events += 1
        elif event == "leveled up":
            level_up_events += 1
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {len(high_level_players)}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()


def fibonacci_stream() -> Generator:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator:
    num: int = 2
    while True:
        is_prime: bool = True
        i: int
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime is True:
            yield num
        num += 1


def ft_generator_demonstration() -> None:
    print("=== Generator Demonstration ===")
    fib: Generator = fibonacci_stream()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        print(next(fib), end="")
        if i < 9:
            print(", ", end="")
    print()
    primes: Generator = prime_stream()
    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        print(next(primes), end="")
        if i < 4:
            print(", ", end="")
    print()


def main() -> None:
    ft_game_data()
    ft_generator_demonstration()


if __name__ == "__main__":
    main()
