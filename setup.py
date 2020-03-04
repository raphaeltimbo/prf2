import io
import os
import re

from setuptools import setup


def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def version(path):
    """Obtain the packge version from a python file e.g. pkg/__init__.py
    See <https://packaging.python.org/en/latest/single_source_version.html>.
    """
    version_file = read(path)
    version_match = re.search(
        r"""^__version__ = ['"]([^'"]*)['"]""", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = version("ccp/__init__.py")


setup(
    name="ccp",
    version=VERSION,
    description="Cálculo de performance para compressores centrífugos.",
    author="Raphael Timbó",
    author_email="raphaelts@petrobras.com.br",
    packages=["ccp", "ccp.config", "ccp.data_io"],
    package_data={"ccp.config": ["new_units.txt"]},
    install_requires=[
        "numpy",
        "scipy",
        "CoolProp",
        "matplotlib",
        "bokeh",
        "pint",
        "toml",
        "openpyxl",
        "tqdm",
    ],
)
