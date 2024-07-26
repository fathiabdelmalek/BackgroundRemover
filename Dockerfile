FROM python:alpine
COPY u2net.onnx /home/.u2net/u2net.onnx
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5100
CMD ["python", "app.py"]