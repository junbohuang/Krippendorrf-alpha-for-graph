from setuptools import setup

setup(
    name='krippendorrf-graph',
    version='0.0.1',
    description='A Python package for computing krippendorrfs alpha for graph (modified from https://github.com/grrrr/krippendorff-alpha/blob/master/krippendorff_alpha.py)',
    url='https://github.com/grrrr/krippendorff-alpha/blob/master/krippendorff_alpha.py',
    author='Junbo Huang',
    author_email='junbo.huang@uni-hamburg.de',
    license='Apache 2 License',
    install_requires=['networkx',
                      'numpy',
                      "tqdm"
                      ],

    py_modules=["./"]
)