from setuptools import setup

with open("README.rst", encoding="utf-8") as file:
    readme = file.read()

setup(
    name='totz',
    version='1.2.1',
    author='Ken Kundert',
    author_email='totz@nurdletech.com',
    description='Convert timezone of a time.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    license='GPLv3+',
    scripts=['totz'],
    install_requires=[
        'docopt',
        'inform>=1.4',
    ],
    python_requires='>=3.6',
)
