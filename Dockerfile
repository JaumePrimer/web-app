# Use an official Python image
FROM python:3.7

# Copy local code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies
RUN pip install -r ./requirements.txt

# Run the web service.
# The number of threads should equal the number of workers in the case
# of multiple CPU cores.
CMD ["python", "app.py"]
