FROM python:3.7
ENV PYTHONUNBUFFERED=1
COPY . .
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000