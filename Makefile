first: cpp

cpp:
	(cd cpp && make)

pylint:
	prospector python/

pytest: pylint
	pytest

cpptest: cpp
	(cd cpp && make test)

test: pytest cpptest

.PHONY: cpp test cpptest pytest pylint
