FROM python:3.7
WORKDIR /usr/local/bin
COPY dot-proxy.py .
CMD ["python3", "dot-proxy.py"]
