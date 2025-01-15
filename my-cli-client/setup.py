from setuptools import setup, find_packages

setup(
    name="my-cli-client",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click==8.0.3",
        "setuptools",
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "mycli=main:cli",
        ],
    },
)