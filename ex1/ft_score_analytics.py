import sys


def ft_score_analytics() -> None:
    try:
        print("=== Player Score Analytics ===")
        argc: int = len(sys.argv)
        if argc == 1:
            raise ValueError("No scores provided. Usage: python3 "
                             "ft_score_analytics.py <score1> <score2> ...")
        scores: list[int] = []
        i: int = 1
        line: str = "Scores processed: ["
        first: bool = True
        while i < argc:
            if first is False:
                line += ", "
            first = False
            line += sys.argv[i]
            scores += [int(sys.argv[i])]
            i += 1
        line += "]"
        print(line)
        print(f"Total players: {argc - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / (argc - 1)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    ft_score_analytics()
