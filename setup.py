import setuptools
import os
import uv_build_utils.version_utils
import uv_build_utils.repo_utils


with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

setuptools.setup(
    name=uv_build_utils.repo_utils.repo_name(),
    version=uv_build_utils.version_utils.version_string(),
    author="",
    author_email="",
    description="",
    package_dir={'': uv_build_utils.repo_utils.repo_root()},
    packages=setuptools.find_packages(uv_build_utils.repo_utils.repo_root()),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required
)
