# -*- coding: utf-8 -*-
from dataclasses import dataclass
from unittest.mock import patch

from django.db.models.signals import post_save
from django.test.testcases import TestCase
from factory.django import mute_signals

from comic.eyra.models import Submission
from comic.eyra.tasks import run_submission
from tests.factories import SubmissionFactory


def zilch(*args, **kwargs):
    pass


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

@dataclass
class DummyPodMetadata:
    name: str

@dataclass
class DummyPod:
    name: str
    @property
    def metadata(self):
        return DummyPodMetadata(self.name)


class DummyPodList:
    items = [
        DummyPod('input'),
        DummyPod('main'),
        DummyPod('output')
    ]


class DummyPodStatus:
    succeeded = True
    failed = False

@patch('comic.container_exec.backends.k8s.load_incluster_config', zilch)
@patch('comic.container_exec.backends.k8s.load_kube_config', zilch)
@patch('comic.container_exec.backends.k8s.K8sJob.create_io_pvc', zilch)
@patch('comic.container_exec.backends.k8s.client.BatchV1Api.create_namespaced_job', zilch)
@patch('comic.container_exec.backends.k8s.client.BatchV1Api.read_namespaced_job_status', lambda *args, **kwargs: dotdict({"status": DummyPodStatus()}))
@patch('comic.container_exec.backends.k8s.client.CoreV1Api.list_namespaced_pod', lambda *args, **kwargs: DummyPodList())
@patch('comic.container_exec.backends.k8s.client.CoreV1Api.delete_namespaced_pod', zilch)
@patch('comic.container_exec.backends.k8s.client.BatchV1Api.delete_namespaced_job', zilch)
@patch('comic.container_exec.backends.k8s.client.CoreV1Api.delete_namespaced_persistent_volume_claim', zilch)
@patch('comic.container_exec.backends.k8s.client.CoreV1Api.read_namespaced_pod_log', lambda *args, **kwargs: 'DummyLog')
class ContainerExecTest(TestCase):
    def test_create_job(self):
        submission: Submission = mute_signals(post_save)(SubmissionFactory)()
        self.assertIsNone(submission.algorithm_job)
        self.assertIsNone(submission.evaluation_job)

        run_submission(submission.pk)
        submission.refresh_from_db()
        self.assertIsNotNone(submission.algorithm_job)

        print(submission.algorithm_job)

    # def test_update_benchmark_no_crash(self):
    #     user = UserFactory()
    #     benchmark: Benchmark = BenchmarkFactory(
    #         creator=user
    #     )
    #     benchmark.description = "updated description"
    #     benchmark.save()

