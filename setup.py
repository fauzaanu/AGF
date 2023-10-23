from setuptools import setup, find_packages

# Specify the full path to the requirements.txt file
requirements_file = 'requirements.txt'

with open(requirements_file, encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name='agf',
    version='0.1',
    description='Article Generation Framework',
    author='Fauzaan Gasim',
    author_email='hello@fauzaanu.com',
    packages=find_packages(),
    install_requires=requirements,
)
