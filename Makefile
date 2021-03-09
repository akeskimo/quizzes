first: cpp

cpp:
	(cd cpp && make)

pytest:
	pytest

cpptest: cpp
	(cd cpp && make test)

test: pytest cpptest

.PHONY: cpp test cpptest pytest