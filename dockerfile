FROM python:3.7.5-slim
RUN python3.7.5 --m pip install -r requirements.txt
CMD['python3.7.5', 'main.py']
