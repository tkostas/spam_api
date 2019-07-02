FROM python:3.7-slim
RUN mkdir /api
WORKDIR /api
COPY . ./
RUN \
 pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt && \
 pip install --no-cache-dir gunicorn
RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]