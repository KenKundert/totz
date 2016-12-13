from setuptools import setup

setup(
    name='totz',
    version='1.1.3',
    author='Ken Kundert',
    author_email='totz@nurdletech.com',
    description='Convert timezone of a time.',
    license='GPLv3+',
    scripts=['totz'],
    install_requires=[
        'docopt',
        'inform>=1.4',
    ],
)
