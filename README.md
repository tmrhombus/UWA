UWAnalysis
==========
UW Analysis for 53x (8Tev)


download this using the recipe below:

```bash
scram pro -n MyWorkingAreaName CMSSW CMSSW_5_3_9
cd MyWorkingAreaName/src/

cmsenv
```
set up cvs - something like this
```bash
export CVSROOT=:gserver:<user_name>@cmssw.cvs.cern.ch:/local/reps/CMSSW
kinit <user_name>@CERN.CH; aklog -cell cern.ch
```

Clone From GIT
```bash
git clone https://github.com/tmrhombus/UWAnalysis.git
```
Then you need to do a stupid hack: open JetMETCorrections/METPUSubtraction/src/PFMETAlgorithmMVA.cc and there are two sets of likes like

```
<<<<<<
abcd
=======
defg
>>>>>>>
```
do some deleting to make this just ``defg``.  Then run the recipe

```
./UWAnalysis/recipe/recipe.sh
```

check before compiling ``showtags`` should give 40 (fewer could mean cvs not up)

Compile
```bash
scramv1 build -c
scramv1 build
```

For future compiling, only run ``scramv1 build``

Some useful histograms are
```bash
cd $CMSSW_BASE/src/UWAnalysis/Configuration/data
scp /afs/cern.ch/user/a/agilbert/public/HTT_Pileup/12-06-13/MC_Summer12_PU_S10-600bins.root .
scp /afs/cern.ch/user/a/agilbert/public/HTT_Pileup/12-06-13/Data_Pileup_2012_ReReco-600bins.root .
cd $CMSSW_BASE/src/UWAnalysis/Crab/MuNu/weights
scp /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt .
```
