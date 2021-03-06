FROM python:3

ADD golden.py .

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install numpy scikit-image opencv-python requests

CMD ["python", "./golden.py"]
