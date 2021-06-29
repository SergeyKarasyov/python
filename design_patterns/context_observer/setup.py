"""[summary]
"""
import os

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

import setuptools

SETUP_DIR = os.path.dirname(os.path.realpath(__file__))
INSTALL_REGS = parse_requirements(os.path.join(SETUP_DIR, 'requirements.txt'), session=False)
REGS = [str(ir.req) for ir in INSTALL_REGS]

setuptools.setup(install_requires=REGS)
