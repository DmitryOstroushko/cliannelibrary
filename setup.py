from setuptools import setup, find_packages

setup(name='cliannelibrary',
      version='0.1',
      url='https://github.com/DmitryOstroushko/cliannelibrary',
      license='Dmitry Ostroushko',
      author='Dmitry Ostroushko',
      author_email='dmitrlylianne@gmail.com',
      description='Create useful utilities',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)