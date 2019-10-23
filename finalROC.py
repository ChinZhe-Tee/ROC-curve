import os
import ROOT
import rootlogon
import collections
import math
import sys
from ROOT import TGraph
import array as array
  
ROOT.gROOT.SetBatch()
outDir  = './value/'

def main():


	sample = "ttbar"
	inFileName = "~/work/FYP/rootfiles_histo/version2/Histo_MC17_all.root"

	tagger1    = "CSVV2"
	tagger2    = "DeepB"
	tagger3	   = "DeepFlavB"
	
	yaxisname = "udsg-jet misid. probability"
	xaxisname = "b-jet efficiency"
  
	
   #Get root file with histograms
 
	inputFile  = ROOT.TFile.Open(inFileName)
	
   # Make TCanvas
	canv = ROOT.TCanvas("ratio","misid vs eff", 800, 800)
	canv.SetFillStyle( 4000 )
	canv.SetLeftMargin(0.15)
	canv.SetRightMargin(0.08)
	canv.SetTopMargin(0.07)
	canv.SetBottomMargin(0.15)
	canv.SetGrid()
	canv.SetLogy()
  
  # Set legend
  
  # legend position
	legpos = "Right"
	if legpos == "Left":
		xLat = 0.2
	elif legpos == "Right":
		xLat = 0.7 # move left and right
	else:
		xLat = 0.2
    
	yLat = 0.5 # move legend up and down, the larger( about 1 already at the edge of canvas) the higher it goes
	xLeg = xLat
	yLeg = yLat

	leg_g =  0.03 * 3 # 3 legend entry
	leg = ROOT.TLegend( xLeg, yLeg - leg_g, xLeg + 0.2, yLeg )
	leg.SetNColumns( 1 )
	leg.SetFillStyle( 0 )
	leg.SetTextFont( 43 )
	leg.SetTextSize( 20 )
  
  
  #Do for CSVV2
  #Get 2D histograms from root file
	histo2D_Flav5 = inputFile.Get("h_jet_hadFlav5_"+tagger1+"_pt")
	histo2D_Flav0 = inputFile.Get("h_jet_hadFlav0_"+tagger1+"_pt")
  
  #1D projection and rebin
	histo1D_Flav5_CSVV2 = histo2D_Flav5.ProjectionY("py_b_")
	histo1D_Flav0_CSVV2 = histo2D_Flav0.ProjectionY("py_l_")
  
	histo1D_Flav5_CSVV2.Rebin(4)
	histo1D_Flav0_CSVV2.Rebin(4)
  #Finding first and last bin
	firstbin1 =  histo1D_Flav5_CSVV2.FindFirstBinAbove()
	nbin1= histo1D_Flav5_CSVV2.FindLastBinAbove()
  #start a for loop for CSVV2
	x= array.array('d') # define array 
	y= array.array('d')
	
	ibin1 = firstbin1 # loop for b-jet efficiency
	for ibin1 in xrange ( firstbin1, nbin1 +1 ):
		
		Ntotal_bjets1= histo1D_Flav5_CSVV2.Integral()
		Ncut_bjets1 = histo1D_Flav5_CSVV2.Integral( ibin1, nbin1 +1)
		eff_b1 = (Ncut_bjets1/Ntotal_bjets1)
		#print(eff_b)
		x.append(eff_b1)
	
		Ntotal_ljets1= histo1D_Flav0_CSVV2.Integral()
		Ncut_ljets1 = histo1D_Flav0_CSVV2.Integral(ibin1, nbin1 +1)
		misid_light1 = (Ncut_ljets1/Ntotal_ljets1)
		#print(misid_l)
		
		y.append(misid_light1)
		
		
	#print([x],[y1])
	  
	n = nbin1 +1 -firstbin1
	gr_CSVV2 =TGraph(n,x,y)
	gr_CSVV2.GetXaxis().SetRangeUser(10e-4,1.1)
	gr_CSVV2.GetYaxis().SetRangeUser(10e-5,1.1)
	
	gr_CSVV2.GetYaxis().SetTitleOffset(1.25)
	gr_CSVV2.SetMarkerStyle(29)
	gr_CSVV2.SetLineColor(3)
	gr_CSVV2.SetMarkerColor(3)
	gr_CSVV2.SetTitle("Misid.prob vs efficiency")
	gr_CSVV2.SetTitle( "Misid.prob vs efficiency ; b-jet efficiency; udsg-jet misid. prob." )
	gr_CSVV2.Eval(0.30, 0)

	leg.AddEntry(gr_CSVV2,"CSVV2")
	gr_CSVV2.Draw("ACP")
	
##################################################################################################################################
    #Do for DeepB
	
  #Get 2D histograms from root file
	histo2D_Flav5_DeepB= inputFile.Get("h_jet_hadFlav5_"+tagger2+"_pt")
	histo2D_Flav0_DeepB = inputFile.Get("h_jet_hadFlav0_"+tagger2+"_pt")
  
  #1D projection and rebin
	histo1D_Flav5_DeepB = histo2D_Flav5_DeepB.ProjectionY("py_b_")
	histo1D_Flav0_DeepB = histo2D_Flav0_DeepB.ProjectionY("py_l_")
  
	histo1D_Flav5_DeepB.Rebin(4)
	histo1D_Flav0_DeepB.Rebin(4)
  #Finding first and last bin
	firstbin2 =  histo1D_Flav5_DeepB.FindFirstBinAbove()
	nbin2= histo1D_Flav5_DeepB.FindLastBinAbove()
  #start a for loop for CSVV2
	x2= array.array('d') # define array 
	y2= array.array('d')
	
	ibin2 = firstbin2 # loop for b-jet efficiency
	for ibin2 in xrange ( firstbin2, nbin2 +1 ):
		
		Ntotal_bjets2= histo1D_Flav5_DeepB.Integral()
		Ncut_bjets2 = histo1D_Flav5_DeepB.Integral(ibin2 , nbin2+1)
		eff_b2 = (Ncut_bjets2/Ntotal_bjets2)
		#print(eff_b)
		x2.append(eff_b2)
		
		Ntotal_ljets2= histo1D_Flav0_DeepB.Integral()
		Ncut_ljets2 = histo1D_Flav0_DeepB.Integral(ibin2 , nbin2+1)
		misid_light2 = (Ncut_ljets2/Ntotal_ljets2)
		#print(misid_l)
		
		y2.append(misid_light2)
		
	#print([x],[y_2])
	  
	n2 = nbin2 +1 -firstbin2
	gr_DeepB =TGraph(n2,x2,y2)
	gr_DeepB.GetYaxis().SetTitleOffset(1.25)
	gr_DeepB.SetMarkerStyle(20)
	gr_DeepB.SetLineColor(4)
	gr_DeepB.SetMarkerColor(4)
	leg.AddEntry(gr_DeepB,"DeepB")
	gr_DeepB.Draw("CP")
	
##############################################################################################################################

   #Do for DeepFlavB
	
  #Get 2D histograms from root file
	histo2D_Flav5_DeepFlavB= inputFile.Get("h_jet_hadFlav5_"+tagger3+"_pt")
	histo2D_Flav0_DeepFlavB = inputFile.Get("h_jet_hadFlav0_"+tagger3+"_pt")
  
  #1D projection and rebin
	histo1D_Flav5_DeepFlavB = histo2D_Flav5_DeepFlavB.ProjectionY("py_b_")
	histo1D_Flav0_DeepFlavB = histo2D_Flav0_DeepFlavB.ProjectionY("py_l_")
  
	histo1D_Flav5_DeepFlavB.Rebin(4)
	histo1D_Flav0_DeepFlavB.Rebin(4)
  #Finding first and last bin
	firstbin3 =  histo1D_Flav5_DeepFlavB.FindFirstBinAbove()
	nbin3= histo1D_Flav5_DeepFlavB.FindLastBinAbove()
  #start a for loop for CSVV2
	x3= array.array('d') # define array 
	y3= array.array('d')
	
	ibin3 = firstbin3 # loop for b-jet efficiency
	for ibin3 in xrange ( firstbin3, nbin3 +1 ):
		
		Ntotal_bjets3= histo1D_Flav5_DeepFlavB.Integral()
		Ncut_bjets3 = histo1D_Flav5_DeepFlavB.Integral(  ibin3 , nbin3 +1)
		eff_b3 = (Ncut_bjets3/Ntotal_bjets3)
		#print(eff_b)
		x3.append(eff_b3)
	
	
		Ntotal_ljets3= histo1D_Flav0_DeepFlavB.Integral()
		Ncut_ljets3 = histo1D_Flav0_DeepFlavB.Integral(ibin3 , nbin3 +1)
		misid_light3 = (Ncut_ljets3/Ntotal_ljets3)
		#print(misid_l)
		
		y3.append(misid_light3)
		
		
	#print([x],[y_2])
	  
	n3 = nbin3 +1 -firstbin3
	gr_DeepFlavB =TGraph(n3,x3,y3)
	gr_DeepFlavB.GetYaxis().SetTitleOffset(1.25)
	gr_DeepFlavB.SetMarkerStyle(33)
	gr_DeepFlavB.SetLineColor(28)
	gr_DeepFlavB.SetMarkerColor(28)
	leg.AddEntry(gr_DeepFlavB,"DeepB")
	gr_DeepFlavB.Draw("CP")
	
	leg.Draw()
	canv.Print(outDir + "finalROC_MC16.pdf")

   
   
  
   
    
  
  
if __name__ == "__main__":

 main()  
  
