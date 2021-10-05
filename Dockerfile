FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/aykhan026/bozqurd /root/bozqurd
WORKDIR /root/bozqurd/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
