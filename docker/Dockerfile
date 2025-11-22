# Set the base image to Python 3 (slim version)
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /home/app/web

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1


# Update packages and install system dependencies
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    nodejs \
    npm \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY ./requirements.txt /requirements.txt
# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the entrypoint script into the container
COPY ./entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod 0755 /entrypoint.sh

# Set the default command to run when the container starts
CMD [ "/entrypoint.sh" ]