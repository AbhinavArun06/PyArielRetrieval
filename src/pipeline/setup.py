from setuptools import setup, find_packages

setup(
    name="ariel_pipeline",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'numpy>=1.20',
        'pandas>=1.3',
        'scikit-learn',
        'PyWavelets',
        'batman-package',
        'pymultinest'
    ],
)