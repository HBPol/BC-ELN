#!/bin/bash
# run this inside the vagrant machine once started

# create venv virtual environment in folder ~/venv
python3 -m venv ~/venv

# activate the virtual environment
source ~/venv/bin/activate

# install django
pip install django
pip install --upgrade pip