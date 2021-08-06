from collections import UserString

from django.utils.translation import pgettext


class AttributiveTranslationMessage(UserString):
    def __init__(self, data):
        super().__init__(data)
        try:
            self.raw_data = data._proxy____args[0]
        except AttributeError:
            self.raw_data = data

    def __getattr__(self, item):
        try:
            return getattr(self.raw_data, item)
        except AttributeError:
            return pgettext(context=item, message=self.raw_data)

    def __html__(self):
        return self.data
