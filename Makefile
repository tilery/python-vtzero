compile:
	cython -3 --cplus vtzero/tile.pyx
	python setup.py build_ext --inplace

test:
	py.test -v
