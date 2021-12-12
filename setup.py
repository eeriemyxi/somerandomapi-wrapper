from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="somerandomapiml",
    version="1.0.3",
    packages=["somerandomapi", "somerandomapi.structures"],
    install_requires=['httpx'],
    author="Myxi",
    author_email="myxi@duck.com",
    url="https://github.com/m-y-x-i/some-random-api-API-Wrapper",
    description="Easy to use API Wrapper for somerandomapi.ml. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    license="GNU GPLv3",
)