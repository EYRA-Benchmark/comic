from django.test.testcases import TestCase

from comic.eyra.models import Algorithm
from tests.factories import AlgorithmFactory, UserFactory


class AlgorithmUpdateTest(TestCase):
    def test_update_algorithm(self):
        user = UserFactory()
        algorithm: Algorithm = AlgorithmFactory(
            creator=user
        )
        algorithm.description = "new description"
        algorithm.save()
