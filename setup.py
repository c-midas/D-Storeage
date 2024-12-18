from setuptools import setup, find_packages

setup(
    name="arweave-python",
    version="0.1.0",
    description="A Python library for interacting with the Arweave network",
    author="Mikee",
    author_email="midashand99@gmail.com",
    url="https://github.com/c-midas/D-Storeage",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
