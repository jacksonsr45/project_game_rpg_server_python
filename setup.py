from setuptools import setup

setup(
   name='server_game',
   version='0.1.0',
   description='A server for a game',
   author='jacksonsr45',
   author_email='jacksonsr45@gmail.com',
   packages=[
       '.server',
       '.teste',
       ],  #same as name
   install_requires=[
       
   ], #external packages as dependencies
)