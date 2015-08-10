

callFindMTresolution()
{
 int error = 0;

 gROOT->ProcessLine(".L findMTresolution.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING findMTresolution.C"<<std::endl;}
 findMTresolution f;

// TChain *theChain    = new TChain("muonEventTree/eventTree");
// TChain *theChain    = new TChain("electronEventTree/eventTree");
 TChain *theChain        = new TChain("muEleEventTree/eventTree");

 TString path="./test/";

 TString outfileName = path+"res_mt_Wbb4F_tight_matched_firstNu.root" ;
 TString infileName = "/hdfs/store/user/tperry/Schweincomp_gen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root" ;


  std::cout << "Output File Name: " << outfileName << std::endl;
  //std::cout << "Input File Name: "  << infileName <<  std::endl;
 
  theChain->Reset();

  //TProof::Open("workers=8");

 // theChain->Add( infileName );
  theChain->Add("/hdfs/store/user/tperry/Schweincomp_gen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-*.root");

  //theChain->SetProof();

 
  f.Init(theChain); 
    
//  theChain.
//
//chain->Process("selector","args");

  f.Loop( outfileName ); 

} // void callFindMTresolution()


