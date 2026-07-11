import os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

# Create folders
os.makedirs("models", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Create environment
env = gym.make("CartPole-v1")
env = Monitor(env, "logs")

# Create PPO model
model = PPO(
    policy="MlpPolicy",
    env=env,
    verbose=1,
    learning_rate=0.0003,
    n_steps=2048,
    batch_size=64,
    gamma=0.99,
    gae_lambda=0.95
)

print("Training started...")

# Train model
model.learn(total_timesteps=60000)

# Save model
model.save("models/ppo_cartpole")

print("Training completed successfully!")
print("Model saved in models/ppo_cartpole.zip")

env.close()