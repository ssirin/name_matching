from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
   name='name_matching',
   version='0.8.4',
   description='A package for the matching of company names',
   author='Michiel Nijhuis',
   author_email='m.nijhuis@dnb.nl',
   url="https://github.com/DeNederlandscheBank/name_matching",
   packages=['name_matching','distances'],
   install_requires = [
			'cleanco',
			'scikit-learn', 
                        'pandas',
                        'numpy',
			'tqdm'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
