from setuptools import setup

setup(
    name="panoptes-cli",
    version="0.1.0",
    py_modules=["cli"],
    include_package_data=True,
    install_requires=["click","pandas"],
    entry_points="""
        [console_scripts]
        panoptes=cli:cli
    """,
)