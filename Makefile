publish_release:
	rm -rf build
	python2 setup.py bdist_egg bdist_wheel sdist upload
	python3 setup.py bdist_egg bdist_wheel upload
