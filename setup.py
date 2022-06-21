from setuptools import setup


setup(
    name='slirm',
    version='0.1dev',
    packages=['slirm',],
    license='BSD',
    long_description=open('README.md').read(),
    entry_points = {
        'console_scripts': ['slirm=slirm.cli:main'],
    }
)
