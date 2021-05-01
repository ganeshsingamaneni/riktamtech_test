FROM ubuntu:18.04

FROM python:3.6
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get -y install cmake protobuf-compiler
RUN apt-get install -y git
# RUN git clone https://github.com/davisking/dlib.git

# RUN cd dlib
# RUN mkdir build
# RUN cd build
# RUN cmake ..
# RUN cmake --build .
# RUN cd ..
# RUN apt-get install -y --fix-missing \
#     build-essential \
#     cmake \
#     gfortran \
#     git \
#     wget \
#     curl \
#     graphicsmagick \
#     libgraphicsmagick1-dev \
#     libatlas-base-dev \
#     libavcodec-dev \
#     libavformat-dev \
#     libgtk2.0-dev \
#     libjpeg-dev \
#     liblapack-dev \
#     libswscale-dev \
#     pkg-config \
#     python3-dev \
#     python3-numpy \
#     && apt-get clean && rm -rf /tmp/* /var/tmp/*

# RUN cd ~ && \
#     mkdir -p dlib && \
#     git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
#     cd  dlib/ && \
#     python3 setup.py install --yes USE_AVX_INSTRUCTIONS


# RUN python3 setup.py install --yes USE_AVX_INSTRUCTIONS

RUN cd ..


COPY ./requirements.txt /app/requirements.txt 

WORKDIR /app

# Copy the current directory contents into the container /app where . is the relative directory AKA flask
ADD . /app

RUN pip3 install -r requirements.txt 

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]


