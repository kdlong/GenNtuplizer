# coding: utf-8
import ROOT
import sys
sys.path.append('/afs/cern.ch/user/k/kelong/work/WZConfigPlotting/Utilities')
import plot_functions as plotter
import argparse 

parser = argparse.ArgumentParser()

mgfile = ROOT.TFile("MGPartonPlots.root")
mgofffile = ROOT.TFile("MGPartonPlots-OfficialSample.root")
#vbfnlofile = ROOT.TFile("VBFNLOplots.root")
vbfnlofile = ROOT.TFile("VBFNLO-fromauthors-PartonPlots.root")
for i in vbfnlofile.GetListOfKeys():
    mg_hist = mgfile.Get(i.GetName())
    mgoff_hist = mgofffile.Get(i.GetName())
    vbfnlo_hist = vbfnlofile.Get(i.GetName())
    vbfnlo_hist.SetLineColor(ROOT.kRed)

    mgoff_hist.Sumw2()
    mg_hist.Sumw2()
    vbfnlo_hist.Sumw2()

    mg_hist.Scale(0.001826*1000/100000)
    mg_hist.SetLineColor(ROOT.kBlue)
    mgoff_hist.Scale(0.01763*1000/450045)
    #vbfnlo_hist.Scale(0.00068*1000/50000)
    vbfnlo_hist.Scale(1.0026/42508)

    mgoff_hist.GetXaxis().SetTitle(i.GetTitle())
    mgoff_hist.GetYaxis().SetTitle("d#sigma (fb)")

    hist_stack = ROOT.THStack("stack", "stack")
    hist_stack.Add(mgoff_hist)
    hist_stack.Add(mg_hist)
    hist_stack.Add(vbfnlo_hist)
    canvas = ROOT.TCanvas("canvas_"+mgoff_hist.GetName())
    hist_stack.Draw("nostack hist")
    hist_stack.GetYaxis().SetTitleOffset(1.2)    
    hist_stack.GetYaxis().SetTitle("d#sigma (fb)")

    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(mgoff_hist, "MG5_aMC LO 4F", "lp")
    legend.AddEntry(mg_hist, "#splitline{MG5_aMC LO 4F}{no b quarks}", "lp")
    legend.AddEntry(vbfnlo_hist, "#splitline{VBFNLO LO}{from Michael}", "lp")
    legend.SetFillStyle(0)
    legend.Draw()

    canvas = plotter.splitCanvas(canvas, "ratio to MG", [0.4, 1.6])
    if vbfnlo_hist.GetMaximum() > mgoff_hist.GetMaximum():
        mgoff_hist.SetMaximum(vbfnlo_hist.GetMaximum())
    mgoff_hist.SetMaximum(mgoff_hist.GetMaximum()*1.1)
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/Jul2017Update/%s.png" % i.GetName())
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/Jul2017Update/%s.pdf" % i.GetName())
    del canvas
