from django.test import TestCase

from comic.eyra.tasks import sleep_one_sec


class TestBasicTask(TestCase):
    def test_sleep_one_sec(self):
        r = sleep_one_sec.delay()
        self.assertEqual(r.result, 42)