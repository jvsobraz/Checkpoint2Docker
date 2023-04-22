FROM python

RUN apt-get -y update

RUN apt-get -y install python

RUN touch projeto-dimdim-dockercompose

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]