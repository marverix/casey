# Casey
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmarverix%2Fcasey.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmarverix%2Fcasey?ref=badge_shield)


A simple library to support various string notation systems and convert strings from one to another.

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

subject = casey.camel(subject)
print(subject)
# Prints: every1WORDIsVeryIMPORTANT

subject = casey.kebab(subject)
print(subject)
# Prints: every-1-WORD-is-very-IMPORTANT

subject = casey.pascal(subject)
print(subject)
# Prints: Every1WORDIsVeryIMPORTANT

subject = casey.snake(subject)
print(subject)
# Prints: every_1_WORD_is_very_IMPORTANT

subject = casey.snake(subject, upper=True)
print(subject)
# Prints: EVERY_1_WORD_IS_VERY_IMPORTANT

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

## License

This project is licensed under Apache-2.0 License - see the [LICENSE](LICENSE) file for details.


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmarverix%2Fcasey.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmarverix%2Fcasey?ref=badge_large)