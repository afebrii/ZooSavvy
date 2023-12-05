# parent image
FROM python:3.7-slim

# Set working directory ke /app
WORKDIR /app

RUN mkdir -p /app/chatbot

COPY ./chatbot /app/chatbot

# Set the working directory ke /app/chatbot
WORKDIR /app/chatbot

# Install packages yang ada di requirements.txt
COPY ./chatbot/requirements.txt /app/chatbot/requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Reset working directory kembali ke /app
WORKDIR /app

# buat port 8080 
EXPOSE 8080

# enviironment variable
ENV NAME World

# run App.py
CMD ["python", "App.py"]