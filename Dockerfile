# Tic-Tac-Toe Web App - Production Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Flask (no external requirements.txt needed)
RUN pip install --no-cache-dir Flask==3.0.3

# Copy application code
COPY app.py .
COPY templates/ ./templates/

# Expose port 5000
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
