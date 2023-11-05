from setuptools import setup,find_packages

setup( 
    name="Work Automation",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    description="Convert files into different formats",
    long_description=open("README.md").read(),
    url="https://github.com/AneleMaphalala/work-automation.git",
    author="Anele Maphalala",
    author_email="maphalalaanele@gmail.com"
    )
   