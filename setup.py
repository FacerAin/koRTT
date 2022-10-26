from setuptools import setup, find_packages
from distutils.core import setup, Extension

setup(
    name="koRTT",
    version="0.0.1",
    url="https://github.com/FacerAin/koRTT",
    author="FacerAin",
    author_email="ywsong.dev@kakao.com",
    description="Round Trip Translation tool for Korean data augmentation",
    packages=find_packages(exclude=["test"]),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=[""],
    python_requires=">=3",
    license="MIT",
)
