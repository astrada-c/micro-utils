from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='vanna-micro-utils',
    url='https://github.com/svera-co/micro-utils.git',
    author='',
    author_email='',
    # Needed to actually package something
    packages=['vanna_micro_utils'],
    # Needed for dependencies
    install_requires=['boto3'],
    # *strongly* suggested for sharing
    version='0.3',
    # The license can be anything you like
    license='MIT',
    description='modules used across services',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
