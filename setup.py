# -*- coding: utf-8 -*-
import os.path
from setuptools import setup


here = os.path.dirname(os.path.abspath(__file__))


setup(name='gntplib',
      version='0.5',
      description=('A Growl Notification Transport Protocol (GNTP)'
                   ' client library in Python'),
      long_description=open(os.path.join(here, 'README.rst')).read(),
      author='papaeye',
      author_email='papaeye@gmail.com',
      url='http://github.com/papaeye/gntplib',
      packages=['gntplib'],
      tests_require=['coverage', 'mock', 'nose', 'tornado', 'pycrypto'],
      extras_require={'async': ['tornado'], 'ciphers': ['pycrypto']},
      keywords='gntp growl async',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      platforms='any',
      license='BSD License'
      )
