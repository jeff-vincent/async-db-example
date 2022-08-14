FROM python:3.10
COPY ./worker/ .
COPY async_tasks.py .
RUN pip install -r requirements.txt
CMD ./run.sh
