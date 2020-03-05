from setuptools import setup

setup(
    name='rexinsta',
    version='0.0.0',
    description='Discord bot made to follow people that is potentially follower to your \
        profile and unfollows who doesn\'t follows you',
    
    packages=[
        'rexinsta'
    ],

    install_requires=[
        'requests~=2.22'
    ],
)