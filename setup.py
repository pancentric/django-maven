import os

from setuptools import find_packages, setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='django-maven',
    version='0.3',
    license='ISC',
    description='Capture exceptions in django management commands '
                'into Sentry by Raven',
    long_description=read('README.md') + read('CHANGES.md'),
    keywords='django exception management command sentry raven raise error '
             'handling log logging',
    url='https://github.com/saippuakauppias/django-maven',
    author='Denis Veselov',
    author_email='progr.mail@gmail.com',
    include_package_data=False,
    packages=find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP'
    ],
    zip_safe=True,
)
