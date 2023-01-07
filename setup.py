from setuptools import setup, find_packages

setup(
    name="chatty-form",
    install_requires=[
        "openai"
    ],
    entry_points={
        "console_scripts": [
            "chatform = src.main:main"
        ]
    },
    packages=find_packages(),
    python_requires="<3.12,>=3.10",
)
