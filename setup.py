import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mindspore-json",
    version="0.1.0",
    author="Your Name",
    description="MindSpore JSON utilities and machine learning models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dq77/mindspore-json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: MindSpore",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.7',
    install_requires=[
        'mindspore>=1.0.0',
        'numpy>=1.17.0',
        'easydict>=1.9',
        'matplotlib>=3.3.0'
    ],
    setup_requires=['wheel'],
)
