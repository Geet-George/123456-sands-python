import numpy as np
from functions import generate_sine_wave


def test_generate_sine_wave():
    t, y = generate_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0

    t, y = generate_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = generate_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0

    t, y = generate_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)


def test_we_want_to_see_a_fail():
    t, y = generate_sine_wave(1, 2, 1)
    assert len(t) == 1000
