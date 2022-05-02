from setuptools import setup

setup(
    name="fah",
    version="1.0.9-dev0",
    description="Package providing fasta helpers",
    url="https://github.com/crowja/fah",
    author="John A. Crow",
    author_email="crowja@gmail.com",
    license="",
    scripts=["bin/fah"],
    packages=["fah"],
    install_requires=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
    ],
)
