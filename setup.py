from setuptools import setup, find_packages

with open("requirements.txt", 'r') as file:
    requirement = file.read().splitlines()
    
setup(
    name="Car Price Prediction App",
    version="0.0.1",
    author="Md. HR Khan",
    author_email="mdhrkhandata.analyst@gmail.com",
    install_require = requirement,
    packages=find_packages()
)