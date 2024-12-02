import matplotlib.pyplot as plt
import numpy as np


class Chart:
    def __init__(self, x, y, title):
        self.xs = []
        self.ys = []
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(title)
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)

        # box = self.ax.get_position()
        # self.ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # self.ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))

    def add_chart(self, name, a, b, h):
        self.setup_values(a, b, h)
        self.ax.plot(self.xs, self.ys, label=name)

    def polygonal_chart(self, a, b):
        self.xs.append(a)
        self.ys.append(b)
        self.ax.plot(self.xs, self.ys, marker="o")

    def add_histogram(self, name, a, b, h):
        self.setup_values(a, b, h)
        self.ax.fill_between(self.xs, self.ys, label=name)

    def plot(self, name):
        self.ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))
        self.fig.tight_layout()
        self.fig.savefig(name + ".png")

    def setup_values(self, a, b, h):
        self.xs.clear()
        self.ys.clear()
        self.xs.extend([a, b])
        self.ys.extend([h, h])
