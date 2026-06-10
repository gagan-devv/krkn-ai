import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file (read as UTF-8 to avoid Windows encoding errors)
DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

# Parse requirements.txt into a list of package specifiers.
# NOTE: read_text() returns a raw str; passing that directly to install_requires
# causes setuptools to iterate over individual characters rather than package
# names, silently skipping every dependency.  We must split into lines and
# filter out blank lines and comments.
REQUIRE = [
    line.strip()
    for line in (HERE / "requirements.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.strip().startswith("#")
]

setup(
    name="krkn_ai",
    version="0.0.3",
    description="Krkn-AI",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    platforms="any",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
    packages=find_packages(include=["krkn_ai*"]),
    include_package_data=True,
    install_requires=REQUIRE,
    entry_points={
        "console_scripts": [
            "krkn_ai = krkn_ai.cli:main",
        ]
    },
)
