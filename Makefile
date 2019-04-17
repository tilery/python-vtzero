init:
	git submodule update --init

compile: 
	python setup.py build_ext --inplace

test:
	pip install .
	py.test -v


release: init compile test
	rm -rf dist/ build/ *.egg-info
	python setup.py sdist upload