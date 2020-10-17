import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="human-friendly-opening-hours",
    version="0.0.5",
    author="Glenn Calleja Frendo",
    author_email="glenncal@gmail.com",
    description="A package used to render opening hours in a human-friendly format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glenncalleja/human_friendly_opening_hours",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
