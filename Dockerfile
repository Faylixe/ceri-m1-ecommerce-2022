# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update -y && apt-get build-dep python-mysqldb
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
#slt