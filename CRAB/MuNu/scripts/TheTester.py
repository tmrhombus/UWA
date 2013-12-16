'''
Tests if all the variable names are valid
'''

import histoRange as hr 
import TheParameters as p
import TheCuts as ct

lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,eventTreeLocation,extraCut = p.arams() 

CutsMCn, CutsMCnW, CutsMCi,CutsDatan,CutsDatai,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb,CutsMCnT,CutsMCiT,CutsMCnTup,CutsMCiTup,CutsMCnTdn,CutsMCiTdn = ct.cutmaker(
 iso_value,antiIso_value,lumi,bNr,btype,jNr,njetcut,jetcut,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,extraCut
)

print("Data Cuts: \n %s\n"%(CutsDatai))
print("MC Cuts: \n %s\n"%(CutsMCi))

for leaf in leafs:
 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
 print(leaf)
 print('%s %s'%(xtitle,xunits))
 print('%s(%s,%s)'%(steps,xmin,xmax))
 print('Log Scale: %s'%setLogY)
 print('')
