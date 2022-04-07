FROM alpine:3.5

RUN apk add --update py3-pip

CMD ["python","/var/lib/jenkins/workspace/build-python/qualitymetrics/qualitymetrics/src/main.py"]
