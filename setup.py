#!/usr/bin/env python
#
# ======================================================================
#
#                           Brad T. Aagaard
#                        U.S. Geological Survey
#
# ======================================================================
#

# Setup script for the eqdatautils package

from distutils.core import setup

setup(name='obspyutils',
      version='1.0.0',
      description='Utilities for working with seismic waveform data via ObsPy.',
      author='Brad Aagaard',
      packages=['obspyutils',
                'obspyutils/utils',
                ],
      scripts=['applications/specfemToObspy.py',
               ]
      )


# End of file
