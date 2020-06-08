import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="1800_CODE_CHALLENGE",
    version="0.0.1",
    author="Nasimunni",
    author_email="nasicseiiit@gmail.com",
    description="1800_CODE_CHALLENGE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nasicseiiit/1800",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)