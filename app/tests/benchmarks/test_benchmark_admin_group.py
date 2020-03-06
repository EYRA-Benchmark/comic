from django.contrib.auth.models import Group
from django.test.testcases import TestCase

from comic.eyra.models import Benchmark
from tests.factories import BenchmarkFactory, UserFactory


class BenchmarkCreateTest(TestCase):
    def test_create_delete_admin_group_with_benchmark(self):
        user = UserFactory()
        benchmark: Benchmark = BenchmarkFactory(
            creator=user
        )
        benchmark_name = benchmark.name
        self.assertTrue(Group.objects.filter(name__contains=benchmark_name).exists())

        benchmark.delete()

        self.assertFalse(Group.objects.filter(name__contains=benchmark_name).exists())

    def test_update_benchmark_no_crash(self):
        user = UserFactory()
        benchmark: Benchmark = BenchmarkFactory(
            creator=user
        )
        benchmark.description = "updated description"
        benchmark.save()

