from distutils.core import setup

setup(
    name="usfm_tools",
    version="0.0.31",
    author="unfoldingWord",
    author_email="info@unfoldingWord.org",
    description="A framework for transforming .usfm files into specified targets",
    license="MIT",
    keywords="unfoldingWord usfm tools",
    url="https://github.com/linearcombination/USFM-Tools",
    packages=["usfm_tools", "usfm_tools/support"],
    package_data={"usfm_tools": ["py.typed"], "usfm_tools/support": ["py.typed"]},
    long_description="This project comprises a framework for transforming .usfm files into specified targets. It is "
    "primarily used for the Open English Bible, and may need adjustment if used for other purposes. ",
    classifiers=[],
    install_requires=[
        "bs4",
        "future",
        "pyparsing",
    ],
    test_suite="tests",
)
