FROM python:3
RUN apt-get update && apt-get install -y libsasl2-dev libldap2-dev inotify-tools && pip install python-ldap
COPY nginx-ldap-auth-daemon /
COPY autoreload.sh /
COPY data_file_descriptor.py
CMD [ "/autoreload.sh" ]
