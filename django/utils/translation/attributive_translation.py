from collections import UserString

from django.utils.functional import Promise
from . import gettext, pgettext_nocontext_fallback

def make_attributive(message):
    if isinstance(message, str):
        return DummyAttributiveString(message)
    elif isinstance(message, Promise) and message.__reduce__()[1][0] == gettext:  # is lazy gettext
        return AttributiveTranslationMessage(message)
    return message


class DummyAttributiveString(str):
    def __getattr__(self, item):
        return self

class AttributiveTranslationMessage(UserString):
    def __init__(self, data):
        self.data = data

    def __getattr__(self, item):
        return pgettext_nocontext_fallback(
            context=item, message=self.data._proxy____args[0]
        )
