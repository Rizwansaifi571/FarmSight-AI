from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list[str]:
    '''
    This function returns a list of requirements read from a given file.
    It removes any editable package specifier from the list.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="FarmSight-AI",
    version="0.0.1",
    author="Mohd Rizwan",
    author_email='rizwansaifi2614@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
