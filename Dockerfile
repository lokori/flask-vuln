FROM python:2-alpine

EXPOSE 5000

RUN pip install flask
RUN mkdir /app && chown nobody:nobody /app
COPY --chown=nobody:nobody *.txt *.py *.html *.jpg run.sh /app/
USER nobody
WORKDIR /app
CMD ["./run.sh", "-h", "0.0.0.0"]
