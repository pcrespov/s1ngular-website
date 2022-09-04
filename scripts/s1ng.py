from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def main(basedir: Path):
    w, h = mpl.figure.figaspect(0.5)
    k = 5
    plt.figure(figsize=(k * w, k * h))

    x1 = np.linspace(-10, -1e-6, 800)
    x2 = np.linspace(1e-6, 10, 800)

    for x in [x1, x2]:
        for m in np.linspace(10, 60, 4):
            y = 300 / x**3 + m * x
            plt.plot(x, y, "r-", linewidth=20)
            # plt.hold(True)

    plt.axvline(linewidth=3, color="r")
    axes = plt.gca()

    axes.set_ylim([-600, 600])

    plt.axis("off")
    plt.savefig(basedir / "s1ngularity.svg")


if __name__ == "__main__":
    main(Path("./ignore.keep"))
