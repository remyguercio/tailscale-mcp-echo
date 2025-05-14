# Use the latest stable Python runtime as a parent image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ADD . /app

# Set working directory in the container
WORKDIR /app

# Install dependencies using UV
RUN uv sync --locked

# Make port 8080 available to the world outside this container
EXPOSE 8080

ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["fastmcp", "run", "main.py", "--transport", "streamable-http", "--port", "8080"]