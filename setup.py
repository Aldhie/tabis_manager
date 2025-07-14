from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="tabis_manager",
    version="0.0.1",
    description="Custom application for Trabis.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Aldhie",
    author_email="email@anda.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
