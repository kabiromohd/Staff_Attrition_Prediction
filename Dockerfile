FROM python:3.11-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "best_model_capst.pkl", "dicv.pkl", "./"]

EXPOSE 9690

ENTRYPOINT ["pipenv", "run", "gunicorn", "--bind=0.0.0.0:6090", "predict:app"]