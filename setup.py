from setuptools import find_packages, setup
from typing import List
import os

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip() and not line.startswith('#')]

    # Print or log the requirements to debug
    print("Parsed requirements:", requirements)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Harsha Vardhan',
    author_email='hvaitha07@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
