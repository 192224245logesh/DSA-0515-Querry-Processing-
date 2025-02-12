import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 3)
axs[0, 0].plot([1, 2, 3], [1, 4, 9], color='blue')
axs[0, 0].set_title("Plot 1")
axs[0, 1].scatter([1, 2, 3], [1, 4, 9], color='red')
axs[0, 1].set_title("Plot 2")
axs[0, 2].bar([1, 2, 3], [1, 4, 9], color='green')
axs[0, 2].set_title("Plot 3")
axs[1, 0].plot([1, 2, 3], [1, 2, 3], color='purple')
axs[1, 0].set_title("Plot 4")
axs[1, 1].scatter([1, 2, 3], [3, 2, 1], color='orange')
axs[1, 1].set_title("Plot 5")
axs[1, 2].bar([1, 2, 3], [3, 2, 1], color='pink')
axs[1, 2].set_title("Plot 6")
plt.tight_layout()
plt.show()
