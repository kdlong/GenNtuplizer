# coding: utf-8

import ROOT
chain = ROOT.TChain("analyzeWZ/Ntuple")
chain.Add("WZTo2Mu1E1Nu_fixedscale_powheg_pythia8_Ntuple_leptonType-dressed.root", 5000)

#var = "Z1mass"
#cut = "Z1mass < 111 && Z1mass > 81"
var = "Mass"
label = "M_{3l} [GeV]"
cut = ""

chain.Draw(var+":LHEweights[1]", cut, "goff")
graph1 = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2());

chain.Draw(var+":LHEweights[2]/LHEweights[0]", cut, "goff")
graph2 = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

chain.Draw(var+":LHEweights[3]/LHEweights[0]", cut, "goff")
graph3 = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

chain.Draw(var+":LHEweights[4]/LHEweights[0]", cut, "goff")
graph4 = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

chain.Draw(var+":LHEweights[6]/LHEweights[0]", cut, "goff")
graph6 = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

chain.Draw(var+":LHEweights[8]/LHEweights[0]", cut, "goff")
graph8 = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

chain.Draw(var+":maxScaleWeight", cut, "goff")
maxGraph = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

chain.Draw(var+":minScaleWeight", cut, "goff")
minGraph = ROOT.TGraph(5000, chain.GetV1(),chain.GetV2())

graph1.SetMarkerSize(.25)
graph2.SetMarkerSize(.25)
graph3.SetMarkerSize(.25)
graph4.SetMarkerSize(.25)
graph6.SetMarkerSize(.25)
graph8.SetMarkerSize(.25)
maxGraph.SetMarkerSize(1)
minGraph.SetMarkerSize(1)

graph2.SetMarkerColorAlpha(ROOT.kRed, 0.75)
graph3.SetMarkerColorAlpha(ROOT.kViolet, 0.75)
graph4.SetMarkerColorAlpha(ROOT.kGreen, 0.75)
graph6.SetMarkerColorAlpha(ROOT.kOrange, 0.75)
graph8.SetMarkerColorAlpha(ROOT.kBlue, 0.75)
maxGraph.SetMarkerColorAlpha(ROOT.kPink, 0.25)
minGraph.SetMarkerColorAlpha(ROOT.kPink, 0.25)

canvas = ROOT.TCanvas()

maxGraph.SetMinimum(0)
maxGraph.Draw("AP")
maxGraph.GetXaxis().SetTitle(label)
maxGraph.GetYaxis().SetTitle("weight")
graph1.Draw("P same")
graph2.Draw("P same")
graph3.Draw("P same")
graph4.Draw("P same")
graph6.Draw("P same")
graph8.Draw("P same")
minGraph.Draw("P same")

graph1clone = graph1.Clone()
graph1clone.SetMarkerSize(1)
graph2clone = graph2.Clone()
graph2clone.SetMarkerSize(1)
graph3clone = graph3.Clone()
graph3clone.SetMarkerSize(1)
graph4clone = graph4.Clone()
graph4clone.SetMarkerSize(1)
graph6clone = graph6.Clone()
graph6clone.SetMarkerSize(1)
graph8clone = graph8.Clone()
graph8clone.SetMarkerSize(1)

legend = ROOT.TLegend(0.6, 0.5, 0.9, 0.9)
legend.AddEntry(graph1clone, "#mu_{F}=1 #mu_{R}= 2", "p")
legend.AddEntry(graph2clone, "#mu_{F}=1 #mu_{R}= 1/2", "p")
legend.AddEntry(graph3clone, "#mu_{F}=2 #mu_{R}= 1", "p")
legend.AddEntry(graph4clone, "#mu_{F}=2 #mu_{R}= 2", "p")
legend.AddEntry(graph6clone, "#mu_{F}=1/2 #mu_{R}= 1", "p")
legend.AddEntry(graph8clone, "#mu_{F}=1/2 #mu_{R}= 1/2", "p")
legend.AddEntry(maxGraph, "Max (min) weight", "p")
legend.Draw()
canvas.Print("~/www/weightvMass.png")
