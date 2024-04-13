# setup venv
python3.8 -m venv venv
source ./venv/bin/activate
python3.8 -m pip install --upgrade pip # just to be safe

# install requirements
python3 -m pip install -r ./requirements.txt # install local requirements

deactivate