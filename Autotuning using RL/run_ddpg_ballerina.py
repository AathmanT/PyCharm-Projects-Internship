# %%
import numpy as np
import torch
import matplotlib.pyplot as plt

import ballerina_environment

from ddpg_agent import Agent

from collections import deque

# Create simulation environment
env = ballerina_environment.BalEnv()

# Initialize Feed-forward DNNs for Actor and Critic models.
agent = Agent(state_size=env.observation_space_dimension(), action_size=env.action_space_dimension(), random_seed=0)

# Set the number of episodes to run the simulation
episodes = 3
print_every = 100
iterationss = 20

scores_deque = deque(maxlen=print_every)
scores = []

for episode in range(episodes):
    # Reset the enviroment
    cur_state = env.reset(seed=episode)

    score = 0

    for i in range(iterationss + 1):

        # Predict the best action for the current state.
        action = agent.act(cur_state, add_noise=True)

        # Action is performed and new state, reward, info are received.
        new_state, reward, done, info = env.step(action)
        print("episode: ",episode," sample: ",i," reward: ",reward)
        # current state, action, reward, new state are stored in the experience replay
        agent.step(cur_state, action, reward, new_state, done)

        # roll over new state
        cur_state = new_state

        

        score += reward
        if done:
            break

    scores_deque.append(score)
    scores.append(score)
    print('\rEpisode {}\tAverage Score: {:.2f}'.format(episode, np.mean(scores_deque)), end="")
    torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
    torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')
    if episode % print_every == 0:
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(episode, np.mean(scores_deque)))

#     return scores

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(1, len(scores) + 1), scores)
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.show()






