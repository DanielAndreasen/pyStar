[![Build Status](https://travis-ci.org/DanielAndreasen/pyStar.svg?branch=master)](https://travis-ci.org/DanielAndreasen/pyStar)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/914ea06f3b4f489badba77583e7d46b6)](https://www.codacy.com/app/daniel.andreasen/pyStar?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DanielAndreasen/pyStar&amp;utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/914ea06f3b4f489badba77583e7d46b6)](https://www.codacy.com/app/daniel.andreasen/pyStar?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DanielAndreasen/pyStar&amp;utm_campaign=Badge_Grade)

[![GitHub license](https://img.shields.io/github/stars/DanielAndreasen/pyStar.svg?style=flat-square)](https://github.com/DanielAndreasen/pyStar/stargazers)
[![GitHub license](https://img.shields.io/github/forks/DanielAndreasen/pyStar.svg?style=flat-square)](https://github.com/DanielAndreasen/pyStar/network)
[![GitHub license](https://img.shields.io/github/issues/DanielAndreasen/pyStar.svg?style=flat-square)](https://github.com/DanielAndreasen/pyStar/issues)
[![GitHub license](https://img.shields.io/github/license/DanielAndreasen/pyStar.svg?style=flat-square)](https://github.com/DanielAndreasen/pyStar/blob/master/LICENSE)


# pyStar

I want a module that does star-stuff. I give it data (colours, asteroseismic,
spectrocopic, etc.) and it give me results like Teff, logg, age, mass, etc.

This is an open project. If any are interested in helping feel free to contact me,
open an issue, or create a pull request.

## Installation
Things you need is `python3.6` and the modules listed in the `requirements.txt`.
It is recommended to install by running this command: `pip install git+https://github.com/DanielAndreasen/pyStar` and then
`import star` for all its glory. This will also take care of any requirements
not installed on your system.


## Usage
`pyStar.py` is the main module. See the example in the end of the file.

The other files are classes to deal with the responsibility for other stuff.
These also have examples at the end of the file.

### Spectroscopy
A function to showcase this class has been added. Simply run:

```python
from star import spectroscopy
spectroscopy.example()
```
