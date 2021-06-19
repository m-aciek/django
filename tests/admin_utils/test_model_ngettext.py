from unittest.mock import patch

from django.contrib.admin.utils import model_ngettext
from django.db import models
from django.test import TestCase
from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _


class ModelNgettextTests(TestCase):
    @patch('django.contrib.admin.utils.ngettext')
    def test_model_ngettext(self, ngettext):
        def fake_gettext(message):
            return {'foo': 'troo', 'foos': 'troos'}[message]

        _ = lazy(fake_gettext, str)

        class Foo(models.Model):
            class Meta:
                verbose_name = _('foo')
                verbose_name_plural = _('foos')

        result = model_ngettext(Foo(), None)
        self.assertEqual(ngettext.call_args.args[0], 'foo')
        self.assertEqual(ngettext.call_args.args[1], 'foos')
        self.assertEqual(result, 'foos')
