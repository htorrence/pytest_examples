from setuptools import find_packages, setup

with open('pytest_examples/_version.py') as version_file:
    exec(version_file.read())

with open('README.md') as r:
    readme = r.read()

setup(
    name='pytest_examples',
    version=__version__,
    description='Reference package for unit tests',
    long_description=readme,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        
    ]
)
