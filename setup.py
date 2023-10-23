from setuptools import setup, find_packages

setup(
    name='agf',
    version='0.1',
    description='Article Generation Framework',
    author='Fauzaan Gasim',
    author_email='hello@fauzaanu.com',
    packages=find_packages(),
    install_requires=[
        'openai==0.27.6',
        'python-dotenv==1.0.0',
    ]
)
