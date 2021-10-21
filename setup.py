from setuptools import setup

setup(name='auto_renewal',
      version='0.1',
      description='Helps in auto renewal of books issued from Library.',
      url="https://github.com/mananbordia/Library-Book-Renew.gitpt",
      author='mananbordia',
      author_email='mananbordia@gmail.com',
      license='MIT',
      packages=['auto_renewal'],
      install_requires=[
          'selenium','webdriver-manager'
      ],
      include_package_data=True,
      zip_safe=False)