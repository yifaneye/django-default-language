from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='django-default-language',
    version='0.0.1',
    description='Set a default language for Django project with ease!',
    py_modules=['language'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=long_description,
    long_description_context_type='text/markdown',
    url='https://github.com/yifaneye/django-default-language',
    author='Yifan Ai',
    author_email='yifanai@aol.com'
)
