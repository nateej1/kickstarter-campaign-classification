from setuptools import setup, find_packages

setup(name="d00_utils", packages=find_packages(),
      version='0.0.1',
      description='a package example',
      author='Misha Berrien',
      author_email='misha.berrien@gmail.com',
      packages=['d00_utils'],
      install_requires=['pandas',
                        'numpy',
                        'glob',
                        'functools'])
