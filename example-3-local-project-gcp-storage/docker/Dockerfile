FROM jupyter/base-notebook:latest

COPY requirements.txt /tmp/requirements.txt
RUN pip install --ignore-installed -r /tmp/requirements.txt

# enable the JupyterLab extensions
RUN jupyter labextension install @jupyterlab/toc
RUN jupyter labextension install @aquirdturtle/collapsible_headings

USER root

RUN apt-get update && apt-get install -y curl

USER jovyan

WORKDIR /home/mlpanel-example-3

CMD jupyter lab --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token=''