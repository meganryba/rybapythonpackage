from setuptools import setup

setup(name='Ryba Python Package',
      version='0.1',
      description='Read a matrix asnd run BLAST searches',
      url='TBD',
      author='Megan Ryba',
      author_email='megan.ryba@selu.edu',
      license='MIT',
      packages=['rybapythonpackage'],
      install_requires=[
          'dendropy',
          'biopython',
          'pandas'
      ],
      long_description=open('README.txt').read(),
zip_safe=True)
