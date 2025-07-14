import pytest
import numpy as np
from src.pipeline.systematics.wavelet import WaveletDetrender

@pytest.fixture
def synthetic_signal():
    t = np.linspace(0, 10, 1000)
    signal = np.sin(t) + 0.5*np.random.randn(1000)
    return signal

def test_wavelet_detrend(synthetic_signal):
    detrender = WaveletDetrender(wavelet='db4', level=5)
    cleaned = detrender(synthetic_signal)
    assert np.std(cleaned) < 0.6  # Noise reduced