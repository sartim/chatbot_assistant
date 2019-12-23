import re


def get_part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 22
        else
        "night"
    )


def capitalize(match):
    return match.group(0).upper()


def get_capitalized(content):
    return re.sub(
        r'(?:^\s*|[.?]\s+)(\w)', capitalize,
        content
    )
