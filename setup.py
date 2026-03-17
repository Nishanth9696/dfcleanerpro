from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dfcleanerpro",
    version="0.2.6",
    author="Nishanth_K",
    description="Simple DataFrame cleaning toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url='https://github.com/Nishanth9696/dfcleanerpro',
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
        ],
    install_requires=["pandas","numpy"],
    python_requires=">=3.8",
)