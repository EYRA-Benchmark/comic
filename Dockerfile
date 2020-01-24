FROM python:3.8

RUN apt-get update && \
    apt-get install -y \
    python-openssl \
    libpng-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libxft-dev \
    libffi-dev \
    wget \
    gettext

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app /static

WORKDIR /app

# Install base python packages
ADD requirements.txt /app
ADD requirements.dev.txt /app
RUN pip install -r requirements.txt && pip install -r requirements.dev.txt

ADD ./app/ /app/

RUN chown 2001:2001 /static
RUN chown 2001:2001 /app

USER 2001:2001

RUN python manage.py collectstatic

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0", "config.wsgi", "--log-level debug"]
