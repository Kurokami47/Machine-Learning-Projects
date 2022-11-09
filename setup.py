from setuptools import setup, find_packages
from typing import List
    
#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR=" Jagannath Padhy"
DESRCIPTION="This is a my first Machine Learning Project"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file return This function is going 
    to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(
name=PROJECT_NAME,
version=VERSION,  # type: ignore
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)