from unittest import TestCase
from unittest.mock import patch

from django.utils.translation import gettext_lazy
from django.utils.translation.attributive_translation_message import (
    AttributiveTranslationMessage,
)


class TranslationTestCase(TestCase):
    @patch(
        'django.utils.translation.attributive_translation_string.pgettext_nocontext_fallback',
        return_value='troo',
    )
    def test_accessing_attribute_causes_call_of_pgettext(
        self, pgettext_nocontext_fallback_mock
    ):
        self.assertEqual(
            'troo',
            AttributiveTranslationMessage.create(
                gettext_lazy('foo')._proxy____args[0]
            ).bar,
        )
        pgettext_nocontext_fallback_mock.assert_called_with(
            context='bar', message='foo'
        )

    @patch(
        'django.utils.translation.attributive_translation_string.gettext',
        return_value='ploo',
    )
    def test_accessing_directly_causes_call_of_gettext(self, gettext_mock):
        self.assertEqual(
            'ploo', AttributiveTranslationMessage(gettext_lazy('foo')._proxy____args[0])
        )
        gettext_mock.assert_called_with('foo')

    def test_creation_prevents_failure_when_raw_string_provided(self):
        self.assertEqual('foo', AttributiveTranslationMessage('foo'.bar))
