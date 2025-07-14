import numpy as np
from pathlib import Path
from typing import Dict

class OpacityDatabase:
    """Molecular cross-section manager"""
    
    def __init__(self, data_dir: str):
        self.data = {}
        for path in Path(data_dir).glob("*.npy"):
            self.data[path.stem] = np.load(path)

    def get(self, species: str, wavelength: float) -> float:
        """Interpolate cross-section at given wavelength"""
        wavelengths, xsects = self.data[species].T
        return np.interp(wavelength, wavelengths, xsects)