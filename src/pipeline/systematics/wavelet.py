import pywt
import numpy as np
from typing import Tuple

class WaveletDetrender:
    def __init__(self, wavelet: str = 'db4', level: int = 5):
        """
        Args:
            wavelet: Wavelet type (db4, sym5, etc.)
            level: Decomposition level
        """
        self.wavelet = wavelet
        self.level = level

    def detrend(self, lightcurve: np.ndarray) -> np.ndarray:
        """Remove systematics using wavelet decomposition"""
        coeffs = pywt.wavedec(lightcurve, self.wavelet, level=self.level)
        # Remove high frequency components (indices 1 onward)
        coeffs[1:] = [np.zeros_like(c) for c in coeffs[1:]]
        return pywt.waverec(coeffs, self.wavelet)[:len(lightcurve)]

    def get_wavelet_coeffs(self, signal: np.ndarray) -> Tuple[np.ndarray, ...]:
        """Get full wavelet decomposition for diagnostics"""
        return pywt.wavedec(signal, self.wavelet, level=self.level)