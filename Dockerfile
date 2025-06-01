from python:3.13.3

WORKDIR /api

COPY requirements.txt ./

RUN pip install -r requirements.txt


COPY . ./api

EXPOSE 8080

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]