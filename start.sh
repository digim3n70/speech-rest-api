#!/bin/bash

cd /home/dwemer/speech-rest-api
source /home/dwemer/speech-rest-api/python/bin/activate

export PORT=3000

# Run the REST API
python custom_app.py &>log.txt&


