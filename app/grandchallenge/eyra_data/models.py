import logging

from django.conf import settings
from django.db import models

from grandchallenge.core.models import UUIDModel

logger = logging.getLogger(__name__)


def get_data_file_name(obj, filename=None):
    return 'data_files/'+str(obj.id)


class DataType(UUIDModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    description = models.TextField(
        default="",
        blank=True,
        null=True,
        help_text="Description of this data type in markdown.",
    )

    def __str__(self):
        return self.name


class DataFile(UUIDModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="data_files",
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(
        default="",
        blank=True,
        null=True,
        help_text="Description of this file in markdown.",
    )
    type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    frozen = models.BooleanField(default=False)
    file = models.FileField(blank=True, null=True, upload_to=get_data_file_name)
    sha = models.CharField(max_length=40, null=True, blank=True)
    original_file_name = models.CharField(null=True, blank=True, max_length=150)

    def __str__(self):
        return self.name


class DataSet(UUIDModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="data_sets",
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(
        default="",
        blank=True,
        null=True,
        help_text="Description of this data set in markdown.",
    )
    test_data_file = models.ForeignKey(
        DataFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    test_ground_truth_data_file = models.ForeignKey(
        DataFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    data_files = models.ManyToManyField(
        DataFile,
        related_name='data_sets',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name