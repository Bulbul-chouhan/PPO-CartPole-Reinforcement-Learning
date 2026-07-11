import os
import gymnasium as gym
from stable_baselines3 import PPO
import numpy as np

# Create results folder
os.makedirs("results", exist_ok=True)

# Load environment
env = gym.make("CartPole-v1")

# Load trained model
model = PPO.load("models/ppo_cartpole")

episode_rewards = []

episodes = 100

for episode in range(episodes):

    obs, _ = env.reset()
    done = False
    total_reward = 0

    while not done:

        action, _ = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        total_reward += reward

    episode_rewards.append(total_reward)

env.close()

average_reward = np.mean(episode_rewards)
highest_reward = np.max(episode_rewards)
lowest_reward = np.min(episode_rewards)
success_rate = (np.array(episode_rewards) >= 475).mean() * 100

report = f"""
PPO CartPole-v1 Evaluation Report
================================

Total Episodes : {episodes}

Average Reward : {average_reward:.2f}

Highest Reward : {highest_reward}

Lowest Reward : {lowest_reward}

Success Rate (>475 reward): {success_rate:.2f}%
"""

print(report)

with open("results/evaluation_report.txt", "w") as file:
    file.write(report)

print("Evaluation report saved successfully.")