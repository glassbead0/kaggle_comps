#!/bin/bash

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' > /kaggle/log/jupyter.log 2>&1 &

tail -f /dev/null