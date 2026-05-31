import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path: str) -> pd.DataFrame:
    """Load example survival and body weight data."""
    data = pd.read_csv(file_path)
    return data


def calculate_survival_rate(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate survival rate based on total larvae and dead larvae."""
    data["survival_rate"] = (
        data["total_larvae"] - data["dead_larvae"]
    ) / data["total_larvae"] * 100
    return data


def plot_survival_curve(data: pd.DataFrame) -> None:
    """Plot survival curves for different groups."""
    for group in data["group"].unique():
        group_data = data[data["group"] == group]
        plt.plot(
            group_data["day"],
            group_data["survival_rate"],
            marker="o",
            label=group,
        )

    plt.xlabel("Day")
    plt.ylabel("Survival rate (%)")
    plt.title("Survival Curve")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_body_weight(data: pd.DataFrame) -> None:
    """Plot average body weight changes for different groups."""
    for group in data["group"].unique():
        group_data = data[data["group"] == group]
        plt.plot(
            group_data["day"],
            group_data["average_body_weight_g"],
            marker="o",
            label=group,
        )

    plt.xlabel("Day")
    plt.ylabel("Average body weight (g)")
    plt.title("Body Weight Change")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = load_data("example_data.csv")
    df = calculate_survival_rate(df)

    print(df)

    plot_survival_curve(df)
    plot_body_weight(df)
