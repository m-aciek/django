from collections import UserString

from django.utils.translation import gettext, pgettext


class AttributiveTranslationMessage(UserString):
    def __init__(self, data):
        super().__init__(gettext(data))
        self.raw_data = data

    def __getattr__(self, item):
        return pgettext(context=item, message=self.raw_data)


class DummyAttributiveMessage(UserString):
    def __getattr__(self, item):
        return self.data
