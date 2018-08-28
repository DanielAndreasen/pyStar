from setuptools import setup, find_packages
from Cython.Distutils import build_ext
import star


setup(
	maintainer=star.__author__,
    name=star.__name__,
	version=star.__version__,
	long_description=open('README.md').read(),
	license='MIT',
    packages=find_packages(),
    url='https://github.com/DanielAndreasey/pyStar',
    cmdclass={'build_ext': build_ext},
	package_data={'star': ['data/spec_ml_sample.hdf']},
	install_requires=[
		'astropy>=3.0.3',
		'numpy>=1.15.0',
		'matplotlib>=2.0.2',
		'pandas>=0.23.0',
		'dataclasses>=0.6',
		'scikit-learn>=0.19.2',
		'scipy>=1.1.0',
		'tables>=3.4.4',
		'specML>=0.4'
	],
	dependency_links=[
		'https://github.com/MariaTsantaki/spectroscopy-ML/tarball/master#egg=specML-0.4'
	]
)
