from setuptools import setup, find_packages

setup(
    name="chatty-form",
    install_requires=[
        "Django==4.1.5",
        "fastapi==0.88.0",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "chatform = src.entrypoints.main:main"
        ]
    },
    packages=find_packages(),
    python_requires="<3.12,>=3.10",
)
