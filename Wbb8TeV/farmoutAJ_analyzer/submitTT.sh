#!/bin/bash

mkdir -p SubmitRecords
nohup bash fajSubmit_analyzerTTbarProgression.sh >> ./SubmitRecords/submitTT_${version}_${runname}.out 2>&1&

tail -f ./SubmitRecords/submitTT_${version}_${runname}.out
