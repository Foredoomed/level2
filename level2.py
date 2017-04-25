import easyquotation
import json
import sys, getopt

sn = sys.argv[1]
q = easyquotation.use('lf') # ['leverfun', 'lf']
#print(quotation.real('300494'))
d = q.real(sn)
s = d[sn]
print ("卖1: [" + str(s["ask1"]) + ", " + str(s["ask1_volume"]/100) + "]" )
print ("卖2: [" + str(s["ask2"]) + ", " + str(s["ask2_volume"]/100) + "]" )
print ("卖3: [" + str(s["ask3"]) + ", " + str(s["ask3_volume"]/100) + "]" )
print ("卖4: [" + str(s["ask4"]) + ", " + str(s["ask4_volume"]/100) + "]" )
print ("卖5: [" + str(s["ask5"]) + ", " + str(s["ask5_volume"]/100) + "]" )
print ("卖6: [" + str(s["ask6"]) + ", " + str(s["ask6_volume"]/100) + "]" )
print ("卖7: [" + str(s["ask7"]) + ", " + str(s["ask7_volume"]/100) + "]" )
print ("卖8: [" + str(s["ask8"]) + ", " + str(s["ask8_volume"]/100) + "]" )
print ("卖9: [" + str(s["ask9"]) + ", " + str(s["ask9_volume"]/100) + "]" )
print ("卖10: [" + str(s["ask10"]) + ", " + str(s["ask10_volume"]/100) + "]" )

print ("买1: [" + str(s["bid1"]) + ", " + str(s["bid1_volume"]/100) + "]" )
print ("买2: [" + str(s["bid2"]) + ", " + str(s["bid2_volume"]/100) + "]" )
print ("买3: [" + str(s["bid3"]) + ", " + str(s["bid3_volume"]/100) + "]" )
print ("买4: [" + str(s["bid4"]) + ", " + str(s["bid4_volume"]/100) + "]" )
print ("买5: [" + str(s["bid5"]) + ", " + str(s["bid5_volume"]/100) + "]" )
print ("买6: [" + str(s["bid6"]) + ", " + str(s["bid6_volume"]/100) + "]" )
print ("买7: [" + str(s["bid7"]) + ", " + str(s["bid7_volume"]/100) + "]" )
print ("买8: [" + str(s["bid8"]) + ", " + str(s["bid8_volume"]/100) + "]" )
print ("买9: [" + str(s["bid9"]) + ", " + str(s["bid9_volume"]/100) + "]" )
print ("买10: [" + str(s["bid10"]) + ", " + str(s["bid10_volume"]/100) + "]" )


print ("总卖: " + str((s["ask1_volume"]+s["ask2_volume"]+s["ask3_volume"]+s["ask4_volume"]+s["ask5_volume"]+s["ask6_volume"]+s["ask7_volume"]+s["ask8_volume"]+s["ask9_volume"]+s["ask10_volume"]) / 100 ))
print ("总买: " + str((s["bid1_volume"]+s["bid2_volume"]+s["bid3_volume"]+s["bid4_volume"]+s["bid5_volume"]+s["bid6_volume"]+s["bid7_volume"]+s["bid8_volume"]+s["bid9_volume"]+s["bid10_volume"])/ 100 ))