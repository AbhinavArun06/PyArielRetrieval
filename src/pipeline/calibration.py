import numpy as np
import pandas as pd

class ADCCalibrator:
    def __init__(self, config):
        self.gain = config['adc']['gain']
        self.offset = config['adc']['offset']
        self.linear_coeffs = config['adc']['linear_coeffs']
    
    def apply_adc(self, data, calibration_files):
        # Apply gain/offset correction
        flux = data * self.gain + self.offset
        # Subtract dark current
        dark = pd.read_parquet(calibration_files['dark'])
        flux -= dark.values
        # Non-linearity correction
        a0, a1, a2, a3 = self.linear_coeffs
        flux_linear = a0 + a1*flux + a2*flux**2 + a3*flux**3
        return flux_linear
