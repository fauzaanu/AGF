from setuptools import setup, find_packages

with open('requirements.txt',encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name='agf',
    version='0.1',
    description='Your package description',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=requirements,
)
