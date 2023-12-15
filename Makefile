init:
	pip install -r requirements-dev.txt

test:
	pytest tests/

docs:
    cd docs && make html

clean:
	cd docs && make clean