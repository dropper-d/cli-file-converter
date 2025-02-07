from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name="format-converter",
    version="0.9.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "pyyaml",
        "toml"
    ],
    entry_points={
        "console_scripts": [
        "fconv=scripts.cli:app"
        ]
    },
    author="dropper-d",
    description="Easy CLI tool to convert between JSON, YAML and TOML.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dropper-d/cli-file-converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)