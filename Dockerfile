# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY ./docker/requirements.txt .
RUN python -m pip install -r requirements.txt

RUN apt-get update -y \    
    && apt-get install python3-opencv -y \
    && apt-get install unzip \
    && apt-get install zip

WORKDIR /app
COPY . /app

WORKDIR /app/models
COPY . /app/models


#RUN zip -s 40m -r WilhemNet_86.zip WilhemNet_86.h5
#RUN split -b 40m  WilhemNet_86.h5 segment
RUN echo "SE DEBE UNIR LOS ARCHIVOS"
RUN cat segment* > WilhemNet_86.h5
RUN ls

WORKDIR /app
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
