from setuptools import setup, find_packages

setup(name='Postman',
      version='0.1',
      description='A library to send emails using different providers',
      long_description=open('README.md').read(),
      keywords='graphql schema api python3',
      url='https://github.com/x0y-gt/postman',
      author='Sebastian Godoy',
      author_email='x0y@milkyweb.co',
      license='GNUv3',
      packages=find_packages(),
      install_requires=[
		'jinja2',
		'yagmail',
      ],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"]
)
