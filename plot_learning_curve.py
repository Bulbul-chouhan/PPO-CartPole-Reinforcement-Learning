import pandas as pd
import matplotlib.pyplot as plt

# Read training log
df = pd.read_csv("logs/monitor.csv", skiprows=1)

# Calculate moving average
df["Moving Average"] = df["r"].rolling(window=20).mean()

plt.figure(figsize=(12,6))

# Raw rewards
plt.plot(
    df["r"],
    color="lightblue",
    linewidth=1,
    alpha=0.5,
    label="Episode Reward"
)

# Moving average
plt.plot(
    df["Moving Average"],
    color="red",
    linewidth=2.5,
    label="20-Episode Moving Average"
)

plt.title("PPO Training Performance on CartPole-v1", fontsize=16)
plt.xlabel("Episode", fontsize=12)
plt.ylabel("Reward", fontsize=12)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("results/learning_curve.png", dpi=300)

plt.show()

print("Learning curve saved successfully!")