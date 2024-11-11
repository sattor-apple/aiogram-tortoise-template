# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for the bot token and database URL
# Ensure that you have .env in your project with required environment variables
COPY .env /app/.env

# Expose the port your bot might use, default to 8000
EXPOSE 8000

# Run the bot
CMD ["python", "app.py"]
