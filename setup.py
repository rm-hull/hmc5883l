#!/usr/bin/env python

import setuptools

setuptools.setup(name='hmc5883l',
      version='0.0.1',
      description='Interface functions for HMC8553L Magnetometer (I2C digital compass)',
      author='Richard Hull',
      author_email='unknown@example.com',
      url='https://github.com/rm-hull/hmc5883l',
      packages=setuptools.find_packages(),
      install_requires=["smbus"],
      include_package_data=True,
      entry_points='''
      [console_scripts]
      hmc5883l = hmc5883l:main
      '''
  )
