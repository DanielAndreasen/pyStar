from setuptools import setup, find_packages
from Cython.Distutils import build_ext


setup(
	maintainer='Daniel T. Andreasen',
    name='pyStar',
	version=0.1,
	license='MIT',
    packages=find_packages(),
    url='https://github.com/DanielAndreasey/pyStar',
    cmdclass={'build_ext': build_ext}
)
