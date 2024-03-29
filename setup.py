#! /usr/bin/env python
#

DESCRIPTION = "psfcube: Python library to fit PSF profile + Background on Integral Field Unit cubes "
LONG_DESCRIPTION = """  Python library to fit PSF profile + Background on Integral Field Unit cubes """

DISTNAME = 'psfcube'
AUTHOR = 'Mickael Rigault'
MAINTAINER = 'Mickael Rigault' 
MAINTAINER_EMAIL = 'm.rigault@ipnl.in2p3.fr'
URL = 'https://github.com/MickaelRigault/psfcube'
LICENSE = 'Apache 2.0'
DOWNLOAD_URL = 'https://github.com/MickaelRigault/psfcube/0.10'
VERSION = '0.10.0'

try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

if __name__ == "__main__":

    if _has_setuptools:
        packages = find_packages()
        print(packages)
    else:
        # This should be updated if new submodules are added
        packages = ['psfcube']

    setup(name=DISTNAME,
          author=AUTHOR,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires= [
                "astropy>=4.0.5",
                "iminuit>=2.0.0",
                "matplotlib",
                "modefit>=0.4.0",
                "numpy>=1.21.6",
                "pyifu",
                "scipy>=1.7.3",
                "shapely>=1.8.0"
          ],
          packages=packages,
          package_data={},
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.5',              
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Astronomy',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
      )
