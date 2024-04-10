import setuptools

# Add numpy import
import numpy as np

# Define the extension
elas = setuptools.Extension('elas', sources=[
    'src/pyelas.cpp',
    'src/elas.cpp',
    'src/descriptor.cpp',
    'src/filter.cpp',
    'src/matrix.cpp',
    'src/triangle.cpp',
], define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')])

_long_descr = '''
This package is the port to Python of libelas.

It is a library for computing disparity maps of large images.
It was written by Andreas Geiger as a C++ library and MATLAB toolbox.
I wrote only the Python interface to use it in Python scripts.

You can find the paper where the algorithm is described at
http://dx.doi.org/10.1007/978-3-642-19315-6_3.
'''

setuptools.setup(
    name='pyelas',
    version='1.0.1',
    author='Pier Angelo Vendrame',
    author_email='vogliadifarniente@gmail.com',
    description='These are the Python bindings for libelas by '
                'Andreas Geiger.',
    long_description=_long_descr,
    long_description_content_type='text/plain',
    url='https://github.com/PieroV/PyElas',
    project_urls={
        'Original homepage': 'http://www.cvlibs.net/software/libelas/',
        'Paper': 'http://dx.doi.org/10.1007/978-3-642-19315-6_3',
    },
    classifiers=[
        'Programming Language :: C++',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    license='GPLv3',
    platforms=['Linux', 'Windows', 'Unix', 'macOS'],
    ext_modules=[elas],
    # Add numpy include directory
    include_dirs=[np.get_include()],
    install_requires=[
        'numpy>=1.7',
    ],
    python_requires=">=3.5"
)

