FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Start the application using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
