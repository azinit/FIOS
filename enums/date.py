__MONTHS = {
    "ru": ["январь",  "ферваль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"],
    "en": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"],
}


def get_months(locale="en"):
    src = __MONTHS.get(locale)
    if src:
        return src
    else:
        pass
