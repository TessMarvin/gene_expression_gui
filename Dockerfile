FROM python:3
ADD gui_dashboard.py /
RUN pip install matplotlib pandas
CMD tail -f /dev/null
