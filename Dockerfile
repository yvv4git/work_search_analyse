FROM python:2.7

RUN mkdir -p /app
ADD . /app
WORKDIR /app

RUN pip install requests tabulate pandas

CMD ["./work_search_by_hhapi.sh"]
