FROM python:3

#gitpod user will have be gitpod (uid 33333)

RUN apt-get update && \
    apt-get install postgresql-10 && \
    useradd -u 33333 gitpod &&\
    chown gitpod -R /var/lib/postgresql && \
    chown gitpod -R /var/run/postgresql && \
    chown gitpod -R /etc/postgresql/10

USER gitpod