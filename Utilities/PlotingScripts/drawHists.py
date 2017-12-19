# coding: utf-8
import ROOT
import sys
sys.path.append('/afs/cern.ch/user/k/kelong/work/WZConfigPlotting/Utilities')
import plot_functions as plotter
import argparse 
import array

parser = argparse.ArgumentParser()

ROOT.gROOT.SetBatch(True)
mgfile = ROOT.TFile("MGPartonPlots-nobquarks-ptj30_wponly_rebin.root")
mgofffile = ROOT.TFile("MGPartonPlots-ptj30_wponly.root")
vbfnlofile = ROOT.TFile("VBFNLO-fromauthors-ptj30_wponly_rebin.root")
#vbfnlofile = ROOT.TFile("VBFNLO-fromauthors-PartonPlots-ptj30.root")
for i in vbfnlofile.GetListOfKeys():
    mg_hist = mgfile.Get(i.GetName())
    #mgoff_hist = mgofffile.Get(i.GetName())
    vbfnlo_hist = vbfnlofile.Get(i.GetName())
    vbfnlo_hist.SetLineColor(ROOT.kRed)

    #mgoff_hist.Sumw2()
    mg_hist.Sumw2()
    vbfnlo_hist.Sumw2()

    mg_hist.Scale(0.001826*1000/100000)
    mg_hist.SetLineColor(ROOT.kBlue)
    #mgoff_hist.Scale(0.01763*1000/450045)
    vbfnlo_hist.Scale(1.0026/42508)
    mg_hist.GetXaxis().SetTitle(i.GetTitle())
    mg_hist.GetYaxis().SetTitle("d#sigma (fb)")

    hist_stack = ROOT.THStack("stack", "stack")
    hist_stack.Add(mg_hist)
    #hist_stack.Add(mgoff_hist)
    hist_stack.Add(vbfnlo_hist)
    if "mqq" in i.GetName():
        recola_name = "histogram_invariant_mass_mjj12_born_alpha6"
        recolaFileName = "RecolaHists/%s.root" % recola_name
        recolaFile = ROOT.TFile(recolaFileName)
        recola_hist = recolaFile.Get("canvas").GetListOfPrimitives().FindObject(recola_name)
        #xbins = array.array('d', range(0,3100,100))
        #rebinned_recola_hist = recola_hist.Rebin(len(xbins)-1, recola_hist.GetName()+"_rebin", xbins)
        #rebinned_recola_hist = recola_hist.Rebin(5, recola_hist.GetName()+"_rebin")
        recola_hist.Scale(40)

        recola_hist.Rebin(2)
        vbfnlo_hist.Rebin(2)
        mg_hist.Rebin(2)

        recola_hist.SetLineColor(ROOT.kGreen+3)
        hist_stack.Add(recola_hist)

    canvas = ROOT.TCanvas("canvas_"+mg_hist.GetName())
    hist_stack.Draw("nostack hist")
    hist_stack.SetMinimum(0.0001)

    if "mqq" in i.GetName():
        hist_stack.GetHistogram().GetXaxis().SetRangeUser(20, 4060)
        canvas.Update()
    hist_stack.GetYaxis().SetTitleOffset(1.2)    
    hist_stack.GetYaxis().SetTitle("d#sigma (fb)")

    legend = ROOT.TLegend(0.65, 0.7, 0.9, 0.9)
    #legend.AddEntry(mgoff_hist, "MG5_aMC LO 4F", "lp")
    legend.AddEntry(mg_hist, "#splitline{MG5_aMC LO 4F}{no b quarks}", "lp")
    legend.AddEntry(vbfnlo_hist, "VBFNLO LO", "lp")

    canvas = plotter.splitCanvas(canvas, [800, 800], "ratio to MG", [0.4, 1.6])
    ratioPad = canvas.GetListOfPrimitives().FindObject("ratioPad")
    first_hist = ratioPad.GetListOfPrimitives().FindObject(canvas.GetName()+"_central_ratioHist")
    canvas.Update()
    
    first_hist.GetYaxis().SetTitleOffset(0.5)
    if "mqq" in i.GetName():
        first_hist.GetXaxis().SetRangeUser(20,4060)
        legend.AddEntry(recola_hist, "MoCaNLO+Recola", "lp")

    legend.SetFillStyle(0)
    legend.Draw()

    #if vbfnlo_hist.GetMaximum() > mgoff_hist.GetMaximum():
    #    mgoff_hist.SetMaximum(vbfnlo_hist.GetMaximum())
    #mgoff_hist.SetMaximum(mgoff_hist.GetMaximum()*1.1)
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/Dec2017/%s.png" % i.GetName())
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/Dec2017/%s.pdf" % i.GetName())
    del canvas
    break
print "MadGraph"
print "    Initial: 17.63 pb"
#print "    Fiducial: %f fb" % mgoff_hist.Integral(0, mgoff_hist.GetNbinsX()+1)
print "MadGraph (no bs)"
print "    Initial: 1.826 pb"
print "    Fiducial: %f fb" % mg_hist.Integral(0, mg_hist.GetNbinsX()+1)
print "VBFNLO fiducial"
print "    Initial: 1.0026 pb"
print "    Fiducial: %f fb" % vbfnlo_hist.Integral(0, vbfnlo_hist.GetNbinsX()+1)
