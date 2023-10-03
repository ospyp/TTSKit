from setuptools import setup, find_packages

setup(
    name='pyttskit',
    version='0.1.0',
    packages=find_packages(),
    author='mrfakename',
    author_email='me@mrfake.name',
    description='Text-to-speech kit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ospyp/TTSKit',
    license='Multiple (See File). Main: NOSCL-C-2.0. Includes MIT, etc',
)