from setuptools import setup

setup(
    name = "paquete",
    version = "0.1",
    description = "Este es un paquete de ejemplo",
    author = "Alejandro Rivera",
    author_email = "alejandro.rivera0309@gmail.com",
    url = "http://alejandrorivera.com",
    scripts = [],
    packages = ["package", "package.firstsubpackage", "package.secondsubpackage"],
)

# Run this command to create a package and distribute it
# command: python setup.py sdist

# To install the package go to the zip file directory and run this command
# command: pip3 install packagename.zip
# now we can import the package anywhere

# To see all the installed packages
# command: pip3 list

# to uninstall the package
# command: pip3 uninstall packagename