from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYTHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """
    Fetch all the packages available inside of requirements.txt file and return as list of strings
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file_name:
        requirement_list  = requirements_file_name.readlines()
    requirement_list = [requirement_package_name.replace("\n","") for requirement_package_name in requirement_list]
    if HYTHEN_E_DOT in requirement_list:
        requirement_list.remove(HYTHEN_E_DOT)
    return requirement_list 


setup(
    name="sensor",
    version="0.0.1",
    author="Rahul Chatterjee",
    author_email="chatterjeerahul187@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)