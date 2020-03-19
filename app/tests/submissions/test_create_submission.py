from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.test.testcases import TestCase
from factory.django import mute_signals

from tests.factories import SubmissionFactory

MutedFactory = mute_signals(post_save)(SubmissionFactory)


class SubmissionCreateTest(TestCase):
    def test_create_valid_submission(self):
        submission = MutedFactory(
            image='alpine:latest'
        )

    def test_create_invalid_image_submission(self):
        with self.assertRaises(ValidationError):
            submission = MutedFactory(
                image='blsfsdfd:3'
            )
