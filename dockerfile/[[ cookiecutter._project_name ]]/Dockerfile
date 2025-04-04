FROM [[ cookiecutter.image ]]

RUN apk update && apk upgrade --no-cache
RUN apk add gettext busybox openrc su-exec

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_DEBUG false
ENV DJANGO_DB_DIR '/var/data/django-cron/db'
RUN mkdir -p ${DJANGO_DB_DIR}

WORKDIR /opt/app

COPY requirements.txt /opt/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /opt/app/

RUN addgroup -S app-group && adduser -S app-user -G app-group
RUN chown app-user:app-group ${DJANGO_DB_DIR} -R

RUN chmod u+s /usr/sbin/crond

RUN chmod +x /usr/local/bin/root-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/root-entrypoint.sh"]

RUN chmod +x /usr/local/bin/user-entrypoint.sh
CMD ["./user-entrypoint.sh"]
