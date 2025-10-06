import numpy as np


def generate_sine_wave(frequency, amplitude, duration, sample_rate=1000):
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, y