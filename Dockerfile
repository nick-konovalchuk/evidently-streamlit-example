FROM python:3.10.13-slim

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

WORKDIR /home

COPY . .

ENTRYPOINT streamlit run app.py --server.address 0.0.0.0 --server.port 8100 --browser.gatherUsageStats False