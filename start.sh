#!/bin/bash
ulimit -Sn `ulimit -Hn` # ROCm is a bitch
source ./venv/bin/activate
python3 ./main.py "$@"
deactivate