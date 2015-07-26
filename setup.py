import setuptools

setuptools.setup(
    name="text2num",
    version="0.1",
    url="https://github.com/ajaali/text2num.git",

    author="Ahmed Ali",
    author_email="ahmed@ajaali.com",

    description="Convert text numerals to integers",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
