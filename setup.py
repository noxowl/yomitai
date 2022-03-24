from setuptools import setup, find_packages
from yomitai import __version__

setup(name='yomitai',
      version=__version__,
      url='https://github.com/noxowl/yomitai',
      license='MIT',
      author='Suyeong RHIE',
      author_email='me@euc-kr.net',
      description='CLI Application for quick reference of Japanese-Yomikata',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      python_requires='>=3.9')
