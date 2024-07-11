FROM python:3.9

# Create a group and user to run our app
ARG APP_USER=test_user
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

COPY requirements.txt /usr/src/app/
RUN pip3 install -r /usr/src/app/requirements.txt

# NB comment this *out* -> no error; leave it in to see the error
# Change to a non-root user
USER ${APP_USER}:${APP_USER}

COPY test.py /usr/src/app/

WORKDIR /usr/src/app

CMD ["python", "test.py"]
