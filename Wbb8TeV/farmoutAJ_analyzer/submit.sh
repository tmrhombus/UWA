#!/bin/bash

mkdir -p SubmitRecords
nohup bash fajSubmit_analyzer.sh >> ./SubmitRecords/submit_${version}_${runname}.out 2>&1&

tail -f ./SubmitRecords/submit_${version}_${runname}.out
