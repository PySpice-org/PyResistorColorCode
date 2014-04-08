####################################################################################################
# 
# PyResistorColorCode - Python Electronic Tools.
# Copyright (C) 2012 Salvaire Fabrice
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
# 
####################################################################################################

####################################################################################################

import os

####################################################################################################

# Utility function to read the README file.
# Used for the long_description.
def read(file_name):

    source_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.basename(source_path) == 'tools':
        source_path = os.path.dirname(source_path)
    elif 'build/bdist' in source_path:
        source_path = source_path[:source_path.find('build/bdist')]
    absolut_file_name = os.path.join(source_path, file_name)
    doc_path = os.path.join(source_path, 'doc', 'sphinx', 'source')

    # Read and merge includes
    lines = open(absolut_file_name).readlines()
    for line_index, line in enumerate(lines):
        if line.startswith('.. include::'):
            include_file_name = line.split('::')[-1].strip()
            lines[line_index] = open(os.path.join(doc_path, include_file_name)).read()

    return ''.join(lines)
                                
####################################################################################################

setup_dict = dict(
    name='PyResistorColorCode',
    version='0.1.0',
    author='Fabrice Salvaire',
    author_email='fabrice.salvaire@orange.fr',
    description='Python module providing some tools to manage IEC 60062 marking codes for resistors.',
    license = "GPLv3",
    keywords = "resistor color colour code IEC 6006",
    url='http://fabricesalvaire.github.io/PyResistorColorCode',
    scripts=['bin/resistor-decoder'],
    packages=['PyResistorColorCode'],
    data_files = [('share/PyResistorColorCode/icons',['share/icons/resistor.svg']),
                  ('share/applications', ['spec/resistor-decoder.desktop']),
                  ],
    long_description=read('README.txt'),
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
        # pip install => Could not find any downloads that satisfy the requirement PyQt4>=4.9
        # 'PyQt4>=4.9', 
        ],
    )

####################################################################################################
#
# End
#
####################################################################################################
