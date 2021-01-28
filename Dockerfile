FROM python

WORKDIR /opt/easycalc

COPY easycalc/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py", "api"]