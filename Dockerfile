FROM python:3.7.7-slim-buster

RUN pip3 install pip --upgrade
RUN apt-get update

#Prophet from Dockerfile.base ea-arodek
RUN apt-get -y install gcc g++ build-essential apt-utils
RUN pip3 install Cython cmdstanpy numpy pandas matplotlib LunarCalendar convertdate holidays setuptools-git python-dateutil tqdm
RUN pip3 install pystan==2.19.1.1 --no-cache

# Camelot dependecy
#RUN apt-get install -y libgl1-mesa-dev libglib2.0-0  ghostscript python3-tk
RUN apt-get update && apt-get install ghostscript python3-tk -y
RUN pip3 install fbprophet --no-cache
RUN pip3 install camelot-py[cv]==0.10.1 --no-cache


# PostgreSQL dependecies
RUN apt-get update && apt-get install libpq-dev -y

# pre installing python packages that we want to keep at certain versions. from Dockerfile.base ea-arodek
RUN mkdir -p /tmp/data

# Copying application
COPY . /ps-energy-dl
RUN pip3 install /ps-energy-dl --no-cache