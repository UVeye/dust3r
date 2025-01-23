import setuptools
import os
import uv_build_utils.repo_utils

from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=PipSession())

setuptools.setup(
    name=uv_build_utils.repo_utils.repo_name(),
    version=uv_build_utils.version_utils.version_string(),
    author="",
    author_email="",
    description="",
    packages=setuptools.find_packages(exclude=['*tests*', '*production*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[str(requirement.requirement) for requirement in requirements],
    include_package_data=True
)
