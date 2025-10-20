FROM python:alpine
WORKDIR /custom/file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
COPY . .
CMD [ "gunicorn", "--bind","0.0.0.0:3000","app:app" ]