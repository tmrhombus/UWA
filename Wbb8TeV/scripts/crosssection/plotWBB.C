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
                    "#sigma(W(l#nu)+b#bar{b}) [pb]",
                    -0.2, 1., 506, ""
                    );

      lep.addEntry( "MCFM (x Hadronization)", 
		    0.51, 0.02,0.06, "PDF+Had","DPI",
		    20,1.5,kBlack,ndigit ); 
      lep.addData( "",
                   0.66,
                   0.03,0.14,0.07,0.02,
                   20,1.5,kBlack,ndigit );

      //lep.addEntry( "MG+Py6 5F",
      lep.addEntry( "MadGraph5 + Pythia6 5F",
		    0.51,0.03,0,"PDF","DPI",
		    20,1.5,kBlack,2 );
      lep.addData( "",
                   0.66,0.03,0.14,0.07,0.02,
                   20,1.5,kBlack,ndigit );

      lep.addEntry( "MadGraph5 + Pythia6 4F",
		    0.49, 0.02,0.06,"PDF","DPI",	
                    20,1.5,kBlack,ndigit );
      lep.addData( "",
                   0.66,0.03,0.14,0.07,0.02,
                   20,1.5,kBlack,ndigit );

      lep.addEntry( "MadGraph5 + Pythia8 4F",
                    0.50,0.03, 0.06, "PDF","DPI",
                    20,1.5,kBlack,ndigit );
      lep.addData( "",
                   0.66,0.03,0.14,0.07,0.02,
                   20,1.5,kBlack,ndigit );



      lep._y0   = 5.;
      lep._eps2 = 0.2;
      lep._upDy = 1.5;
      lep._dy = 0.3;


                          //  xc      stat    syst    theo    lumi
      lep.setCMSMeasurement2( 0.6425, 0.0299, 0.1017, 0.0646, 0.0167, "CMS");

      lep.addColorLegend2("Total uncertainty","DPI uncertainty","PDF uncertainty");
//      lep._txtLeft  = "Work In Progress";
      //lep._txtLeft  = "CMS Preliminary";
      lep._txtLeft  = "CMS";
      lep._intLumi = 0;
      lep._txtRight = "19.8 fb^{-1} (8 TeV)";
      //lep._txtRight = "20 fb^{-1} at #sqrt{s} = 8 TeV";
      lep.draw();
      lep.print();

}
