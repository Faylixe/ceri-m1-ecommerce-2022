FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ ./
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh
ENV PORT=8080
ENTRYPOINT ["sh", "entrypoint.sh"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
