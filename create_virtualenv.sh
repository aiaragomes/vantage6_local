#!/bin/bash -e

# Setting paths
CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_BIN=${HOME}/.pyenv/shims/python3.7
PIP_BIN=$(which pip)
VIRTUALENV_BIN=$(which virtualenv)

# Check dependencies
if [ ! -f ${PYTHON_BIN} ]; then
  echo "Please install python 3.7 with pyenv, exiting ..."
  exit 1
fi

ls ${PIP_BIN}
if [ ! -f ${PIP_BIN} ]; then
  echo "Please install pip, exiting ..."
  exit 1
fi

ls ${VIRTUALENV_BIN}
if [ ! -f ${VIRTUALENV_BIN} ]; then
  echo "Please install virtualenv, exiting ..."
  exit 1
fi

# Remove virtual env if present
if [ -d .venv ]; then
  rm -rf .venv
fi

# Create virtual environment
virtualenv -p ${PYTHON_BIN} .venv
source ./.venv/bin/activate
pip install -r ${CWD}/requirements.txt

echo "To enable python env type: "
echo "source ${CWD}/.venv/bin/activate"
