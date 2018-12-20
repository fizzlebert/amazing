import setuptools

from amazing.__version__ import __author__, __author_email__, __description__
from amazing.__version__ import __license__, __title__, __version__

setuptools.setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    python_requires=">= 3.0.0, <=3.6.7",
    description=__description__,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danieloconell/amazing",
    packages=["amazing"],
    install_requires=["pydaedalus", "pillow"],
    license=__license__,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
