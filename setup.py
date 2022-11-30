import os
import io
from setuptools import setup, find_packages

CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name='sat-biblio-referencement',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/clemsciences/sat-biblio-referencement',
    license='',
    author='clemsciences',
    author_email='clem@clementbesnier.fr',
    description='SAT BIBLIO Référencement',
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=True,
    install_requires=["lxml", "SQLAlchemy", "requests"],
    python_requires=">=3.6",
    keywords=['library', 'french'],
    script=[]
)
