import numpy as np
from typing import Dict

class Calibrator:
    def __init__(self, dark_frame: np.ndarray, flat_frame: np.ndarray):
        self.dark = dark_frame
        self.flat = flat_frame / np.median(flat_frame)  # Normalize

    def apply_calibration(self, raw_images: np.ndarray) -> np.ndarray:
        """Apply dark subtraction and flat fielding"""
        calibrated = (raw_images - self.dark) / self.flat
        return np.clip(calibrated, 0, None)  # Remove negative values

    @classmethod
    def from_calibration_files(cls, calib_data: Dict[str, np.ndarray]):
        """Initialize from calibration data dictionary"""
        return cls(
            dark_frame=calib_data['dark'],
            flat_frame=calib_data['flat']
        )