import sys
import json
import os
key=sys.argv[1]
val=input()
cfgpath=os.path.expanduser('~')+"/.config/lighthouse/beacon.conf"
if not os.path.isfile(cfgpath):
    f=open(cfgpath,"w")
    f.write("{}")
    f.close()
f=open(cfgpath,"r")
cfgraw=f.read()
f.close()
cfg=json.loads(cfgraw)
cfg[key]=val
#print (cfg)
f=open(cfgpath,"w")
f.write(json.dumps(cfg))
f.close()
