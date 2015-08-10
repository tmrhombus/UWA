cut = 'C3'
andreas_events = [line.strip() for line in open('%s_and.txt'%(cut))]
jelenas_events = [line.strip() for line in open('%s_jel.txt'%(cut))]
toms_events    = [line.strip() for line in open('%s_tom.txt'%(cut))]

just_andrea = []
just_jelena = []
just_tom = []

t_noJ = []
t_noA = []
j_noT = []
j_noA = []
a_noT = []
a_noJ = []

t_j = []
a_t = []
j_a = []
t_j_a = []

for toms_event in toms_events:
 tj = False
 ta = False
 for jelenas_event in jelenas_events:
  if long(toms_event) == long(jelenas_event):
   tj = True
   break
 for andreas_event in andreas_events:
  if long(toms_event) == long(andreas_event): 
   ta = True
   break
 if tj == False and ta == False: just_tom.append(toms_event)
 if tj == False: t_noJ.append(toms_event)
 if ta == False: t_noA.append(toms_event)
 if tj == True  and ta == True:  t_j_a.append(toms_event)
 if tj == True: t_j.append(toms_event)
 if ta == True: a_t.append(toms_event)

for andreas_event in andreas_events:
 at = False
 aj = False
 for toms_event in toms_events:
  if long(andreas_event) == long(toms_event): 
   at = True
   break
 for jelenas_event in jelenas_events:
  if long(andreas_event) == long(jelenas_event):
   aj = True
   break
 if at == False and aj == False: just_andrea.append(andreas_event)
 if at == False: a_noT.append(andreas_event)
 if aj == False: a_noJ.append(andreas_event)
 if aj == True: j_a.append(andreas_event)

for jelenas_event in jelenas_events:
 ja = False
 jt = False
 for andreas_event in andreas_events:
  if long(andreas_event) == long(jelenas_event):
   ja = True
   break
 for toms_event in toms_events:
  if long(toms_event) == long(jelenas_event):
   jt = True
 if ja == False and jt == False: just_jelena.append(jelenas_event)
 if ja == False: j_noA.append(jelenas_event)
 if jt == False: j_noT.append(jelenas_event)

log = open('/afs/hep.wisc.edu/home/tperry/www/wbb/synch/2014ocbr03/%s_tt_comp_noleptonclean.log'%(cut),'w')
log.write("Andreas Events: %s\n"%len(andreas_events))
log.write("Jelenas Events: %s\n"%len(jelenas_events))
log.write("Toms Events:    %s\n"%len(toms_events ))
log.write("All Three:      %s\n\n"%len(t_j_a))

log.write(" Tom Has, Jelena Doesn't (%s)\n"%len(t_noJ))
for e in t_noJ: log.write(" "+e)
log.write("\n\n")
log.write(" Jelena Has, Tom Doesn't (%s)\n"%len(j_noT))
for e in j_noT: log.write("  "+e)
log.write("\n\n")

log.write("====================================================================\n\n")
log.write(" Tom Has, Andrea Doesn't (%s)\n"%len(t_noA))
for e in t_noA: log.write("  "+e)
log.write("\n\n")
log.write(" Andrea Has, Tom Doesn't (%s)\n"%len(a_noT))
for e in a_noT: log.write("  "+e)
log.write("\n\n")

log.write("====================================================================\n\n")
log.write(" Jelena Has, Andrea Doesn't (%s)\n"%len(j_noA))
for e in j_noA: log.write("  "+e)
log.write("\n\n")
log.write(" Andrea Has, Jelena Doesn't (%s)\n"%len(a_noJ))
for e in a_noJ: log.write("  "+e)
log.write("\n\n")

log.write("We All Have %s\n"%len(t_j_a))
for e in t_j_a: log.write(e+" ")
log.write("\n\n")

log.write("Tom Has %s\n"%len(toms_events))
for e in toms_events: log.write(e+" ")
log.write("\n\n")

log.write("Jelena Has %s\n"%len(jelenas_events))
for e in jelenas_events: log.write(e+" ")
log.write("\n\n")

log.write("Andreas Has %s\n"%len(andreas_events))
for e in andreas_events: log.write(e+" ")
log.write("\n\n")
