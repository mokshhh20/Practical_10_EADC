FROM python:3.8-alpine
COPY ./requirements.txt /moksh/requirements.txt
WORKDIR /moksh
RUN pip install -r requirements.txt
COPY . /moksh
ENTRYPOINT [ "python" ]
CMD ["view.py" ]