import factory
from django.db.models import signals
from django.test import TestCase

from comic.eyra.models import Submission
from comic.eyra.tasks import create_algorithm_job_for_submission
from tests.factories import SubmissionFactory


class test_create_algorithm_job(TestCase):
    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_create_job_for_submission(self):
        submission: Submission = SubmissionFactory()
        self.assertIsNone(submission.algorithm_job)
        create_algorithm_job_for_submission(submission)
        self.assertIsNotNone(submission.algorithm_job)
