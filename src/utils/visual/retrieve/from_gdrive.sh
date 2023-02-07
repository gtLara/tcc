#!/bin/bash

figure_name=stationarity_examples.png
figure_google_drive_id=1Kn_KMYytpqFp_2w8wTRtu-TnMms56rQi

curl -L -o figures/$figure_name "https://docs.google.com/uc?export=download&id=${figure_google_drive_id}"
