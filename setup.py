"""python-vtzero setup."""

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

with open("README.md") as f:
    long_description = f.read()

ext_options = {
    'include_dirs': ['./vendor/vtzero/include', './vendor/protozero/include'],
    'extra_compile_args': ['-O2', '-std=c++11']
}
ext_modules = cythonize([
    Extension('vtzero.tile', ['vtzero/tile.pyx'], language="c++", **ext_options)
])

extra_reqs = {
    "test": ["pytest"],
}


setup(
    name='vtzero',
    description='Python wrapper for vtzero C++ library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    ext_modules=ext_modules,
    provides=['vtzero'],
    include_package_data=True,
    extras_require=extra_reqs,
)
