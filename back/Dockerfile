# FROM python:3.8
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
# ENTRYPOINT ["uvicorn","main:app"]

#install FastAPI

# FROM python:3.7
# RUN pip3 install fastapi uvicorn
# RUN pip3 install sqlmodel
# RUN pip3 install PyMySQL
# RUN pip3 install mysqlclient
# RUN pip3 install psycopg2
# WORKDIR /back
# COPY . .
# #EXPOSE  8000
# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"]

# 
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

RUN apt update -y && apt install -y libmariadb3 libmariadb-dev

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ ./

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
