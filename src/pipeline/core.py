import numpy as np
import cupy as cp
from .calibration import ADCCalibrator
from .lightcurve import LightCurveExtractor
from .systematics import SystematicsRemover
from .transit import TransitFitter
from .retrieval import SpectralRetriever

class ArielPipeline:
    def __init__(self, config):
        self.backend = 'cupy' if config.get('use_cuda', False) else 'numpy'
        self.calibrator = ADCCalibrator(config)
        self.lc_extractor = LightCurveExtractor(config)
        self.sys_remover = SystematicsRemover(config)
        self.transit_fitter = TransitFitter(config)
        self.retriever = SpectralRetriever(config)
        # cSpell:ignore coeffs
        # cSpell:ignore cupy lightcurve
    
    def process_planet(self, planet_id, signal_file, calibration_files):
        # Load and calibrate data
        raw_data = self.lc_extractor.load_data(signal_file)
        calibrated = self.calibrator.apply_adc(raw_data, calibration_files)
        # Light curve extraction and systematics removal
        lc = self.lc_extractor.extract_lightcurve(calibrated)
        cleaned_lc = self.sys_remover.remove_systematics(lc)
        # Transit fitting
        fit_result = self.transit_fitter.fit(cleaned_lc)
        # Spectral retrieval
        spectrum = self.retriever.retrieve(fit_result)
        return spectrum
