####################################################################################################
#
# Make a Release
#
####################################################################################################

# Set the environment
. setenv.sh 

# Cleanup the repository
./tools/clean 

# Check licence
./tools/check-license.sh 

# Make Source Tar Archive
python setup.py sdist

# Build
python setup.py bdist
python setup.py bdist_rpm
# python setup.py upload

# Check file list in archive
# Test RPM

####################################################################################################
#
# End
#
####################################################################################################
