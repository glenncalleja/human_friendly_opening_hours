Development info
========================================================================

To run coverage report:

```zsh
pytest --cov-report term-missing --cov=human_friendly_opening_hours .
```


To publish to Pypi:

```zsh
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload  dist/*
```