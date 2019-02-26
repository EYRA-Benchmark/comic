# Generated by Django 2.1.7 on 2019-02-26 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eyra_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('description', models.TextField(blank=True, default='', help_text='Description of this algorithm in markdown.')),
                ('container', models.CharField(max_length=64, unique=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='algorithms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('output_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='eyra_data.DataType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Started'), (2, 'Re-Queued'), (3, 'Failed'), (4, 'Succeeded'), (5, 'Cancelled')], default=0)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('stopped', models.DateTimeField(blank=True, null=True)),
                ('log', models.TextField(blank=True, null=True)),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eyra_algorithms.Algorithm')),
                ('output', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output_of_job', to='eyra_data.DataFile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobInput',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('data_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_inputs', to='eyra_data.DataFile')),
                ('input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='eyra_algorithms.Input')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='eyra_algorithms.Job')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='input',
            name='interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='eyra_algorithms.Interface'),
        ),
        migrations.AddField(
            model_name='input',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='eyra_data.DataType'),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algorithms', to='eyra_algorithms.Interface'),
        ),
    ]
