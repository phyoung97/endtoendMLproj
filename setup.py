from typing import List
from setuptools import setup, find_packages

def get_requirements(file_path: str) -> List[str]:
    '''
    Reads the requirements from a file and returns them as a list.
    Removes '-e .' if present.
    '''
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()

    requirements = [req.strip() for req in requirements]

    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
