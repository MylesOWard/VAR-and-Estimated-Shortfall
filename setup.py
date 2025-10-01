from setuptools import setup, find_packages

setup(
    name="monte-carlo-var",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy", "pandas", "matplotlib", "scipy", "yfinance"
    ],
)
