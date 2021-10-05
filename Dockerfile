FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/aykhan026/bozqurduserbot /root/bozqurduserbot
WORKDIR /root/bozqurduserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
