def show_achievement(name: str, achievement: set[str]) -> None:
    print(f"Player {name} achievements: {achievement}")


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    alice: set[str] = {'first_kill', 'level_10',
                       'treasure_hunter', 'speed_demon'}
    show_achievement("alice", alice)
    bob: set[str] = {'first_kill', 'level_10',
                     'boss_slayer', 'collector'}
    show_achievement("bob", bob)
    charlie: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer',
                         'speed_demon', 'perfectionist', 'perfectionist'}
    show_achievement("charlie", charlie)
    print()
    print("=== Achievement Analytics ===")
    all_achievement: set[str] = {'boss_slayer', 'collector', 'first_kill',
                                 'level_10', 'perfectionist', 'speed_demon',
                                 'treasure_hunter'}
    print(f"Total unique achievements: {len(all_achievement)}")
    print()
    print(f"Common to all players: {set.intersection(alice, bob, charlie)}")
    rare_alice: set[str] = set.difference(set.difference(alice, bob), charlie)
    rare_bob: set[str] = set.difference(set.difference(bob, charlie), alice)
    rare_charlie: set[str] = set.difference(set.difference(charlie, alice),
                                            bob)
    print(f"Rare achievements (1 player): "
          f"{set.union(rare_alice, rare_bob, rare_charlie)}")
    print()
    print(f"Alice vs Bob common: {set.intersection(alice, bob)}")
    print(f"Alice unique: {set.difference(alice, bob)}")
    print(f"Bob unique: {set.difference(bob, alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
