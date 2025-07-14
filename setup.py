# setup.py
from setuptools import setup, find_packages

# Ganti dengan informasi aplikasi Anda
__version__ = "0.0.1"
app_name = "tabis_manager"
app_title = "Tabis Manager"
app_publisher = "Trabis"
app_description = "Custom application for Trabis."
app_email = "apps-support@globaltelko.com"
app_license = "MIT"

setup(
    name=app_name,
    version=__version__,
    description=app_title,
    author=app_publisher,
    author_email=app_email,
    license=app_license,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[], # Tambahkan dependensi Python di sini jika ada
)
