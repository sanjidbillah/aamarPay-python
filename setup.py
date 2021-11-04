from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

requires = [

    'requests==2.26.0',
]
setup(
    name='aamarpay',
    version='0.0.1',
    description='Payment gateway libarary',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='Masum billah sanjid',
    author_email='masumbillahsanjid@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Payment',
    packages=find_packages(),
    install_requires=requires
)
