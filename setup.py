from setuptools import setup, find_packages  

setup(  
    name='webconsole',  
    version='0.1',  
    packages=find_packages(),  
    install_requires=[  
        'Flask',  
        'requests'  
    ],  
    entry_points={  
        'console_scripts': [  
            'webconsole=webconsole:webconsole_main',  
        ],  
    },  
)
