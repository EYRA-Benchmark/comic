## Backend for the EYRA Benchmark platform.

.. image:: https://travis-ci.org/EYRA-Benchmark/comic.svg?branch=master
  :target: https://travis-ci.org/EYRA-Benchmark/comic
    

.. image:: https://readthedocs.org/projects/eyra/badge/?version=latest
  :target: https://eyra.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status
  
  
.. image:: https://sonarcloud.io/api/project_badges/measure?project=EYRA-Benchmark_comic&metric=coverage
  :target: https://sonarcloud.io/component_measures?id=EYRA-Benchmark_comic&metric=coverage


.. image:: https://sonarcloud.io/api/project_badges/measure?project=EYRA-Benchmark_comic&metric=alert_status
  :target: https://sonarcloud.io/component_measures?id=EYRA-Benchmark_comic
  
  
.. image:: https://sonarcloud.io/api/project_badges/measure?project=EYRA-Benchmark_comic&metric=security_rating
  :target: https://sonarcloud.io/component_measures?id=EYRA-Benchmark_comic
  
  
.. image:: https://sonarcloud.io/api/project_badges/measure?project=EYRA-Benchmark_comic&metric=sqale_rating
  :target: https://sonarcloud.io/component_measures?id=EYRA-Benchmark_comic


.. image:: https://pyup.io/repos/github/EYRA-Benchmark/comic/shield.svg
  :target: https://pyup.io/repos/github/EYRA-Benchmark/comic/
  :alt: Updates
  
  
`Read the docs <https://eyra.readthedocs.io>`_.

Forked from `grand-challenge.org <https://github.com/comic/grand-challenge.org/>`_.

## Setup a dev environment:

- Use miniconda3 https://docs.conda.io/en/latest/miniconda.html
- Create a virtual environment: ``conda create -n comic python=3``
- Activate environment: ``conda activate comic``
- Install dependencies: ``pip install -r requirements.txt && pip install -r requirements.dev.txt``
- Install our repo in edit mode: ``pip install -e app``
- Install docker-compose: ``pip install docker-compose``
- Setup ``.env``: ``cp .env.dev .env``
- Start containers: ``docker-compose up postgres redis``
- Run the database migrations: ``cd app; python manage.py migrate; python manage.py init_db_data``

- Install VSCode Python extension
- Set the correct python path in ``.vscode/settings.json`` (``"python.pythonPath"``).
- Launch ``Python: Django``, server should start running at ``http://localhost:8000``.


