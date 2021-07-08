from setuptools import setup, find_packages


def read(filename: str) -> [str]:
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="Little Notes",
    version="0.0.1",
    description="Quick Note System",
    packages=find_packages(exclude="venv"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)
