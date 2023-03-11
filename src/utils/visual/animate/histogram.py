import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.axes._subplots import Axes
from matplotlib import animation


def iterate_signal_animation(iterator: int, bars: Line2D, axis: Axes,
                             win_size: int, bins: int, step: int,
                             signal: np.array) -> Line2D:
    """
    Animator function which plots the appropriate signal segmente based on the
    iterator argument and window parameters. The window starts at the first
    position and slides across the signal in increments of 'step' samples.
    Each frame of the animation corresponds to a signal window.

    :param iterator: Iterator variable automatically incremented by the
    animation function
    :type iterator: int
    :param line: Matplotlib line object on which to plot updated signal window
    :type line: Line2D
    :param axis: Matplotlib axis object on which to plot updated line
    :type axis: Axes
    :param win_size: Size of signal window. Controls length of the signal
    segment displayed
    :type win_size: int
    :param step: Step of sliding window. Controls speed of signal movement.
    :type step: int
    :param signal: Signal to display
    :type signal: np.ndarray
    """

    start = iterator*step
    end = start + win_size
    window = range(start, end)

    sigma = np.var(signal[window])
    axis.set_xlim(-4*sigma, 4*sigma)

    counts, _ = np.histogram(signal[window], 100)

    axis.set_ylim(0, counts.max())

    for count, rectangle in zip(counts, bars.patches):
        rectangle.set_height(count)

    return bars

# TODO: debug this! and rewrite docstrings after


def animate_histogram_across_time(signal: np.ndarray, win_size: int, bins: int,
                                  step: int,
                                  interval: int = 20) -> animation.FuncAnimation:
    """
    Generates animation of signal viewed through window of fixed length
    across time. Size and speed of window movemente are controlled by
    'win_size' and 'step' parameters respectively.

    :param signal: Signal to display
    :type signal: np.ndarray
    :param win_size: Size of signal window. Controls length of the signal
    segment displayed
    :type win_size: int
    :param step: Step of sliding window. Controls speed of signal movement.
    :type step: int
    :param interval: Time interval between animation frames in milliseconds,
    defaults to 20
    :type interval: int
    """

    fig = plt.figure()
    ax = plt.axes()
    ax.set_ylim(0, 1.5)
    _, _, bars = ax.hist([], bins, lw=1,
                         ec="gray", fc="gray", alpha=0.7)

    n_frames = ((len(signal) - win_size)//step)

    signal_animation = animation.FuncAnimation(fig, iterate_signal_animation,
                                               frames=n_frames,
                                               interval=interval,
                                               blit=True,
                                               fargs=(bars, ax, win_size, bins,
                                                      step, signal))

    return signal_animation


signal = np.random.normal(size=10000)
animate_histogram_across_time(signal, win_size=100, bins=30, step=20,
                              interval=20)
plt.show()
