#!/bin/bash

file_name=motor_current_samples.pkl
file_google_drive_id=1hXXCtdgaoZqi_lKJ025RIzAljEcgosq

curl -L -o data/$file_name \
     "https://docs.google.com/uc?export=download&id=${file_google_drive_id}"