FROM ubuntu:19.10
LABEL maintainer="Abhishek N. Kulkarni <ankulkarni@wpi.edu>"


# =====================================================================================================================
# Ubuntu Utilities

# Set clock and timezone for docker image
RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get update && apt-get install -q -y tzdata && rm -rf /var/lib/apt/lists/*

# Package installation, setup, vcs, build utilities
RUN apt update && \
	RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive && \
	apt-get install -y software-properties-common wget nano make gcc g++ gnupg2 git cmake pkg-config build-essential

# Dependencies for IGraph
RUN apt update && \
	RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y libxml2-dev libtool zlib1g-dev bison flex


# =====================================================================================================================
# Python and Python Packages

# Python and development tools
RUN apt-get install -y python3-dev

# Setup utilities
RUN apt-get install -y python3-pip

# Must-have packages
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install pytest

# Documentation generation and coverage tools
RUN apt-get install -y python3-sphinx
RUN pip3 install sphinx_rtd_theme recommonmark
RUN pip3 install pytest-cov
RUN pip3 install coverage
RUN pip3 install codecov

# =====================================================================================================================
# Graph Libraries

# NetworkX
RUN pip3 install networkx

# Graph tool
RUN echo "deb [ arch=amd64 ] https://downloads.skewed.de/apt eoan main" | tee -a /etc/apt/sources.list && \
    apt-key adv --keyserver keys.openpgp.org --recv-key 612DEFB798507F25 && \
    apt-get update && \
    apt-get install -y python3-graph-tool

# Snap-Stanford (Python)
RUN pip3 install snap-stanford

# IGraph (Python)
RUN pip3 install python-igraph


# Snap (C++)
ADD thirdparty/snap-5.0.tar.gz /home/thirdparty

COPY thirdparty/CMakeLists-Snap.txt /home/thirdparty/CMakeLists-Snap.txt
RUN cp /home/thirdparty/CMakeLists-Snap.txt /home/thirdparty/Snap-5.0/CMakeLists.txt

COPY thirdparty/CMakeLists-Snap-glibcore.txt /home/thirdparty/CMakeLists-Snap-glibcore.txt
RUN cp /home/thirdparty/CMakeLists-Snap-glibcore.txt /home/thirdparty/Snap-5.0/glib-core/CMakeLists.txt

COPY thirdparty/CMakeLists-Snap-snapcore.txt /home/thirdparty/CMakeLists-Snap-snapcore.txt
RUN cp /home/thirdparty/CMakeLists-Snap-snapcore.txt /home/thirdparty/Snap-5.0/snap-core/CMakeLists.txt


# Lemon (C++)
ADD thirdparty/lemon-1.3.1.tar.gz /home/thirdparty
RUN mkdir /home/thirdparty/lemon-1.3.1/build && \
    cd /home/thirdparty/lemon-1.3.1/build && \
        cmake .. && \
        make && \
        make install && \
    cd /


# =====================================================================================================================
# Pybind11
ADD thirdparty/pybind11.tar.gz /home/thirdparty
RUN mv home/thirdparty/lib/pybind11 home/thirdparty/pybind11
RUN rm -rf home/thirdparty/lib

RUN mkdir /home/graph-benchmarking/
RUN mkdir /home/graph-benchmarking/lib
RUN cp -RT /home/thirdparty /home/graph-benchmarking/lib