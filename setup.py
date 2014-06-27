from setuptools import setup, find_packages


setup(
    name='auto-enaml',
    version='0.1.0',
    author='Steven Silvester',
    author_email='steven.silvester@ieee.org',
    url='https://github.com/blink1073/auto-enaml',
    description='Utilities for auto generation of Enaml widgets',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    package_data={'auto_enaml.tests': ['*.enaml'],
                  'auto_enaml.widgets': ['*.enaml']},
    requires=[
    ],
)
