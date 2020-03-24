#!/usr/bin/env python

from distutils.core import setup

setup(name='Fortune Engine',
      version='1.0',
      description='The Fortune Game Engine',
      author='Justin Lewis',
      author_email='jlew.blackout@gmail.com',
      url='https://github.com/FOSSRIT/FortuneEngine',
      packages=['fortuneengine','fortuneengine.pyconsole'],
      package_dir = {
        'fortuneengine': 'fortuneengine',
        'fortuneengine.pyconsole': 'fortuneengine/pyconsole'
      },
      package_data={
        'fortuneengine.pyconsole': [
            '*.cfg',
            'fonts/*',
            ]},
      license="GPL 3",
     )
