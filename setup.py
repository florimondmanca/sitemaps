import re
from pathlib import Path

from setuptools import find_packages, setup


def get_version(package: str) -> str:
    version = (Path("src") / package / "__version__.py").read_text()
    match = re.search("__version__ = ['\"]([^'\"]+)['\"]", version)
    assert match is not None
    return match.group(1)


def get_long_description() -> str:
    with open("README.md", encoding="utf8") as readme:
        with open("CHANGELOG.md", encoding="utf8") as changelog:
            return readme.read() + "\n\n" + changelog.read()


setup(
    name="sitemaps",
    version=get_version("sitemaps"),
    description="Sitemap generation with support for Python ASGI web apps",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="http://github.com/florimondmanca/sitemaps",
    author="Florimond Manca",
    author_email="florimond.manca@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=["httpx>=0.12,<1.0", "anyio==1.*"],
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
