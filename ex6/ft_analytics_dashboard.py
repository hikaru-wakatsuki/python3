def ft_analytics_dashboard() -> None:
    print('=== Game Analytics Dashboard ===')
    print()
    print("=== List Comprehension Examples ===")
    # players: list[str] = ["alice", "bob", "charlie", "diana"]
    scores: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }
    is_active: dict[str, int] = {
        "alice": True,
        "bob": True,
        "charlie": True,
        "diana": False,
    }
    high_scores: list[str] = [player for player, score in scores.items()
                              if score > 2000]
    doubled_scores: list[int] = [score * 2 for score in scores.values()]
    active_players: list[str] = [player for player, active in is_active.items()
                                 if active is True]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")


if __name__ == "__main__":
    ft_analytics_dashboard()
