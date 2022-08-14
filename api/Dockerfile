FROM python:3.10
COPY ./api/ .
COPY async_tasks.py .
RUN pip3 install -r requirements.txt
CMD python main.py
