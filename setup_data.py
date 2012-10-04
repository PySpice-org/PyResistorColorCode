####################################################################################################
# 
# PyElectronic - Python Electronic Tools
# Copyright (C) Salvaire Fabrice 2012 
# 
####################################################################################################

####################################################################################################

import os

####################################################################################################


# Utility function to read the README file.
# Used for the long_description.
def read(file_name):

    path = os.path.dirname(__file__)
    if os.path.basename(path) == 'tools':
        path = os.path.dirname(path)
    absolut_file_name = os.path.join(path, file_name)

    return open(absolut_file_name).read()

####################################################################################################

setup_dict = dict(
    name='PyElectronic',
    version='1.0',
    author='Fabrice Salvaire',
    author_email='fabrice.salvaire@orange.fr',
    description='Python Tools for Electronic',
    license = "GPLv3",
    keywords = "electronic tools",
    url='http://fabrice-salvaire.pagesperso-orange.fr/software/index.html',
    scripts=['bin/colour-resistor-decoder'],
    packages=['PyElectronic'],
    long_description=read('README'),
    # cf. http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Education",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        ],
    install_requires=[
        'pyqt>=4.8',
        ],
    )

####################################################################################################
#
# End
#
####################################################################################################
