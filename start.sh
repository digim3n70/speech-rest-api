#!/bin/bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/dwemer/speech-rest-api/python/lib/python3.11/site-packages/nvidia/cudnn/lib

cd /home/dwemer/speech-rest-api
source /home/dwemer/speech-rest-api/python/bin/activate

export PORT=3000
export LD_LIBRARY_PATH=/home/dwemer/speech-rest-api/python/lib/python3.11/site-packages/nvidia/cudnn/lib:$LD_LIBRARY_PATH

# Run the REST API
python custom_app.py &>log.txt&


