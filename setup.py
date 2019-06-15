from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='optdesignpy',
    version='0.0.1',
    description='Tools for optical design',
    long_description=readme,
    author='SJSY126',
    author_email='soya.saijo@gmail.com',
    install_requests=['numpy', 'matplotlib'],
    url='https://github.com/SJSY126/optdesignpy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
