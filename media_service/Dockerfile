FROM python:3.8.3-slim
COPY . /app
WORKDIR /app
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt --default-timeout=100 && \
    chmod +x entrypoint.sh
CMD [ "/app/entrypoint.sh" ]