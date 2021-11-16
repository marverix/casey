import re
from typing import List, Callable, Union
from inspect import signature


def clean(subject: str) -> str:
    """
    Returns string with removed cases
    """

    # detect capitalized snake case
    if re.match(r"^[A-Z][A-Z0-9_]+$", subject):
        return subject.replace('_', ' ').lower()

    # clean kebab and snake case
    subject = re.sub(r"[-_]", ' ', subject)

    # clean special characters
    subject = re.sub(r"[^a-z0-9 ]", '', subject, flags=re.IGNORECASE)

    # clean pascal case
    subject = lower_first(subject)

    # clean camel case
    subject = re.sub(r"([A-Za-z])([0-9])", lambda m: m.group(1) + ' ' + m.group(2), subject)
    subject = re.sub(r"[A-Z][a-z]", lambda m: ' ' + m.group(0).lower(), subject)
    subject = re.sub(r"([a-z0-9])([A-Z])", lambda m: m.group(1) + ' ' + m.group(2), subject)

    # minimize white spaces
    subject = re.sub(r"\s{2,}", ' ', subject.strip())

    return subject


def clean_list(subject: str) -> List[str]:
    return clean(subject).split(" ")


def transform(subject: str, transformation: Union[Callable, None], glue=" ") -> str:
    normalized = clean_list(subject)
    words = []

    if transformation:
        sig = signature(transformation)
        params_number = len(sig.parameters)

        for idx, word in enumerate(normalized):
            if params_number == 0:
                w = transformation()
            elif params_number == 1:
                w = transformation(word)
            elif params_number == 2:
                w = transformation(word, idx)
            else:
                raise Exception("Wrong number of arguments for transformation")
            words.append(w)
    else:
        words = normalized

    return glue.join(words)


def _camel_transformation(word: str, idx: int) -> str:
    if idx == 0:
        return word
    else:
        return upper_first(word)


def camel(subject: str) -> str:
    """
    Returns string in camelCase
    """
    return transform(subject, _camel_transformation, "")


def _pascal_transformation(word: str, _) -> str:
    return upper_first(word)


def pascal(subject: str) -> str:
    """
    Returns string in PascalCase
    """
    return transform(subject, _pascal_transformation, "")


def kebab(subject: str) -> str:
    """
    Returns string in kebab-case
    """
    return transform(subject, None, "-")


def snake(subject: str, upper=False) -> str:
    """
    Returns string in snake_case
    """
    s = transform(subject, None, "_")

    if upper:
        s = s.upper()

    return s


def upper_first(subject: str) -> str:
    """
    Returns string with upper first letter
    """
    return re.sub(r"[a-z]", lambda m: m.group(0).upper(), subject, 1, flags=re.IGNORECASE)


def lower_first(subject: str) -> str:
    """
    Returns string with lower first letter
    """
    return re.sub(r"[a-z]", lambda m: m.group(0).lower(), subject, 1, flags=re.IGNORECASE)
