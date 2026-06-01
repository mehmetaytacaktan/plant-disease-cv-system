# 1. Use the official Python 3.10 slim image (slim keeps it lightweight)
FROM python:3.10-slim

# 2. Install system dependencies for OpenCV and Pillow as ROOT (Before switching users)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Create a non-root user for security (Hugging Face standard)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 4. Set the working directory inside the container
WORKDIR /app

# 5. Copy requirements and install dependencies as the 'user'
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 6. Copy the rest of the application files with proper ownership
COPY --chown=user . /app

# 7. Start the FastAPI server on port 7860 (Hugging Face default port)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]