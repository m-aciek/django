from collections import UserString

from django.utils.translation import gettext, is_lazy_gettext, pgettext


class AttributiveTranslationString(UserString):
    def __init__(self, data):
        super().__init__(gettext(data))
        self.raw_data = data

    def __getattr__(self, item):
        return pgettext(context=item, message=self.raw_data)

    @classmethod
    def create(cls, obj):
        if is_lazy_gettext(obj):
            return cls(obj._proxy____args[0])
        return DummyAttributiveString(obj)


class DummyAttributiveString(UserString):
    def __getattr__(self, item):
        return self.data
