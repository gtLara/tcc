import matplotlib.pyplot as plt
plt.style.use("ggplot")


def plot_unit_circle(ax, lim):

    ax.set_aspect("equal")

    unit_circle = plt.Circle((0, 0), 1, color="black", fill=False,
                             linestyle="--")

    ax.add_patch(unit_circle)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
