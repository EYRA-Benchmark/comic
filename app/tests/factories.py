import random

import factory
from factory.faker import faker
from django.conf import settings

from comic.eyra.models import Algorithm, Benchmark, DataFile, Submission, DataSet, Job

fake = faker.Faker()

SUPER_SECURE_TEST_PASSWORD = "testpasswd"


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: f"test_user_{n:04}")
    email = factory.LazyAttribute(lambda u: "%s@test.com" % u.username)
    password = factory.PostGenerationMethodCall(
        "set_password", SUPER_SECURE_TEST_PASSWORD
    )
    is_active = True
    is_staff = False
    is_superuser = False


class DataFileFactory(factory.DjangoModelFactory):
    class Meta:
        model = DataFile

    creator = factory.SubFactory(UserFactory)
    file = factory.PostGeneration(lambda obj, create, extracted, **kwargs: f'data_files/{obj.id}')


class DataSetFactory(factory.DjangoModelFactory):
    class Meta:
        model = DataSet

    name = "Dataset..."
    creator = factory.SubFactory(UserFactory)
    public_test_data_file = factory.SubFactory(DataFileFactory)
    public_ground_truth_data_file = factory.SubFactory(DataFileFactory)


class BenchmarkFactory(factory.DjangoModelFactory):
    class Meta:
        model = Benchmark

    creator = factory.SubFactory(UserFactory)
    name = 'Test-benchmark'
    about = 'Bladiebbla'
    short_description = 'Test benchmark short description'
    description = 'Test benchmark description'
    data_description = 'Test bm data description'
    truth_description = 'Test bm truth description'
    metrics_description = 'Test bm metrics description'
    data_set = factory.SubFactory(DataSetFactory)


class AlgorithmFactory(factory.DjangoModelFactory):
    class Meta:
        model = Algorithm

    creator = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: "Test algorithm %03d" % n)
    description = 'Test benchmark description'

    tags = [fake.color_name() for i in range(0, random.randint(1, 4))]


class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Submission

    creator = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: "Test submission %03d" % n)

    benchmark = factory.SubFactory(BenchmarkFactory)
    algorithm = factory.SubFactory(AlgorithmFactory)
    image = 'test_image'

#
# class JobFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = Job
#
#     submission = factory.SubFactory(SubmissionFactory)
