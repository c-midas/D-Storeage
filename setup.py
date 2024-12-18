from setuptools import setup, find_packages

setup(
    name="arweave-python",
    version="0.1.0",
    description="A Python library for interacting with the Arweave network",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/arweave-python",
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
