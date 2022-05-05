import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name='pyconstantt',
    version='1.0.1',
    license='MIT',
    description="New way to make constant in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Yoonhero06",
    author_email='yoonhero06@naver.com',
    packages=find_packages('src', exclude=("tests",)),
    package_dir={'': 'src'},
    url='https://github.com/yoonhero/pyconstant',
    keywords='constant final variable',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],

)
