#!/bin/bash

rm -f logs/*.log
find . -name __pycache__ | xargs rm -rf

rm -rf ../notebooks/.ipynb_checkpoints
rm -rf ../.ipynb_checkpoints
rm -rf .pytest_cache