from setuptools import setup, find_packages
from Cython.Distutils import build_ext


setup(
	maintainer='Daniel T. Andreasen',
    name='pyStar',
	version=0.2,
	license='MIT',
    packages=find_packages(),
    url='https://github.com/DanielAndreasey/pyStar',
    cmdclass={'build_ext': build_ext},
	package_data={'star': ['data/spec_ml_sample.hdf']}
)
