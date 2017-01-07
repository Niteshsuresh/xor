from setuptools import setup, find_packages

setup(
    name='xor',
    version='0.1',
    description='XOR',
    long_description=readme,
    author=['Niteshsuresh'],
    author_email='nitesh@pratian.com',
    install_requires=(
    	['pillow'], ['pybrain'], ['scipy']
    )
)