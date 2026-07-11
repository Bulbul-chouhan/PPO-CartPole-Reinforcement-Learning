import gymnasium as gym
from stable_baselines3 import PPO

# Create environment with rendering enabled
env = gym.make("CartPole-v1", render_mode="human")

# Load trained model
model = PPO.load("models/ppo_cartpole")

obs, _ = env.reset()

done = False

while not done:

    action, _ = model.predict(obs, deterministic=True)

    obs, reward, terminated, truncated, _ = env.step(action)

    done = terminated or truncated

env.close()