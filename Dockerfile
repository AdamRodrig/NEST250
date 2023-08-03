FROM python:3.7.4-slim-buster

WORKDIR /app
ENV EXCEL_HASH="667af75ede8ee0a165d34094578ab83112be155749b34a79135c6eefcaa656a1  Book1.xlsx"

COPY . .

RUN pip install -r requirements.txt
CMD [ "python3", "excel.py" ]
