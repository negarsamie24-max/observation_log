 
import matplotlib.pyplot as plt

def show_graph(observations):
    if len(observations) == 0:
        print("No observations to display")
        return

    names = []
    values = []

    for obs in observations:
        names.append(obs.target)
        values.append(obs.exposure)

    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    axs[0].bar(names, values)
    axs[0].set_title("Bar Chart")
    axs[0].set_xlabel("Target")
    axs[0].set_ylabel("Exposure (seconds)")

    axs[1].scatter(names, values)
    axs[1].set_title("Scatter Plot")
    axs[1].set_xlabel("Target")
    axs[1].set_ylabel("Exposure (seconds)")

    axs[2].plot(names, values, marker="o")
    axs[2].set_title("Line Plot")
    axs[2].set_xlabel("Target")
    axs[2].set_ylabel("Exposure (seconds)")

    fig.suptitle("Target vs Exposure Time")
    plt.tight_layout()
    plt.show()

    