# Use an official Python image
FROM python:3.7

# Copy local code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies
RUN pip install -r ./requirements.txt

# Run the web service through python.
CMD gunicorn --workers=10 \
             --worker-class="egg:meinheld#gunicorn_worker" \
             --bind=0.0.0.0:8800 \
             app:app
