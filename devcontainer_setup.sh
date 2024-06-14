#!/usr/bin/env bash
set -e 

python3 -m pip install --upgrade pip 
python3 -m pip poetry 
poetry config --local virtualenvs.create false
poetry install