# Casey

[![PyPI](https://img.shields.io/pypi/v/casey)](https://pypi.org/project/casey/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casey)](https://github.com/marverix/casey/actions/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/gh/marverix/casey?token=NPX0JP4458)](https://app.codecov.io/gh/marverix/casey)
[![GitHub](https://img.shields.io/github/license/marverix/casey)](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0))
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmarverix%2Fcasey.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmarverix%2Fcasey?ref=badge_shield)

A simple library to support various naming conventions and convert strings from one to another.

Casey supports:

* camelCase
* PascalCase
* kebab-case
* snake_case and SNAKE_CASE

## Usage

### Installation

```sh
pip install casey
```

### Sample

```python
import casey

subject = "every 1 WORD is very IMPORTANT"

print(casey.camel(subject))
# Prints: every1WORDIsVeryIMPORTANT

print(casey.kebab(subject))
# Prints: every-1-WORD-is-very-IMPORTANT

print(casey.pascal(subject))
# Prints: Every1WORDIsVeryIMPORTANT

print(casey.snake(subject))
# Prints: every_1_WORD_is_very_IMPORTANT

print(casey.snake(subject, upper=True))
# Prints: EVERY_1_WORD_IS_VERY_IMPORTANT

def my_transformation(word: str, idx: int) -> str:
  if idx % 2 == 0:
    return word.lower()
  else:
    return word.upper()
  
print(casey.transform(subject, my_transformation, "_"))
# Prints: every_1_word_IS_very_IMPORTANT

```

### API

* `clean(subject: str) -> str: ...`

    Returns string with removed cases.

* `camel(subject: str) -> str: ...`

    Returns string in camelCase.
  
* `pascal(subject: str) -> str: ...`

    Returns string in PascalCase.
  
* `kebab(subject: str) -> str: ...`

    Returns string in kebab-case.
  
* `snake(subject: str) -> str: ...`

    Returns string in snake_case.

* `snake(subject: str, upper=False) -> str: ...`
  
    Returns string in snake_case.

    If `upper` is `True`, it will convert whole subject to upper snake case.

* `upper_first(subject: str) -> str: ...`
  
    Returns string with upper first letter (A-Z).
  
* `lower_first(subject: str) -> str: ...`

    Returns string with lower first letter (A-Z).

* `transform(subject: str, transformation: Callable, glue=" ") -> str: ...`

    Returns string transformed by the transformation function.
    The transformation function accepts 2 parameters: current word index (int), and a word itself (str).
    Glue is the string used to concat transformed words into one string.

## License

This project is licensed under Apache-2.0 License - see the [LICENSE](LICENSE) file for details.


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmarverix%2Fcasey.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmarverix%2Fcasey?ref=badge_large)
