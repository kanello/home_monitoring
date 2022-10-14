#!/bin/bash

docker run -it -v $(pwd)/database:/app/database --name home_monitor home /bin/bash

# fyi the docker container time will be UTC