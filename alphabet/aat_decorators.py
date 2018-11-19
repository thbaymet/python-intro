def list_decorator(list_items):
    return "<ul>" + list_items + "</ul>"


def list_item_decorator(item):
    return '<li>' + item() + '</li>'


@list_decorator
@list_item_decorator
def country_name():
    return "United States of America"


print(country_name)
