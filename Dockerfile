FROM python:3.10

WORKDIR /tkww-api

COPY . /tkww-api

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry install

EXPOSE 80

CMD ["poetry", "run", "python", "app.py"]