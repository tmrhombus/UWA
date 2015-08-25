#!/bin/bash

mkdir -p SubmitRecords
nohup bash fajSubmit_analyzerDrell.sh >> ./SubmitRecords/submitDrell_${version}_${runname}.out 2>&1&

tail -f ./SubmitRecords/submitDrell_${version}_${runname}.out
