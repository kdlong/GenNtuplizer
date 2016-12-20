import ROOT
import math
tree_name="analyzeDY/Ntuple"
file_path="/data/kelong/DibosonAnalysisData/GenAnalysis/DY_MLL-50_mg5amcatnloFxFx_GenNtuples_leptonType-dressed_2016-11-13-dyGen_cfg/*"
weight="weight"
#tree_var="nj"
#bin_info=[10,0,10]
#xlabel="Number of p_{T} > 30 GeV Gen Jets [GeV]"
tree_var="ht"
bin_info=[100,0,1000]
xlabel="H_{T} [GeV]"
#tree_var="Zmass"
#bin_info=[50,50,150]
#xlabel="m_{Z} [GeV]"
#tree_var="ZPt"
#bin_info=[40,0,800]
#xlabel="p_{T}(Z) with n_{j} #geq 2 [GeV]"
#tree_var="j1Pt"
#bin_info=[50,0,800]
#xlabel="Leading Jet p_{T} [GeV]"
#tree_var="mjj"
#bin_info=[90,0,900]
#xlabel="Di-jet Mas [GeV]"

hist_name = tree_var+"_hist"
chain = ROOT.TChain(tree_name)
chain.Add(file_path)

canvas = ROOT.TCanvas("canvas", "canvas")
weighted_hist = ROOT.TH1D(hist_name, hist_name, *bin_info)
unweighted_hist = ROOT.TH1D(hist_name+"_unweighted", hist_name, *bin_info)

chain.Draw("{var}>>{hist}".format(
    var=tree_var,hist=hist_name), "{0}/abs({0})".format(weight))
chain.Draw("{var}>>{hist}".format(
    var=tree_var,hist=hist_name+"_unweighted"))
print "Effective entries weighted = %i" % weighted_hist.GetEffectiveEntries()
print "Weighted Integral = %i" % weighted_hist.Integral()
print "Effective entries unweighted = % i" % unweighted_hist.GetEffectiveEntries()
print "Unweighted Integral = %i" % unweighted_hist.Integral()

weighted_hist.Draw("")
unweighted_hist.SetLineColor(ROOT.kRed)
unweighted_hist.Draw("same")
canvas.Print("~/www/DYweightStudies/%s_weightedhist.pdf" % tree_var)

errors_hist_name = hist_name+"_errors"
errors_hist = ROOT.TH1F(errors_hist_name, errors_hist_name, *bin_info)
dreamerrors_hist = errors_hist.Clone()
dreamerrors_hist.SetName(dreamerrors_hist.GetName()+"_unweighted")
dreamerrors_hist.SetLineColor(ROOT.kRed)
negweights_hist  = errors_hist.Clone()
negweights_hist.SetName(hist_name+"_fneg")
negweights_hist.SetLineColor(ROOT.kBlue)

for i in xrange(0, weighted_hist.GetSize()):
    error = weighted_hist.GetBinError(i)/weighted_hist.GetBinContent(i) \
        if weighted_hist.GetBinContent(i) > 0 else 0
    errors_hist.SetBinContent(i, error)
    dreamerror = unweighted_hist.GetBinError(i)/unweighted_hist.GetBinContent(i) \
        if unweighted_hist.GetBinContent(i) > 0 else 0
    dreamerrors_hist.SetBinContent(i, dreamerror)
    fneg = ((unweighted_hist.GetBinContent(i) - weighted_hist.GetBinContent(i)) / \
           (unweighted_hist.GetBinContent(i)*2) ) if unweighted_hist.GetBinContent(i) > 0 \
                else 0
    negweights_hist.SetBinContent(i, fneg)
    print "For i = %i, Negative weights fraction is %f" %(i, fneg)
    print "Weighted content is ", weighted_hist.GetBinContent(i)
    print "Unweighted content is ", unweighted_hist.GetBinContent(i)

errors_canvas = ROOT.TCanvas("errcanvas", "errcanvas", 600, 300)
errors_hist.SetMaximum(1)
errors_hist.GetXaxis().SetTitle(xlabel)
errors_hist.Draw("")
dreamerrors_hist.SetMaximum(1)
dreamerrors_hist.Draw("same")
negweights_hist.SetMaximum(1)
negweights_hist.Draw("same")

legend = ROOT.TLegend(0.15, 0.6, 0.55, 0.92)
legend.AddEntry(errors_hist, "Rel. Stat. Error", "l")
legend.AddEntry(dreamerrors_hist, "Rel. Error Pos. Weights", "l")
legend.AddEntry(negweights_hist, "Negative Weight Fraction", "l")
legend.Draw()

errors_canvas.Print("~/www/DYweightStudies/%s_errors.pdf" % tree_var)
