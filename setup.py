from setuptools import setup, find_packages

import sys

if sys.version_info < (3, 7):
    sys.exit("Sorry, Python < 3.7 is not supported")

setup(
    name="i3autoconfig",
    version="0.1.0",
    description="Autoconfig program for i3wm",
    author="Ondřej Červenka",
    author_email="gogo.lejzr@gmail.com",
    keywords="cli, i3wm",
    license="MIT",
    url="https://github.com/ggljzr/i3-autoconfig",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["click", "pytoml"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={"console_scripts": ["i3-autoconfig = i3autoconfig.cli:main"]},
)

