FROM ubuntu

WORKDIR /app

RUN apt-get update
# Install python
RUN apt-get -y install python3-pip 
# Create python virtual enviroment
RUN apt-get -y install python3-venv
RUN apt-get -y install libglib2.0-0 libgthread-2.0-0 libsm6 libxext6 libxrender-dev 
RUN apt-get -y install libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 libsdl2-image-2.0-0
# Install pygame in virtual enviroment
RUN python3 -m venv /app/venv
RUN /app/venv/bin/pip install pygame

ENV PATH="/app/venv/bin:$PATH"

EXPOSE 5000

COPY . .

CMD [ "python3", "pingpongv4.py" ]

# FROM python

# WORKDIR /app

# RUN apt-get update
# RUN apt-get -y install python3
# RUN pip install -U pygame==2.6.0

# EXPOSE 5000

# COPY . . 

# CMD [ "python3", "pingpongv4.py" ]