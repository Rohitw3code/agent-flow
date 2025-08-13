from setuptools import setup, find_packages

setup(
    name='self_reflecting_agent',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'self-reflecting-agent = main:main',
        ],
    },
)
