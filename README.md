# chararray

A standard mutable character array implementation for Python.

```pycon
>>> from chararray import chararray
>>> chars = chararray("abc")
>>> chars
chararray('abc')
>>> chars + 'def'
chararray('abcdef')
>>> chars
chararray('abc')
>>> chars += 'def'
>>> chars
chararray('abcdef')
>>> chars[:3]
chararray('abc')
>>> chars[3:]
chararray('def')
>>> chars[3:] = 'ghi'
>>> chars
chararray('abcghi')
>>> chars[0] = 'A'
>>> chars
chararray('Abcghi')
```

## Installing

Get it via pip:

```console
pip install chararray
```

## Testing

Run `pytest`

## Type Checking

Run `mypy .`
