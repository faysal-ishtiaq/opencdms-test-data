from setuptools import setup, find_packages


setup(
    name='opencdms_test_data',
    version='0.1.0',
    description='OpenCDMS test data as package.',
    author='OpenCDMS',
    author_email='info@opencdms.org',
    url='https://github.com/opencdms/opencdms-test-data',
    packages=find_packages(include=["opencdms_test_data", "opencdms_test_data.*"]),
    include_package_data=True,
    zip_safe=False,
    package_data={'': ["*.csv"]}
)
