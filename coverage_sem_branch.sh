#!/bin/bash
python3 -m venv venv
source venv/bin/activate

pip install coverage pytest

coverage run -m pytest
coverage report -m
coverage html -d htmlcov_sem_branch
