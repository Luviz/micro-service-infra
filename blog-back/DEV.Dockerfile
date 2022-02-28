FROM python:3.10
EXPOSE 80

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip

WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV DB_URL=http://localhost:8000
ENV TABLE_NAME=blogs

COPY . .

CMD ["uvicorn", "app.blog:app", "--reload", "--host", "0.0.0.0", "--port", "80"]

