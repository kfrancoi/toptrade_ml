FROM jupyter/scipy-notebook:7f1482f5a136

WORKDIR /home/jovyan

ADD requirements.txt /home/jovyan/requirements.txt

RUN pip install --upgrade pip
# RUN pip install --upgrade jupyterlab
# RUN pip install --upgrade jupyter_client
RUN pip install -r requirements.txt

RUN pip install --ignore-installed jupyterlab==3.0.1
