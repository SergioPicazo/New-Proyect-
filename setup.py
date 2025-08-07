from setuptools import setup, find_packages

setup(
    name="vehicles-analysis",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.48.0",
        "pandas==2.2.3",
        "plotly==6.2.0"
    ],
)
