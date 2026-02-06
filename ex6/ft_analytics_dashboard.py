def ft_analytics_dashboard() -> None:
    print('=== Game Analytics Dashboard ===')
    # players: list[str] = ["alice", "bob", "charlie", "diana"]
    scores: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }
    is_active: dict[str, bool] = {
        "alice": True,
        "bob": True,
        "charlie": True,
        "diana": False,
    }
    achievements: dict[str, list[str]] = {
        "alice": ["first_kill", "level_10", "boss_slayer",
                  "boss_slayer", "boss_slayer"],
        "bob": ["first_kill", "level_10", "boss_slayer"],
        "charlie": ["first_kill", "level_10", "boss_slayer", "first_kill",
                    "first_kill", "first_kill", "first_kill"],
        "diana": set(),
    }
    regions: dict[str, str] = {
        "alice": "north",
        "bob": "north",
        "charlie": "east",
        "diana": "central",
    }
    print()
    print("=== List Comprehension Examples ===")
    high_scores: list[str] = [player for player, score in scores.items()
                              if score > 2000]
    doubled_scores: list[int] = [score * 2 for score in scores.values()]
    active_players: list[str] = [player for player, active in is_active.items()
                                 if active is True]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")
    print()
    print("=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {
        player: score for player, score in scores.items()
        }
    score_categories: dict[str, int] = {
        "high": len([score for score in scores.values() if score > 2000]),
        "medium": len([score for score in scores.values()
                       if 1500 < score <= 2000]),
        "low": len([score for score in scores.values() if score <= 1500]),
    }
    achievement_count: dict[str, int] = {
        player: len(achievement)
        for player, achievement in achievements.items() if len(achievement) > 0
        }
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_count}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_players: set[str] = {player for player in scores.keys()}
    unique_achievements: set[str] = {
        achievement for achievement_set in achievements.values()
        for achievement in achievement_set
    }
    active_regions: set[str] = {region for region in regions.values()}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(scores)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(scores.values()) / len(scores)}")
    top_player: str = max(scores, key=scores.get)
    print(f"Top performer: {top_player} ({scores[top_player]} points, "
          f"{len(achievements[top_player])} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
