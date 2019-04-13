init:
	git submodule update --init

compile: 
	python setup.py build_ext --inplace

test:
	py.test -v
