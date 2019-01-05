import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mclibre_python_testing_client",
    version="0.0.10",
    author="Bartolome Sintes",
    author_email="bartolome.sintes@gmail.com",
    description="Testing tool for some of the proposed exercises in mclibre.org's Python course available at http://www.mclibre.org/consultar/python/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BartolomeSintes/mclibre-python-testing/",
    # packages=setuptools.find_packages(),
    packages=["mclibre_python_testing_client"],
    # scripts=["mclibre-python-testing-client/mptc.py"],
    entry_points={"console_scripts": ["mptc = mclibre_python_testing_client.mptc:main"]},
    install_requires=["requests", "pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
