#!/bin/bash
python3 -m venv venv
source venv/bin/activate

pip install coverage pytest

coverage run --branch -m pytest
coverage report -m
coverage html -d htmlcov_com_branch
