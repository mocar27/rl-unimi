import networkx as nx
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from enum import Enum, auto

# Museum Map(Start and Painting position) distribution enumeration.
class SpawnStrategy(Enum):
    FIXED = auto()      # Always bottom-left to top-right
    DIVIDED = auto()    # Random, but Thief on Left, Painting on Right
    RANDOM = auto()     # Completely random everywhere

# Outside function to map given string museum_map into actual graph.
# 'O' indicates a room in the museum, 'W' indicates a wall, example:
# custom_map = [
#     "OOOOO",
#     "OOWOO"
# ]
def map_museum_to_graph(museum_map):
    base_graph = nx.Graph()
    valid_rooms = []
    height = len(museum_map)
    width = len(museum_map[0])

    for y in range(height):
        for x in range(width):
            if museum_map[y][x] == 'O':
                valid_rooms.append((x, y))
                base_graph.add_node((x, y))

                # Connect to left neighbor if it's a room
                if x > 0 and museum_map[y][x - 1] == 'O':
                    base_graph.add_edge((x, y), (x - 1, y))
                # Connect to top neighbor if it's a room
                if y > 0 and museum_map[y - 1][x] == 'O':
                    base_graph.add_edge((x, y), (x, y - 1))

    return base_graph, len(valid_rooms)

# Visualizes the heatmap of probability/importance distribution
# across museum rooms that were chosen by surveillance algorithm.
# Tells us which rooms our Agent learned to be
# the most important, while trying to prevent the painting theft.
def plot_museum_heatmap(env, agent, strat):
    probs = agent.get_probabilities()
    heatmap_data = np.full((env.height, env.width), np.nan)

    for idx, prob in enumerate(probs):
        x, y = env.idx_to_node[idx]
        heatmap_data[y, x] = prob

    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(heatmap_data, annot=True, fmt=".3f", cmap="YlOrRd",
                     cbar_kws={'label': 'Node Importance (Selection Probability)'})

    ax.set_facecolor('black')
    plt.title(f"Camera Attention Heatmap (Temp={agent.tau}, Beta={env.beta}, Lr={agent.lr}, Strat={strat.name})")
    plt.show()

# Plots the Agent's winrate over the course of training.
def plot_learning_curve(win_rate_history, strat, e_win_rate):
    plt.figure(figsize=(8, 5))

    episodes_x = np.arange(1, len(win_rate_history) + 1) * 100
    win_percentages = np.array(win_rate_history) * 100

    plt.plot(episodes_x, win_percentages, marker='o', linestyle='-', color='b', label='Training Win Rate')
    plt.axhline(y=e_win_rate, color='red', linestyle='--', linewidth=2,
                label=f'Eval Win Rate ({e_win_rate:.1f}%)')

    plt.title(f"Agent Win Rate over Time, Spawn Strategy = {strat.name}")
    plt.xlabel("Episodes")
    plt.ylabel("Agent Win Rate (%)")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()
