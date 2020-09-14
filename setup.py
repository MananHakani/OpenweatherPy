from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'openweatherpy',
    version = '0.0.5',
    author="Ajay Lingayat",
    author_email="lingayatajay2810@gmail.com",
    description = "This module helps to retrieve weather reports from openweathermap.org.",
    url="https://github.com/Ajay2810-hub/OpenweatherPy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules = ['OpenweatherPy'],
    package_dir = {'': 'src'},
    install_requires=[
       "requests",
    ], 
    extras_require = {
       "dev":[
       "pytest>=3.7",
       ]
    },
    classifiers=[
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.5",
       "Programming Language :: Python :: 3.6",
       "Programming Language :: Python :: 3.7",
       "Programming Language :: Python :: 3.8",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
