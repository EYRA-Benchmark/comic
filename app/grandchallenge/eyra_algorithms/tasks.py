from datetime import datetime
import time

from celery import shared_task

from grandchallenge.container_exec.backends.k8s import K8sJob
from grandchallenge.eyra_algorithms.models import Job


@shared_task
def run_job(job_pk):
    """Celery task for running a job.

    Args:
        job_pk: the primary key of the Job object that defines the algorithm run
    """
    job = Job.objects.get(pk=job_pk)
    with K8sJob(job) as k8s_job:
        k8s_job.run()
        job.status = Job.STARTED
        job.started = datetime.now()
        job.save()
        while True:
            s = k8s_job.status()
            job.log = k8s_job.get_text_logs()
            job.save()

            if s.failed or s.succeeded:
                break

            time.sleep(5)

        job.status = Job.SUCCESS if s.succeeded else Job.FAILURE
        job.log = k8s_job.get_text_logs()
        job.stopped = datetime.now()
        job.save()

    if not s.succeeded:
        raise Exception("Job failed")
