import setuptools

setuptools.setup(
    name="epic-games-parser-perses",
    version="0.0.1",
    author="Tiago",
    author_email="tiago.ventura12@gmail.com",
    description="A parser to fetch free games from epic games",
    url="https://github.com/tjventura/epic-games-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)