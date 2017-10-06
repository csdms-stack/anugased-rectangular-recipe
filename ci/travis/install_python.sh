#! /bin/bash

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    os="MacOSX-x86_64";
else
    os="Linux-x86_64";
fi

dest=$HOME/miniconda.sh
if [[ "$TRAVIS_PYTHON_VERSION" == 2.* ]]; then
    curl $MINICONDA_URL_BASE/Miniconda2-latest-$os.sh > $dest;
else
    curl $MINICONDA_URL_BASE/Miniconda3-latest-$os.sh > $dest;
fi

bash $dest -b -p $CONDA_PREFIX
export PATH="$CONDA_PREFIX/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda install python=$TRAVIS_PYTHON_VERSION
conda install -q conda-build anaconda-client coverage sphinx
