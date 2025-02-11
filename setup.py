from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_jonasbrito92",
    version="0.0.1",
    author="Jonas",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonasbrito92/package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)