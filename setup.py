
import re
from setuptools import setup
from typing import List

import storessales



#Declaring variables
PROJECT_NAME='stores-sales-predictor'
VERSION='0.0.1'
AUTHOR='Krishna Kumar'
DESCRIPTION='this is the store sales predector project for shoping malls'
PACKAGES=['storessales']
REQUIREMENT_FILE_NAME='requirements.txt'


def get_requirements_list()->List[str]:

    """
    Description: this function is going to return a list of requirements
    mentioned in requirements.txt file and

    return this function is going to return a list which cinntain name 
    of libraries in requirements.txt file"""

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()




setup(
name=PROJECT_NAME,
verssion=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages= PACKAGES,
install_requires=get_requirements_list()
)


#to chek wehther it is working or not 
if __name__=='__main__':
    print(get_requirements_list())
