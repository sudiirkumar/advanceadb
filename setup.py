import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="advance_adb",
    version="0.0.1",
    author="Sudhir Kumar",
    author_email="sudhir9122kumar@gmail.com",
    description="Advance adb toolkit in one place",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
