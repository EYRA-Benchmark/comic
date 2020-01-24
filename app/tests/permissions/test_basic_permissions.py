from django.test import TestCase
from guardian.shortcuts import assign_perm

from comic.eyra.models import Benchmark
from tests.factories import BenchmarkFactory, UserFactory


class PermissionTest(TestCase):
    def test_default_false(self):
        user = UserFactory()
        benchmark: Benchmark = BenchmarkFactory()

        self.assertFalse(user.has_perm('eyra.change_benchmark'))
        self.assertFalse(user.has_perm('eyra.change_benchmark', benchmark))

    def test_give_object_permission(self):
        user = UserFactory()
        benchmark: Benchmark = BenchmarkFactory()
        assign_perm('eyra.change_benchmark', user, benchmark)
        self.assertFalse(user.has_perm('eyra.change_benchmark'))
        self.assertTrue(user.has_perm('eyra.change_benchmark', benchmark))

    def test_give_model_permission(self):
        user = UserFactory()
        benchmark: Benchmark = BenchmarkFactory()

        assign_perm('eyra.change_benchmark', user)
        self.assertTrue(user.has_perm('eyra.change_benchmark'))
        self.assertFalse(user.has_perm('eyra.change_benchmark', benchmark))
