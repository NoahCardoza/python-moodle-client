from setuptools import setup


setup(
    name='moodle',
    version='0.1',
    packages=['moodle'],
    install_requires=['requests'],
    license='MIT',
    long_description=open('README.md').read(),
    url='https://github.com/NoahCardoza/python-moodle-client',
    author='Noah Cardoza'
)
