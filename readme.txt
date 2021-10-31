
USEFUL LINKS:

1. How to do python libraries:
    1) https://code.tutsplus.com/tutorials/how-to-write-your-own-python-packages--cms-26076
    2) https://code.tutsplus.com/ru/tutorials/how-to-write-package-and-distribute-a-library-in-python--cms-28693
    3) https://www.youtube.com/watch?v=ji5nkIiGHrU

2. To create dist
python3 setup.py sdist

3. To upload python packages
twine upload sdist/*

4. To update package on PyPI
It is needed to change version in setup.py
To remove dist directories
To repeat steps 2 and 3