FROM python:3.12-alpine
LABEL authors="gabrielloliveira"

# Set the working directory
WORKDIR /app
# Install Project Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the application code
COPY . .
# Expose the port the app runs on
EXPOSE 80
# Command to run the application
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "80"]
