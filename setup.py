import setuptools

setuptools.setup(
    name="epic-games-parser-perses",
    version="0.0.5",
    author="Tiago",
    author_email="tiago.ventura12@gmail.com",
    description="A parser to fetch free games from epic games",
    url="https://github.com/tjventura/epic-games-parser",
    packages=["epic_games_parser"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)


## Help with packages - https://packaging.python.org/tutorials/packaging-projects/

## Project in pipy - pip install -i https://test.pypi.org/simple/ epic-games-parser-tjventura==0.0.1