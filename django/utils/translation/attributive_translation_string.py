from django.utils.translation import gettext, is_lazy_gettext, pgettext


class AttributiveTranslationString(str):
    def __init__(self, message):
        super().__init__(gettext(message=message))
        self.message = message

    def __getattr__(self, context):
        return pgettext(context=context, message=self.message)

    @classmethod
    def create(cls, obj):
        if is_lazy_gettext(obj):
            return cls(obj._proxy____args[0])
        return DummyAttributiveString(obj)


class DummyAttributiveString(str):
    def __getattr__(self, context):
        return self
