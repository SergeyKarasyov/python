import os
from setuptools import setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup_dir = os.path.dirname(os.path.realpath(__file__))
install_reqs = parse_requirements(os.path.join(setup_dir, 'requirements.txt'),
                                  session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="dateAndGeo",
    version="0.0.1",
    author="SKarasov",
    author_email="SKarasov@companyname.com",
    description=("Package for reading date and geodata values."),
    keywords="data geo",
    packages=['pylib'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 0 - PrePrePreAlpha",
        "Topic :: Utilities",
    ],
    install_requires=reqs,
    requires=reqs
)
