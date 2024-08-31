from setuptools import setup, find_packages

setup(
    name='ecommerce',
    version='0.1',
    description='A simple ecommerce application for product management and order processing',
    author='saikiran',
    author_email='saikiranmandapati@gmail.com',
   
    packages=find_packages(),
    install_requires=[
        'flask==2.2.3',        # Web framework
        'pymongo==4.5.0',      # MongoDB driver
        'sqlalchemy==2.0.18',  # SQL toolkit and ORM
        'pandas==2.0.1',       # Data handling
        'numpy==1.24.3',       # Numerical operations
        'pytest==7.4.0',       # Testing framework
        'pytest-mock==3.12.2', # Mocking for tests
        'flake8==6.0.0',       # Linter
        'black==23.8.0'        # Code formatter
    ],
    
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'ecommerce=ecommerce.main:main',  # Entry point for the application
        ],
    },
    include_package_data=True,
)
