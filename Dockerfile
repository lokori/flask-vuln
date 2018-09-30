FROM python:2-alpine

EXPOSE 5000

RUN pip install flask
RUN mkdir -p /app/templates && chown nobody:nobody /app
COPY --chown=nobody:nobody *.txt *.py *.html *.jpg run.sh /app/
COPY --chown=nobody:nobody templates/* /app/templates/
USER nobody
WORKDIR /app
CMD ["./run.sh", "-h", "0.0.0.0"]
