To reproduce include directory order issue with Homebrew Python on OS X:

mv TESTHEADER.h /usr/local/include
python setup.py build_ext --inplace
