#!/bin/bash
set -e

for py_version in 3.6 3.7 3.8 3.9 3.10
do
echo "Creating python=$py_version environment for test..."
~/miniconda3/bin/conda create -n test_env python=$py_version -y > /dev/null
~/miniconda3/bin/conda install -n test_env pytest -y > /dev/null
~/miniconda3/bin/conda run -n test_env --no-capture-output pytest test --cache-clear
~/miniconda3/bin/conda env remove --name test_env -y > /dev/null
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
rm -rf test/test_module_output
rm -rf .pytest_cache
rm /dev/null
done
