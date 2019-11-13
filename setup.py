from setuptools import find_packages, setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Postman',
    url='https://github.com/x0y-gt/postman',
    author='Sebastian Godoy',
    author_email='x0y@milkyweb.co',
    # Needed to actually package something
    #packages=find_packages(exclude=('tests',)),
    packages=['postman'],
    # Needed for dependencies
    install_requires=['jinja2', 'yagmail'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A library to send emails using different providers',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
