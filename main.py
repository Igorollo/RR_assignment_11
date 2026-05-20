import numpy as np
import pandas as pd


def main() -> None:
    data = pd.read_csv("data/scores.csv")
    scores = data["score"].to_numpy()

    print(f"numpy {np.__version__}")
    print(f"pandas {pd.__version__}")
    print()
    print("Score summary")
    print(data.groupby("group")["score"].agg(["count", "mean", "min", "max"]).round(2))
    print()
    print(f"Overall mean: {np.mean(scores):.2f}")
    print(f"Overall standard deviation: {np.std(scores, ddof=1):.2f}")


if __name__ == "__main__":
    main()
