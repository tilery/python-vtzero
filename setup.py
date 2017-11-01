import os
from setuptools import setup, Extension

os.environ["CC"] = 'clang++'


setup(
    name='vtzero',
    version='0.0.1',
    description='Python wrapper for vtzero C++ library.',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    keywords='mvt mapbox vector tile gis',
    platforms=['POSIX'],
    author='Yohan Boniface',
    author_email='yohan.boniface@data.gouv.fr',
    license='MIT',
    packages=['vtzero'],
    ext_modules=[
        Extension(
            'vtzero.tile',
            ['vtzero/tile.cpp'],
            extra_compile_args=['-O2', '-std=c++14'],
            include_dirs=['./vendor/vtzero/include',
                          './vendor/protozero/include'],
        )
    ],
    provides=['vtzero'],
    include_package_data=True
)
