from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename)]


setup(
    name="bacchus",
    version="0.1.0",
    description='Bacchus Project - What is the band',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_requires={'dev': read("requirements-dev.txt")}
)
