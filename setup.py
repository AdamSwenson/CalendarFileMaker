"""
Created by adam on 8/28/18
"""
__author__ = 'adam'

if __name__ == '__main__':
    from distutils.core import setup

setup(
    name='CalendarFileMaker',
    version='0.1.0',
    author='adm',
    author_email='adam.swenson@csun.edu',
    packages=[],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
        'ics'
    ],
)