#!/bin/bash

mkdir -p SubmitRecords
nohup bash fajSubmit_analyzerJetVeto.sh >> ./SubmitRecords/submitJetVeto_${version}_${runname}.out 2>&1&

tail -f ./SubmitRecords/submitJetVeto_${version}_${runname}.out
