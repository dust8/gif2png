import re

from setuptools import setup

with open("README.MD", "rt", encoding="utf8") as f:
    readme = f.read()

with open("gif2png/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

setup(
    name="gif2png",
    version=version,
    author="dust8",
    description="Gif to Png toolkit",
    long_description=readme,
    packages=["gif2png"],
    include_package_data=True,
    install_requires=['pillow', 'click'],
    entry_points={
        'console_scripts': [
            'gif2png=gif2png.cli:gif2png',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
