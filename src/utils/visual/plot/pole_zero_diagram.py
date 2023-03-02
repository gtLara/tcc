import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")


def plot_unit_circle(ax: plt.axes._subplots.AxesSubplot,
                     lim: float) -> None:
    """
    Plots unit circle.

    :param ax: Matplotlib axis object on which the unit circle is to be plotted
    :type ax: plt.axes._subplots.AxesSubplot

    :param lim: Extension of plane surrounding unit circle
    :type lim: float

    :rtype: None
    """

    ax.set_aspect("equal")

    unit_circle = plt.Circle((0, 0), 1, color="black", fill=False,
                             linestyle="--")

    ax.add_patch(unit_circle)

    if lim < 1:
        lim = 1

    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)


def plot_roots(roots: np.ndarray,
               ax: plt.axes._subplots.AxesSubplot,
               zeros: bool = True) -> None:
    """
    Plots complex or real polynomial roots.

    :param roots: Array of complex or real roots
    :type roots: np.ndarray

    :param ax: Matplotlib axis object on which the unit circle is to be plotted
    :type ax: plt.axes._subplots.AxesSubplot

    :param zeros: Indicator if roots are zeros of transfer function or not,
                  defaults to True
    :type zeros: bool

    :rtype: None
    """

    for root in roots:
        if zeros:
            ax.scatter(np.real(root), np.imag(root), marker="o", edgecolor="k",
                       facecolor="none", linewidths=1.3)
        else:
            ax.scatter(np.real(root), np.imag(root), marker="x", color="r")


def pole_zero_plot(num: np.ndarray, den: np.ndarray) -> None:
    """
    Plots pole zero plot for a linear filter defined by its transfer function
    numerator and denominator.

    :param num: Array containing transfer function numerator coeficients in
    increasing order
    :type num: np.ndarray

    :param den: Array containing transfer function denominator coeficients in
    increasing order
    :type den: np.ndarray

    :rtype: None
    """

    fig, ax = plt.subplots()

    zeros = np.roots(num)
    poles = np.roots(den)

    max_mag = np.abs(np.concatenate([zeros, poles])).max()
    plot_limit = max_mag + 0.5

    plot_roots(zeros, ax, zeros=True)
    plot_roots(poles, ax, zeros=False)
    plot_unit_circle(ax, plot_limit)
