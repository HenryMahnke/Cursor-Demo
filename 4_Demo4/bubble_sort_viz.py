import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

##some bugs/things to improve: 
#highlight runs twice in the same frame - meaning the last one is always the only one that shows up 
#animation is not very smooth 
#would be cooler if the list was 1->n just the order was messed up so that 

def generate_random_list(n):
    #want to do random swaps 2n times 
    start_list = list(range(1, n+1))
    for i in range(2*n): 
        # pick a random index 
        randIndex1 = random.randint(0, n-1)
        randIndex2 = random.randint(0, n-1)
        # swap the elements at the random indices 
        start_list[randIndex1], start_list[randIndex2] = start_list[randIndex2], start_list[randIndex1]
    return start_list


class BubbleSortVisualizer:
    def __init__(self, data):
        self.data = data.copy()
        self.original_data = data.copy()
        self.n = len(data)

        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.ax.set_xlim(-1, self.n)
        self.ax.set_ylim(0, max(self.data) * 1.1)
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        self.ax.set_title("Bubble Sort Visualization")
        self.highlight = True

        # Create bars
        self.bars = self.ax.bar(
            range(self.n), self.data, color="lightblue", edgecolor="black"
        )

        # Add value labels
        self.value_labels = []
        for i, bar in enumerate(self.bars):
            label = self.ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.1,
                str(self.data[i]),
                ha="center",
                va="bottom",
                fontweight="bold",
            )
            self.value_labels.append(label)

        # Algorithm state
        self.i = 0  # Pass number
        self.j = 0  # Current comparison index
        self.sort_complete = False
        self.comparisons = 0
        self.swaps = 0
        self.step = 0  

        # Statistics display
        self.stats_text = self.ax.text(
            0.02,
            0.95,
            "",
            transform=self.ax.transAxes,
            fontsize=12,
            verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.9),
        )

    def update_display(self):
        """Update bar heights, labels, and statistics"""
        for idx, (bar, label) in enumerate(zip(self.bars, self.value_labels)):
            bar.set_height(self.data[idx])
            label.set_text(str(self.data[idx]))
            label.set_position(
                (bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1)
            )

        # Update statistics
        status = f"Pass: {self.i + 1}/{self.n}\nComparisons: {self.comparisons}\nSwaps: {self.swaps}\nStep: {self.step}"
        if self.sort_complete:
            status += "\nSORTING COMPLETE!"
        self.stats_text.set_text(status)

    def highlight_comparison(self, idx1, idx2, color="red"):
        """Highlight bars being compared"""
        # Reset all colors to default
        for bar in self.bars:
            bar.set_color("lightblue")

        # Highlight sorted portion (elements that have reached final position)
        for k in range(self.n - self.i, self.n):
            if k < len(self.bars):
                self.bars[k].set_color("lightgreen")

        # Highlight comparison bars
        if idx1 < len(self.bars):
            self.bars[idx1].set_color(color)
        if idx2 < len(self.bars):
            self.bars[idx2].set_color(color)

    def animate_2(self,frame): 
        if self.highlight and not self.sort_complete:
            self.highlight_comparison(self.j, self.j + 1, "blue")
            self.highlight = False
        else: 
            self.highlight = True
            self.animate(frame)
        return list(self.bars) + self.value_labels + [self.stats_text]


    def animate(self, frame):
        self.step = frame

        if self.sort_complete:
            # Animation finished - highlight all bars green
            for bar in self.bars:
                bar.set_color("lightgreen")
            self.ax.set_title("Bubble Sort Complete!")
            self.update_display()
            return list(self.bars) + self.value_labels + [self.stats_text]

        # Bubble sort algorithm
        if self.j < self.n - self.i - 1:
            # Highlight the elements being compared
            self.highlight_comparison(self.j, self.j + 1, "blue")
            self.comparisons += 1

            # Compare and swap if necessary
            if self.data[self.j] > self.data[self.j + 1]:
                # Perform swap
                self.data[self.j], self.data[self.j + 1] = (
                    self.data[self.j + 1],
                    self.data[self.j],
                )
                self.swaps += 1
            self.j += 1
        else:
            # End of current pass, move to next pass
            self.i += 1
            self.j = 0

            # Check if sorting is complete
            if self.i >= self.n - 1:
                self.sort_complete = True

        self.update_display()
        return list(self.bars) + self.value_labels + [self.stats_text]

    def start_animation(self, interval=500):
        """Start the animation"""
        # Calculate maximum frames needed (worst case for bubble sort)
        max_frames = self.n * self.n + 10  # Add a few extra

        ani = animation.FuncAnimation(
            self.fig,
            self.animate_2,
            frames=max_frames,
            interval=interval,
            repeat=False,
            blit=False,
        )
        plt.show()
        return ani


def visualize_bubble_sort(data, speed=500):
    """Create and start bubble sort visualization"""
    visualizer = BubbleSortVisualizer(data)
    return visualizer.start_animation(interval=speed)


def main():
    n = 10  # Reduced for clearer visualization
    randomList = generate_random_list(n)
    print(f"Original list: {randomList}")
    print("Starting bubble sort visualization...")

    visualize_bubble_sort(randomList, 100)  # 800ms between steps


if __name__ == "__main__":
    main()
