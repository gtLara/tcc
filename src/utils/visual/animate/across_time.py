import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.axes._subplots import Axes
from matplotlib import animation


def iterate_signal_animation(iterator: int, line: Line2D, axis: Axes,
                             win_size: int, step: int,
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
    signal_min, signal_max = min(signal), max(signal)
    axis.set_ylim(signal_min - signal_min/20,
                  signal_max + signal_max/20)
    line.set_data(np.arange(win_size), signal[window])

    return line,


def animate_signal_across_time(signal: np.ndarray, win_size: int, step: int,
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

    ax = plt.axes(xlim=(0, win_size))
    line, = ax.plot([], [])

    n_frames = ((len(signal) - win_size)//step)

    signal_animation = animation.FuncAnimation(fig, iterate_signal_animation,
                                               frames=n_frames,
                                               interval=interval,
                                               blit=True,
                                               fargs=(line, ax, win_size, step,
                                                      signal))

    return signal_animation


signal = np.random.normal(size=5000)
win_size = 100
step = 50
interval = 10

anim = animate_signal_across_time(signal, win_size, step, interval)
