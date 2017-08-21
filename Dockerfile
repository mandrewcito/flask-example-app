FROM ubuntu:12.04

MAINTAINER Andrés Baamonde Lozano

RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi python-dev python-pip && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install Flask
#enable mod_wsgi
#RUN a2enmod wsgi

#ENV APACHE_RUN_USER www-data
#ENV APACHE_RUN_GROUP www-data
#ENV APACHE_LOG_DIR /var/log/apache2

COPY src /var/www/src

#Creamos el virtual host
COPY resources/docker/app /etc/apache2/sites-available/appflask
RUN a2ensite appflask

EXPOSE 8080
#CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
CMD ["python","/var/www/src/run.py"]
