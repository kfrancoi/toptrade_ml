#!/bin/bash
set -e

pip install -r /home/jovyan/requirements.txt

. /usr/local/bin/start.sh jupyter notebook $*
