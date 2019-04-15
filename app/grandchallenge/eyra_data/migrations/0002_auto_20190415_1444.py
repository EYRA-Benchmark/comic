# Generated by Django 2.1.7 on 2019-04-15 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eyra_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='', help_text='Description of this data set in markdown.', null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data_sets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='datafile',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Description of this file in markdown.', null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='data_files',
            field=models.ManyToManyField(related_name='data_sets', to='eyra_data.DataFile'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='test_data_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eyra_data.DataFile'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='test_ground_truth_data_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eyra_data.DataFile'),
        ),
    ]
