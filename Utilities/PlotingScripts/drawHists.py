# coding: utf-8
import ROOT
import sys
sys.path.append('/afs/cern.ch/user/k/kelong/work/WZConfigPlotting/Utilities')
import plot_functions as plotter
import argparse 
import array

parser = argparse.ArgumentParser()

ROOT.gROOT.SetBatch(True)
chan = "wm"
chan_label = "WmZ" if chan == "wm" else "WpZ"
#mgfile = ROOT.TFile("MGHists/MGPartonPlots-nobquarks-mathieusSetup_reduced_%sonly.root" % chan)
#mgfile = ROOT.TFile("MGHists/MGPartonPlots-mathieusSetup_tightCuts_%sonly.root" % chan)
mgfile = ROOT.TFile("MGHists/MGPartonPlots-mathieusSetup_AllCuts_%sonly.root" % chan)
#mgofffile = ROOT.TFile("MGHists/MGPartonPlots-ptj30_%sonly.root" % chan)
vbfnlofile = ROOT.TFile("VBFNLOHists/VBFNLO-fromauthors-ptj30_%sonly.root" % chan)
vbfnlofile_old = ROOT.TFile("VBFNLOHists/vbfnlo_fromMichael_Jul2017_%sonly.root" % chan)
sumweights_vbfnlo_old = vbfnlofile_old.Get("sumweights").Integral()
vbfnlo_old_xsec = 1.00203/2
#mg_xsec = 0.6802 if chan == "wm" else 0.3293
mg_xsec = 0.1664 if chan == "wm" else 0.3293
vbfnlo_xsec = 0.9589518 if chan == "wm" else 1.578255
sumweights_vbfnlo = vbfnlofile.Get("sumweights").Integral()
sumweights_mg = mgfile.Get("sumweights").Integral()
print "Smweights is ", sumweights_mg
#sumweights_mgoff = mgofffile.Get("sumweights").Integral()

for i in vbfnlofile.GetListOfKeys():
    if i.GetName() == "sumweights":
        continue
    hist_stack = ROOT.THStack("stack", "stack")
    mg_hist = mgfile.Get(i.GetName())
    mg_hist.Sumw2()
    mg_hist.Scale(mg_xsec/sumweights_mg)
    #mgoff_hist = mgofffile.Get(i.GetName())
    vbfnlo_hist = vbfnlofile.Get(i.GetName())
    recola_hist = 0
    sherpa_hist = 0
    first_hist = mg_hist

    if i.GetName() in ["hmqq", "hdeta"]:
        if "mqq" in i.GetName():
            recola_name = "histogram_invariant_mass_mjj12_born"
            recolaFileName = "RecolaHists/%s_FixedScale/%s.root" % (chan_label ,recola_name)
            recolaFile = ROOT.TFile(recolaFileName)
            recola_hist = recolaFile.Get("canvas").GetListOfPrimitives().FindObject(recola_name)
            #xbins = array.array('d', range(0,3100,100))
            #rebinned_recola_hist = recola_hist.Rebin(len(xbins)-1, recola_hist.GetName()+"_rebin", xbins)
            #rebinned_recola_hist = recola_hist.Rebin(5, recola_hist.GetName()+"_rebin")
            recola_hist.Scale(40)

            sherpa_file = ROOT.TFile("data/Sherpa_FO.root")
            sherpa_hist = sherpa_file.Get("WZVBS_LesHouchesStudy_FOshifted/mjj")
            sherpa_hist.Scale(1000)

            recola_hist.Rebin(4)
            sherpa_hist.Rebin(4)
            vbfnlo_hist.Rebin(4)
            #vbfnlo_hist_old.Rebin(4)
            mg_hist.Rebin(4)

            hist_stack.Add(recola_hist)
            hist_stack.Add(sherpa_hist)
        else:
            continue
        if "deta" in i.GetName() and chan == "wm":
            recola_name = "recola_etajj"
            recolaFileName = "RecolaHists/%s_FixedScale/%s.root" % (chan_label ,recola_name)
            recolaFile = ROOT.TFile(recolaFileName)
            recola_hist = recolaFile.Get(i.GetName())
            recola_hist.Scale(0.25)
            hist_stack.Add(recola_hist)

            sherpa_file = ROOT.TFile("data/Sherpa_FO_etajj.root")
            sherpa_hist = sherpa_file.Get("hdeta")
            sherpa_hist.Scale(1000)
            hist_stack.Add(sherpa_hist)
        first_hist = recola_hist
    else: 
        continue
    vbfnlo_hist.SetLineColor(ROOT.TColor.GetColor("#984ea3"))
    vbfnlo_hist.SetLineStyle(2)
    vbfnlo_hist.SetLineWidth(3)

    vbfnlo_hist_old = vbfnlofile_old.Get(i.GetName())
    vbfnlo_hist_old.SetLineColor(ROOT.kBlack)
    vbfnlo_hist_old.Sumw2()
    vbfnlo_hist_old.Scale(vbfnlo_old_xsec/sumweights_vbfnlo_old)
    #mgoff_hist.Sumw2()
    vbfnlo_hist.Sumw2()

    #mg_hist.Scale(0.001826*1000/100000)
    mg_hist.SetLineColor(ROOT.TColor.GetColor("#e41a1c"))
    mg_hist.SetLineWidth(2)
    #mgoff_hist.Scale(0.01763*1000/sumweights_mgoff)
    #vbfnlo_hist.Scale(1.0026/42508)
    vbfnlo_hist.Scale(vbfnlo_xsec/sumweights_vbfnlo)
    first_hist.GetXaxis().SetTitle(i.GetTitle() + (" [GeV]" if "eta" not in i.GetTitle() else ""))
    first_hist.GetYaxis().SetTitle("d#sigma (fb)")

    #hist_stack.Add(mgoff_hist)
    hist_stack.Add(vbfnlo_hist)
    hist_stack.Add(mg_hist)
    #hist_stack.Add(vbfnlo_hist_old)

    canvas = ROOT.TCanvas("canvas_"+mg_hist.GetName())
    hist_stack.Draw("nostack hist")
    hist_stack.SetMinimum(0.0001)

    if "mqq" in i.GetName():
        hist_stack.GetHistogram().GetXaxis().SetRangeUser(500, 4060)
        canvas.Update()
    hist_stack.GetYaxis().SetTitleOffset(1.25)    
    #hist_stack.GetHistogram().GetYaxis().SetTitleFont(42)    
    hist_stack.GetYaxis().SetTitle("#sigma [fb] / bin")

    nentries = len(hist_stack.GetHists())
    legend = ROOT.TLegend(0.55, 0.93-0.065*nentries, 0.95, 0.93)
    if sherpa_hist:
        sherpa_hist.SetLineColor(ROOT.TColor.GetColor("#3f4760"))
        sherpa_hist.SetLineStyle(3)
        sherpa_hist.SetLineWidth(3)
        legend.AddEntry(sherpa_hist, "Sherpa", "l")

    legend.AddEntry(vbfnlo_hist, "VBFNLO", "l")
        #legend.AddEntry(vbfnlo_hist_old, "#splitline{VBFNLO LO}{Default config}", "l")
    legend.AddEntry(mg_hist, "MG5_aMC@NLO", "l")

    if recola_hist:
        recola_hist.SetLineColor(ROOT.TColor.GetColor("#4daf4a"))
        #recola_hist.SetLineStyle(3)
        recola_hist.SetLineWidth(2)
        legend.AddEntry(recola_hist, "MoCaNLO+Recola", "l")

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

    #if vbfnlo_hist.GetMaximum() > mgoff_hist.GetMaximum():
    #    mgoff_hist.SetMaximum(vbfnlo_hist.GetMaximum())
    #mgoff_hist.SetMaximum(mgoff_hist.GetMaximum()*1.1)
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/2018Mar-Update/%s/plots/%s.png" % (chan_label, i.GetName()))
    canvas.Print("~/www/DibosonAnalysisData/PlottingResults/WZGenAnalysis/partonlevel/2018Mar-Update/%s/plots/%s.pdf" % (chan_label, i.GetName()))
    del canvas
print "MadGraph"
print "    Initial: 17.63 pb"
#print "    Fiducial: %f fb" % mgoff_hist.Integral(0, mgoff_hist.GetNbinsX()+1)
print "MadGraph (no bs)"
print "    Initial:  %f fb" % mg_xsec
print "    Fiducial: %f fb" % mg_hist.Integral(0, mg_hist.GetNbinsX()+1)
print "VBFNLO fiducial"
print "    Initial:  %f fb" % vbfnlo_xsec
print "    Fiducial: %f fb" % vbfnlo_hist.Integral(0, vbfnlo_hist.GetNbinsX()+1)
