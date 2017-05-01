//========================================================================
// Input values:
// ============

//Prefit values:
double prefitYield=1318.5; 
double prefitYieldElectrons=1117.0;

//Fit results:
double RFACTOR=1.2728;
double ERROR_RFACTOR=0.242;
double OBSERVED=1726.9;

double RFACTORELECTRONS=1.3779;
double ERROR_RFACTORELECTRONS=0.300;
double OBSERVEDELECTRONS=1567.8;

double RFACTORCOMB=1.3525;
double ERROR_RFACTORCOMB=0.225;
double RFACTORCOMBTRIESTE=1.40;
double ERROR_RFACTORCOMBTRIESTE=0.203;


// Fiducial cross section:
double crosssection_4F_nofwd=0.50, error_4F_nofwd=0.001;
double xc_5F_th=0.51, err_xc_5F_th=0.01;

void xc_calc(){

        double obsXsec=0, errExpXsec=0, errTheoXsec=0;
        printf("Muons\n=============================\n");
        //printf(" xc = %.4f +- %.4f (stat) +- %.4f (syst) +- %.4f (theo) " )



        computeXsec(
         xc_5F_th,err_xc_5F_th,
         prefitYield,
         RFACTOR*prefitYield,
         ERROR_RFACTOR*prefitYield,
         obsXsec,
         errExpXsec,
         errTheoXsec, 
         OBSERVED);


        printf("Electrons\n=============================\n");
          computeXsec(xc_5F_th,err_xc_5F_th,prefitYieldElectrons,RFACTORELECTRONS*prefitYieldElectrons,ERROR_RFACTORELECTRONS*prefitYieldElectrons,obsXsec,errExpXsec,errTheoXsec, OBSERVEDELECTRONS);


        printf("Combined\n=============================\n");
	   cout<<xc_5F_th*RFACTORCOMB<<"  +-   "<<xc_5F_th*ERROR_RFACTORCOMB<<"    "<<xc_5F_th*RFACTORCOMB*sqrt(0.1*0.1+0.01*0.01)<<"(theo) pb "<<endl;



}


void computeXsec(
//inputs:
double xsecTheo, double errorStatTheo, double detectorlevelYield, double observed, double error_observed,
//outputs:
double& observedCrossSection, double& expErrorObservedCrossSection, double& theoErrorObservedCrossSection,
//checks:
double observed_postfit
)
{

// Detector level *expected* yield (per pb-1)
double detector=detectorlevelYield/19800;   double error_detector=0;//40./19800;

// Aceptance 
double acceptance=detector/xsecTheo; 
double erroracceptance=acceptance*sqrt( (errorStatTheo/xsecTheo)*(errorStatTheo/xsecTheo) + (error_detector/detector)*(error_detector/detector));

//double observed=detectorlevelYield*RFactor; 
//double error_observed=observed*sqrt( (40./detectorlevelYield*40./detectorlevelYield)+(errorRFactor/RFactor)*(errorRFactor/RFactor));

//checks
double check=observed_postfit/observed;

// Observed Cross Section
double observed_xsec=observed/acceptance/19800;

double err_observed_xsec_exp=observed_xsec*error_observed/observed;  // Experimental (from fit, includes stats)
double err_observed_xsec_statacc=observed_xsec*erroracceptance/acceptance; // Acceptance Statistical error 
double err_observed_xsec_theoPDF=observed_xsec*0.01;  // PDF uncertainty, based on 7TeV
double err_observed_xsec_theoScale=observed_xsec*0.1; // Scale uncertainy, based on 7TeV
double err_observed_xsec_theo=sqrt(err_observed_xsec_theoPDF*err_observed_xsec_theoPDF+err_observed_xsec_theoScale*err_observed_xsec_theoScale);//+err_observed_xsec_statacc*err_observed_xsec_statacc);

// Observed Cross Section Check
double observed_xsec_check=observed_postfit/(acceptance*check)/19800;
double observed_xsec_check_2=observed_postfit/(acceptance)/19800;


// Logs
cout<<"=============================="<<endl;
cout<<"INPUTS: "<<endl;
cout<<"Prefit yield:"<<detectorlevelYield<<"    Observed yield postfit: "<<observed_postfit<<endl;
cout<<"Signal strength:"<<observed/detectorlevelYield<<"  Ratio yields pre/postfit: "<<observed_postfit/detectorlevelYield<<endl;
cout<<"=============================="<<endl;
cout<<"Theoretical Xsec: "<<xsecTheo<<"+-"<<errorStatTheo<<"pb (stat only error)"<<endl;
cout<<"Acceptance (uncorrected): "<<acceptance<<"+-"<<erroracceptance<<"% (stat only error)"<<endl;
cout<<"=============================="<<endl;
cout<<"Changes in the acceptance from the fit"<<endl;
cout<<"Obs yield from fit: "<<observed_postfit<<endl;
cout<<"Observed yield from signalStrength*prefit: "<<observed<<" +- "<<error_observed<<endl;
cout<<"  change wrt signalStrength*prefit ------>     "<<check<<endl;
cout<<"Acceptance (corrected): "<<acceptance*check<<endl;
cout<<"=============================="<<endl;
cout<<"Observed Cross Section: "<<observed_xsec<<"  (exp: "<<err_observed_xsec_exp<<"   theo: "<<err_observed_xsec_theo<<") pb"<<endl;
//cout<<"(And check: a) change in the efficiency not related to xsec "<<observed_xsec_check<<" vs b) all change in obs coming from xsec "<<observed_xsec_check_2<<")"<<endl;
cout<<"=============================="<<endl;


observedCrossSection=observed_xsec;
expErrorObservedCrossSection=err_observed_xsec_exp;
theoErrorObservedCrossSection=err_observed_xsec_theo;


}

