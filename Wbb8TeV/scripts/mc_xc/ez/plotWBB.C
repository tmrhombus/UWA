// Plots for theoretical comparison of the W+C measurement
// Maria Cepeda  

#include "tdrstyle.C"
#include "plottingLEPStyle.C"
void plotWBB()
{
  setTDRStyle();

  int ndigit(2);

  float size1 = 0.075;
  float size2 = 0.058;

      LEPStyle lep( "Results_WBB",
                    "#sigma(W+b#bar{b}) [pb]",
                    //"#sigma [pb]",
                    -0.2, 1., 506, ""
                    );

      lep.addEntry( "MCFM (x Hadronization)", 
		    0.51, 0.02,0.06, "PDF+Had","DPS",
		    20,1.5,kBlack,ndigit ); 
      lep.addEntry( "MG+Py6 5F",
		    0.51,0.03,0,"PDF","DPS",
		    21,1.5,kBlack,2 );

      lep.addEntry( "MG+Py6 4F",
		    0.49, 0.02,0.06,"PDF","DPS",	
                    22,1.5,kBlack,ndigit );


      lep.addEntry( "MG+Py8 4F",
                    0.50,0.03, 0.06, "PDF","DPS",
                    23,1.5,kBlack,ndigit );


      lep._y0   = 5.;
      lep._eps2 = 0.2;
      lep._upDy = 1.5;
      lep._dy = 0.3;


 
      lep.setCMSMeasurement2( 0.66,0.03,0.14,0.07,
				  "CMS 2012");

      lep.addColorLegend2("Total Uncertainty","Statistical Uncertainty","Experimental-Only Uncertainty");
//      lep._txtLeft  = "Work In Progress";
      //lep._txtLeft  = "CMS Preliminary";
      lep._txtLeft  = "CMS";
      lep._intLumi = 0;
      lep._txtRight = "19.8 fb^{-1} (8 TeV)";
      //lep._txtRight = "20 fb^{-1} at #sqrt{s} = 8 TeV";
      lep.draw();
      lep.print();

}
