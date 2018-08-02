# coding: utf-8
import ROOT
import sys
sys.path.append('/afs/cern.ch/user/k/kelong/work/WZConfigPlotting/Utilities')
import plot_functions as plotter
import argparse 
import array

parser = argparse.ArgumentParser()

ROOT.gROOT.SetBatch(True)
chan = "wp"
chan_label = "WmZ" if chan == "wm" else "WpZ"
mgofffile = ROOT.TFile("MGHists/MGPartonPlots-ptj30_%sonly.root" % chan)
#mgofffile = ROOT.TFile("MGHists/MGPartonPlots-mathieusSetup_AllCuts_wmonly.root" )
sumweights_mgoff = mgofffile.Get("sumweights").Integral()
print "Sumweights is ", sumweights_mgoff

mg14TeVfile = ROOT.TFile("%sJJ_14TeV_fromDylan_%sonly.root" % (chan_label, chan))
print mg14TeVfile
sumweights_mg14TeV = mg14TeVfile.Get("sumweights").Integral()
print "Sumweights at 14 TeV is ", sumweights_mg14TeV

for i in mgofffile.GetListOfKeys():
    if i.GetName() == "sumweights":
        continue
    hist_stack = ROOT.THStack("stack", "stack")
    mg_hist = mgofffile.Get(i.GetName())
    mg14TeV_hist = mg14TeVfile.Get(i.GetName())
    mg_hist.Sumw2()
    mg14TeV_hist.Sumw2()
    mg_hist.Scale(0.01763*1000/sumweights_mgoff)
    #mg_hist.Scale(0.163769733993/sumweights_mgoff)
    first_hist = mg_hist

    mg_hist.SetLineColor(ROOT.TColor.GetColor("#e41a1c"))
    mg_hist.SetLineWidth(2)
    mg14TeV_hist.Scale(6.97/sumweights_mg14TeV)
    first_hist.GetXaxis().SetTitle(i.GetTitle() + (" [GeV]" if "eta" not in i.GetTitle() else ""))
    first_hist.GetYaxis().SetTitle("d#sigma (fb)")

    hist_stack.Add(mg_hist)
    hist_stack.Add(mg14TeV_hist)

    canvas = ROOT.TCanvas("canvas_"+mg_hist.GetName())
    hist_stack.Draw("nostack hist")
    hist_stack.SetMinimum(0.0001)

    hist_stack.GetYaxis().SetTitleOffset(1.25)    
    hist_stack.GetYaxis().SetTitle("#sigma [fb] / bin")

    nentries = len(hist_stack.GetHists())
    legend = ROOT.TLegend(0.55, 0.93-0.065*nentries, 0.9, 0.93)

    legend.AddEntry(mg_hist, "#splitline{MG5_aMC@NLO 13 TeV}{#scale[0.8]{from SMP-18-001}}", "l")
    legend.AddEntry(mg14TeV_hist, "#splitline{MG5_aMC@NLO 14 TeV}{#scale[0.8]{from Dylan}}", "l")

    canvas = plotter.splitCanvas(canvas, [800, 800], "#scale[0.85]{ratio to M+R}", [0.85, 1.15])
    ratioPad = canvas.GetListOfPrimitives().FindObject("ratioPad")
    first_hist = ratioPad.GetListOfPrimitives().FindObject(canvas.GetName()+"_central_ratioHist")
    first_hist.GetYaxis().SetTitleOffset(0.5)
    first_hist.GetYaxis().SetLabelFont(42)
    first_hist.GetXaxis().SetLabelFont(42)
    
    if "mqq" in i.GetName():
        first_hist.GetXaxis().SetRangeUser(500,4060)

    legend.SetFillStyle(0)
    legend.Draw()
    ROOT.dotrootImport('kdlong/CMSPlotDecorations')
    canvas.Update()

    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/Compare13and14TeV/%s/plots/%s.png" % (chan_label, i.GetName()))
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/Compare13and14TeV/%s/plots/%s.pdf" % (chan_label, i.GetName()))
    del canvas
print "MadGraph 13 TeV"
print "    Initial: 17.63 pb"
print "    Fiducial: %f fb" % mg_hist.Integral(0, mg_hist.GetNbinsX()+1)
print "MadGraph 14 Tev"
print "    Initial:  6.97 fb" 
print "    Fiducial: %f fb" % mg14TeV_hist.Integral(0, mg14TeV_hist.GetNbinsX()+1)
