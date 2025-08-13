from setuptools import setup, find_packages

setup(
    name='self_reflecting_agent_multi',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyyaml',
        'groq',
    ],
    entry_points={
        'console_scripts': [
            'self-reflecting-agent = main:main',
        ],
    },
)
