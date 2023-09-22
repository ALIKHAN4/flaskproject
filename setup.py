from setuptools import setup ,find_packages


def get_requirements(file_path):
    requirements = []

    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements



setup(

name = "flask_project",
version = '0.0.1',
author='Ali Khan',
author_email='alikhan680880@gmail.com',
packages=find_packages(),
install_requirements = get_requirements('requirements.txt')

)