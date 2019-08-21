from setuptools import setup

install_requires = [
    'pandas>=0.25.0',
    'numpy>=1.15.4',
    'glob2>=0.6',
    'functools'
]

tests_require = ['pytest>=4.0.2']

setup(name='src',
      version='0.0.1',
      description='test of travis and pytest',
      author='Misha Berrien',
      author_email='misha.berrien@gmail.com',
      tests_require=tests_require,
      install_requires=install_requires,
      packages=['d00_utils'])
