from setuptools import setup, find_packages   

setup(
    name="clean_folder",   
    version='0.0.1',
    entry_points={
        'console_sceipts':['clean-folder=clran_folder.clean:main']
    },
    packages=find_packages()
)