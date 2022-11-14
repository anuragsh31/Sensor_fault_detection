from setuptools import find_packages, setup
from typing import List

def get_requirement()->List[str]:
    requirement_list:list[str]=[]  # add all the requirements in this list which we need
    return requirement_list

setup(
    name='sensor',
    version='0.0.1',
    author='Anurag',
    author_email='imanuragshukla31@gmail.com',
    packages= find_packages(),
    install_requires=get_requirement(), #['pymongo==4.2.0'],
)