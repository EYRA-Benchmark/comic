"""
Migrate, use this file to migrate data from the old models (with data types) to then style (without types)
~ 2020-01
- python manage.py dumpdata > data.prod.json
- run this script
- python manage.py loaddata migrate_data.json (in new backend)
"""

import json
f = open('data.prod.json', 'r')
data = json.loads(f.read())
f.close()

skip_models = [
    'django_celery_results.taskresult',
    'django_celery_beat.intervalschedule',
    'django_celery_beat.crontabschedule',
    'django_celery_beat.periodictasks',
    'django_celery_beat.periodictask',
  # 'contenttypes.contenttype',
  'sessions.session',
  'eyra_algorithms.input',
  'eyra_algorithms.interface',
  'eyra_algorithms.job',
  'eyra_algorithms.jobinput',
  'eyra_algorithms.implementation',
  'eyra_data.datatype',
  'admin.logentry',
  'guardian.groupobjectpermission',
  'social_django.usersocialauth',
  'authtoken.token'
]

def find_by_pk(pk):
    return [d for d in data if d['pk'] == pk][0]

def find_referring_pk(record, key_name):
    return [d for d in data if key_name in d['fields'] and d['fields'][key_name] == record['pk']]

new_data = []
for record in data:
    if record['model'] in skip_models: continue
    elif record['model'] == 'eyra_benchmarks.benchmark':
        record['model'] = 'eyra.benchmark'
        if record['fields']['evaluator']:
            record['fields']['evaluation_image'] = find_by_pk(record['fields']['evaluator'])['fields']['image']
        del record['fields']['interface']
        del record['fields']['evaluator']
        new_data.append(record)

    elif record['model'] == 'eyra_benchmarks.submission':
        record['model'] = 'eyra.submission'
        record['fields']['algorithm'] = find_by_pk(record['fields']['implementation'])['fields']['algorithm']
        del record['fields']['implementation']
        record['fields']['algorithm_job'] = record['fields']['implementation_job']
        del record['fields']['implementation_job']
        new_data.append(record)

        algo_job = find_by_pk(record['fields']['algorithm_job'])
        algo_job['model'] = 'eyra.job'
        del algo_job['fields']['implementation']
        new_data.append(algo_job)

        job_inputs = find_referring_pk(algo_job, 'job')
        for job_input in job_inputs:
            job_input['model'] = 'eyra.jobinput'
            job_input['fields']['name'] = find_by_pk(job_input['fields']['input'])['fields']['name']
            del job_input['fields']['input']
            new_data.append(job_input)

        eval_job = find_by_pk(record['fields']['evaluation_job'])
        eval_job['model'] = 'eyra.job'
        if 'implementation' in eval_job['fields']:
            del eval_job['fields']['implementation']
        new_data.append(eval_job)

        job_inputs = find_referring_pk(eval_job, 'job')
        for job_input in job_inputs:
            job_input['model'] = 'eyra.jobinput'
            job_input['fields']['name'] = find_by_pk(job_input['fields']['input'])['fields']['name']
            del job_input['fields']['input']
            new_data.append(job_input)

    elif record['model'] == 'eyra_algorithms.algorithm':
        record['model'] = 'eyra.algorithm'
        record['fields']['tags'] = []
        del record['fields']['interface']
        new_data.append(record)

    elif record['model'] == 'eyra_data.datafile':
        record['model'] = 'eyra.datafile'
        del record['fields']['format']
        del record['fields']['type']
        new_data.append(record)

    elif record['model'] == 'eyra_data.dataset':
        record['model'] = 'eyra.dataset'
        new_data.append(record)

    else:
        new_data.append(record)


f = open('migrate_data.json', 'w')
f.write(json.dumps(new_data))
f.close()
