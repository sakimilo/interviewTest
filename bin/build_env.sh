#!/bin/bash

#### Create a fresh environment with python 3.7
conda create -n assessment_LingYit python=3.7

#### Activate the environment
conda activate assessment_LingYit

#### Install jupyter lab
conda install jupyterlab -c conda-forge -y

#### Install packages
conda install -c conda-forge matplotlib -y
conda install -c conda-forge scikit-learn -y
conda install -c conda-forge pandas -y
conda install -c conda-forge numpy -y

conda install -c conda-forge pyodbc -y
conda install -c conda-forge seaborn -y