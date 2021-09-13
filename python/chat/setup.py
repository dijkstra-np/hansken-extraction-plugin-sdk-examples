# encoding=utf-8
# file used by distutils to create a distributable package and generate requirements.txt
from setuptools import setup


package_name = "example_chat_plugin"
version_string = "1.0.0"

dependencies = [
    "hansken-extraction-plugin==0.4.3",  # the plugin SDK
]

setup(
    name=package_name,
    version=version_string,
    author='Netherlands Forensic Institute',
    author_email='hansken@holmes.nl',
    description='Example Hansken Extraction Plugin: chat',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['.'],
    include_package_data=True,
    install_requires=dependencies
)
