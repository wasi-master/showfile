import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="showfile",
    version="0.1.1",
    author="Wasi Master",
    author_email="arianmollik323@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A tool to view files with their proper syntax highlighting in the console",
    url="https://wasi-master.github.io/showfile/",
    project_urls={
        "Github": "https://github.com/wasi-master/showfile",
        "Bug Tracker": "https://github.com/wasi-master/showfile/issues",
        "Documentation": "https://github.com/wasi-master/showfile/blob/main/README.md",
        "Say Thanks": "https://saythanks.io/to/arianmollik323@gmail.com",
    },
    packages=["showfile"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General"
    ],
    python_requires=">=3.6",
    install_requires=["rich"],
    entry_points={
        "console_scripts": ["showfile=showfile.main:run"],
    },
)
