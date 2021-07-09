FROM centos

RUN yum install python3 -y

RUN pip3 install scikit-learn 

RUN pip3 install numpy

COPY data2.csv  /

COPY  basic.py  /

CMD python3 basic.py
