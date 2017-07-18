from DataFormats.FWLite import Handle, Events
import random
import json

#events = Events("root://cmsxrootd.fnal.gov///store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_aQGC-FM_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/027561E3-42BE-E611-AB10-001E674DA83D.root")
#sample = "fm"
events = Events("root://cmsxrootd.fnal.gov///store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_aQGC-FS_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/00AEA2AB-82C5-E611-9920-0CC47A706D40.root")
sample = "fs"
handle = Handle("LHEEventProduct")
colors = [
    "nofill-darkpurple",
    "nofill-lightpurple",
    "nofill-darkpurple-dash",
    "nofill-darkgreen",
    "nofill-lightgreen",
    "nofill-lightpink-dotdash",
    "nofill-darkgreen-dotdash",
    "nofill-darkgreen-finedash",
    "nofill-green-dotdash",
    "nofill-green-dash",
    "nofill-lightgreen-dotdash",
    "nofill-lightgreen-dash",
    "nofill-lightgreen-finedash",
    "nofill-darkgreen-dash",
    "nofill-yellow",
    "nofill-lightred",
    "nofill-lightred-dash",
    "nofill-darkred",
    "nofill-red-dash",
    "nofill-lightblue",
    "nofill-lightblue-dash",
    "nofill-darkblue",
    "nofill-darkblue-finedash",
    "nofill-orange",
    "nofill-grey",
    "nofill-lightgrey-dash",
]
weights = 0
for e in events:
    e.getByLabel("externalLHEProducer", handle)
    prod = handle.product()
    weights = prod.weights()
    break
    for i,weight in enumerate(prod.weights()):
        print "index %i, index - 8: %i, ID: %s" % (i, i-8, weight.id)
        print "Weight: %f" % weight.wgt
weight_names = {}
for i,weight in enumerate(weights):
    if sample not in weight.id and "standard_model" not in weight.id:
        continue
    if weight.id == "standard_model":
        name = "wzjj-aqgc%s__sm" % sample
        label = "SM (rw)" 
    else:
        name = "wzjj-aqgc%s__%s" % (sample, weight.id.replace("_","-").replace("--","_"))
        label = weight.id.replace("__", " ")
        label = label.replace("_", "= ")
        label = label.replace("fm0", "F_{M0}") 
        label = label.replace("fm1", "F_{M1}") 
        label = label.replace("ft0", "F_{T0}") 
        label = label.replace("ft1", "F_{T1}") 
        label = label.replace("ft2", "F_{T2}") 
        label = label.replace("fs0", "F_{S0}") 
        label = label.replace("fs1", "F_{S1}") 
        label = label.replace("m", "-")
        label += " TeV^{-4}"
        print "LABEL ", label
    weight_names.update({name : 
        { "Name" : label,
        "Style" : random.choice(colors),
        "add_perc_error" : 0.0,
        "weight" : "pdfWeights[%i]/scaleWeights[0]" % (i-9),
        "Members" : [
            "wzjj-aqgc%s" % sample
        ]}
    })

with open('data.json', 'w') as outfile:
    json.dump(weight_names, outfile,
        sort_keys = True, indent = 4,
         ensure_ascii=False)
