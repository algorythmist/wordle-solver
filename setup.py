import setuptools

setuptools.setup(
    name='wordle-solver',
    version='1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/algorythmist/wordle-solver',
    license='MIT',
    author='Dimitri Papaioannou',
    description='Programs to solve Wordle',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9'
)
