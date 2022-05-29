import os
from unittest import TestCase

from django.conf import settings
from django.test import SimpleTestCase, override_settings
from django.utils.translation.attributive_translation import make_attributive
from django.utils.translation import gettext_lazy, override

here = os.path.dirname(os.path.abspath(__file__))
extended_locale_paths = settings.LOCALE_PATHS + [
    os.path.join(here, "other", "locale"),
]

class TestAttributiveTranslationString(TestCase):
    def test_makes_regular_string_attributive(self):
        attributive_string = make_attributive("foo")
        self.assertEqual(attributive_string, "foo")
        self.assertEqual(attributive_string.bar, "foo")

    def test_lazy_gettext_attributive_fallbacks(self):
        attributive_string = make_attributive(gettext_lazy("foo"))
        self.assertEqual(attributive_string, "foo")
        self.assertEqual(attributive_string.bar, "foo")


class TestAttributiveTranslationStringDjango(SimpleTestCase):
    @override_settings(LOCALE_PATHS=extended_locale_paths)
    def test_lazy_gettext_attributive_translates_attributes(self):
        attributive_string = make_attributive(gettext_lazy("father"))
        with override("de"):
            self.assertEqual(attributive_string, "Vater")
            self.assertEqual(attributive_string.genitive, "Vaters")
