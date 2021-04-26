import re


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


def camel(subject: str) -> str:
    """
    Returns string in camelCase
    """
    normalized_subject = clean(subject)
    return re.sub(r" [a-z0-9]", lambda m: m.group(0)[1].upper(), normalized_subject, flags=re.IGNORECASE)


def pascal(subject: str) -> str:
    """
    Returns string in PascalCase
    """
    return upper_first(camel(subject))


def kebab(subject: str) -> str:
    """
    Returns string in kebab-case
    """
    normalized_subject = clean(subject)
    return re.sub(r"\s", '-', normalized_subject)


def snake(subject: str, upper=False) -> str:
    """
    Returns string in snake_case
    """
    normalized_subject = clean(subject)
    s = re.sub(r"\s", '_', normalized_subject)

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
