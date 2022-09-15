__author__ = "Jeremy Leese | jeremy.leese@thomsonreuters.com | Technology - Product Eng - Content Platforms"
__copyright__ = "Copyright© (C) 2022 Thomson Reuters. All Rights Reserved."
__version__ = "0.1"

HVR_RSC_LIST = {

   # "INFRA" Hard Coded DB Resources
   "status": "status",
   "cci": "cci",
   "lager": "lager",
   "loadqueueoraprimary": "loadqueue",
   "loadqueue": "loadqueue",
   "loadqueueora": "loadqueue",
   "loadqueueprimary": "loadqueue",
   "perfmart": "perfmart.01a.01",
   "persist01a.persist": "persist01a.persist",
   "persist01b.persist": "persist01b.persist",
   "persist": "persist",
   "ecpqueue": "ecpqueue",
   "ecpqueue": "ecpqueue",
   "hadlc": "hadlc",
   "dlc": "dlc"
}

PROD_MASTER_RSC_LIST = {
   "authority":         "authority",
   "binpr.rac7.n1":     "doc.news.02",
   "binpr.rac7.n2":	   "doc.news.02",
   "bnp.rac10.n1":	   "doc.news.05",
   "bnp.rac10.n2":	   "doc.news.05",
   "bnp.rac11.n1":	   "doc.news.06",
   "bnp.rac11.n2":	   "doc.news.06",
   "bnp.rac12.n1":	   "doc.news.07",
   "bnp.rac12.n2":	   "doc.news.07",
   "bnp.rac13.n1":	   "doc.news.08",
   "bnp.rac13.n2":      "doc.news.08",
   "bnp.rac6.n1":	      "doc.news.01",
   "bnp.rac6.n2":	      "doc.news.01",
   "bnp.rac8.n1":	      "doc.news.03",
   "bnp.rac8.n2":	      "doc.news.03",
   "bnp.rac9.n1":	      "doc.news.04",
   "bnp.rac9.n2":	      "doc.news.04",
   "d3.cdp0391":	      "doc.doc3.01",
   "dkp.rac5.n1":	      "doc.dockets.01",
   "dkp.rac5.n2":	      "doc.dockets.01",
   "dkp.rac6.n1":	      "doc.dockets.02",
   "dkp.rac6.n2":	      "doc.dockets.02",
   "dkp.rac7.n1":	      "doc.dockets.03",
   "dkp.rac7.n2":	      "doc.dockets.03",
   "dlc":	            "dlc",
   "docha.rac1.n1":	   "doc.ha.01",
   "docha.rac1.n2":	   "doc.ha.01",
   "docha.rac2.n1":	   "doc.ha.02",
   "docha.rac2.n2":	   "doc.ha.02",
   "docha.rac3.n1":	   "doc.ha.03",
   "docha.rac3.n2":	   "doc.ha.03",
   "docha.rac4.n1":	   "doc.ha.04",
   "docha.rac4.n2":	   "doc.ha.04",
   "docloc.ha.01":      "hadlc",
   "gl.cdp0486":	      "doc.globalip.01",
   "gl.cdp0487":	      "doc.globalip.02",
   "glp.cdp0714":	      "doc.globalip.03",
   "glp.cdp0715":	      "doc.globalip.04",
   "gsp.rac06.n1":	   "doc.gsi.03",
   "gsp.rac06.n2":	   "doc.gsi.03",
   "gsp.rac07.n1":	   "doc.gsi.04",
   "gsp.rac07.n2":	   "doc.gsi.04",
   "gsp.rac14.n1":	   "doc.gsi.05",
   "gsp.rac14.n2":	   "doc.gsi.05",
   "gsp.rac15.n1":	   "doc.gsi.06",
   "gsp.rac15.n2":	   "doc.gsi.06",
   "gsp.rac4.n1":	      "doc.gsi.01",
   "gsp.rac4.n2":	      "doc.gsi.01",
   "gsp.rac5.n1":	      "doc.gsi.02",
   "gsp.rac5.n2":	      "doc.gsi.02",
   "hadlc":	            "hadlc",
   "loadqueue":	      "loadqueue",
   "loadqueueora":	   "loadqueue",
   "mdp07a":	         "metadoc.shared.01",
   "mdp12a":	         "metadoc.gsi.01",
   "medlit.rac2.n1":	   "doc.medlit.01",
   "medlit.rac2.n2":	   "doc.medlit.01",
   "metadocwest1":	   "metadoc.fermi.01",
   "metadocwest2":	   "metadoc.nonfermi.01",
   "metadocwestha":	   "metadoc.ha.01",
   "mxnorm":	         "norm.intl.01",
   "nimswest1":	      "nims.intl.01",
   "nimswest2":	      "nims.names.01",
   "nimswest3":	      "nims.docfam.01",
   "nop04a":	         "norm.patents.01",
   "nop38a":	         "norm.aunz.01",
   "norm.aunz.01":	   "norm.aunz.01",
   "norm.aunz":	      "norm.aunz.01",
   "nop39a":	         "norm.shared.01",
   "normshared1":	      "norm.shared.01",
   "normcobalt":	      "norm.wlncluster.01",
   "normwest1":	      "norm.shared.01",
   "normwest2":	      "norm.ml.citgref.01",
   "normwest3":	      "norm.keycite.01",
   "normwest4":	      "norm.bigregs.01",
   "normwestshared":	   "norm.keycit.shar.01",
   "nvp.rac15.n1":	   "lager",
   "nvp.rac15.n2":	   "lager",
   "prp.rac22.n1":      "doc.westlaw.04",
   "prp.rac22.n2":      "doc.westlaw.04",
   "qatar":	            "doc.qtar.01",
   "sgp.rac2.n1":	      "doc.saegis.01",
   "sgp.rac2.n2":	      "doc.saegis.01",
   "sgp.rac3.n1":	      "doc.saegis.02",
   "sgp.rac3.n2":	      "doc.saegis.02",
   "sh.cdp388.n1":	   "doc.shared.02",
   "sh.cdp388.n2":	   "doc.shared.02",
   "sh.cdp389.n1":	   "doc.shared.03",
   "sh.cdp389.n2":	   "doc.shared.03",
   "shp.rac3.n1":	      "doc.shared.01",
   "shp.rac3.n2":	      "doc.shared.01",
   "shp.rac5.n1":	      "doc.shared.04",
   "shp.rac5.n2":	      "doc.shared.04",
   "trtanort":	         "nort.trtax.01",
   "trtanort1":	      "nort.trtax.01",
   "ttp.rac2.n1":	      "doc.Tax.01",
   "ttp.rac2.n2":	      "doc.Tax.01",
   "wfilingsmetadoc":	"metadoc.gsi.01",
   "wlcdp1075.n1":	   "doc.westlaw.05",
   "wlcdp1075.n2":	   "doc.westlaw.05",
   "wlnuddoc.rac1.n1":  "doc.dataroom.01",
   "wlnuddoc.rac1.n2":  "doc.dataroom.01",
   "wlnuddoc":	         "doc.dataroom.01",
   "wlnuddoc":	         "doc.dataroom.01",
   "wlnv.rac20.n1":	   "doc.westlaw.06",
   "wlnv.rac20.n2":	   "doc.westlaw.06",
   "wlnv.rac21.n1":	   "doc.westlaw.07",
   "wlnv.rac21.n2":	   "doc.westlaw.07",
   "wlnv.rac24.n1":	   "doc.westlaw.09",
   "wlnv.rac24.n2":	   "doc.westlaw.09",
   "wlnv.rac25.n1":	   "doc.westlaw.10",
   "wlnv.rac25.n2":	   "doc.westlaw.10",
   "wlnv.rac28.n1":	   "doc.westlaw.12",
   "wlnv.rac28.n2":	   "doc.westlaw.12",
   "wlp.rac14.n1":	   "doc.westlaw.01",
   "wlp.rac14.n2":	   "doc.westlaw.01",
   "wlp.rac15.n1":	   "doc.westlaw.02",
   "wlp.rac15.n2":	   "doc.westlaw.02",
   "wlp.rac16.n1":	   "doc.westlaw.03",
   "wlp.rac16.n2":	   "doc.westlaw.03",
   "wlp.rac17.n1":	   "doc.westlaw.04",
   "wlp.rac17.n2":	   "doc.westlaw.04",
   "wlp.rac26.n1":	   "doc.westlaw.11",
   "wlp.rac26.n2":	   "doc.westlaw.11",
   "wlp.rac29.n1":	   "doc.westlaw.13",
   "wlp.rac29.n2":	   "doc.westlaw.13",
   "wlp.rac30.n1":	   "doc.westlaw.14",
   "wlp.rac30.n2":	   "doc.westlaw.14",
   "wlp.rac31.n1":	   "doc.westlaw.15",
   "wlp.rac31.n2":	   "doc.westlaw.15",
   "wlp.rac32.n1":	   "doc.westlaw.16",
   "wlp.rac32.n2":	   "doc.westlaw.16",
   "wlp.rac33.n1":	   "doc.westlaw.17",
   "wlp.rac33.n2":	   "doc.westlaw.17",
   "wlp.rac34.n1":	   "doc.westlaw.18",
   "wlp.rac34.n2":	   "doc.westlaw.18",
   "wlp.rac35.n1":	   "doc.westlaw.19",
   "wlp.rac35.n2":	   "doc.westlaw.19",
   "wlp.rac36.n1":	   "doc.westlaw.20",
   "wlp.rac36.n2":	   "doc.westlaw.20",
   "wlp.rac37.n1":	   "doc.westlaw.21",
   "wlp.rac37.n2":	   "doc.westlaw.21",
   "wlp34.rac.n1":	   "doc.westlaw.18",
   "wlp34.rac.n2":	   "doc.westlaw.18",
   "wlp35.rac.n1":	   "doc.westlaw.19",
   "wlp35.rac.n2":	   "doc.westlaw.19",
   "wtoc":	            "nort.shared.01",
   "wwbcmetadoc":	      "metadoc.gsi.01",
   "wwlkccitingrefss":                 "norm.intl.01",
   "WLNPreDocketAuthLocal.Site-B.r":	"authority.02",
   "WLNPreDocketAuthMain.master.u":	   "authority.02",
   "WLNUDAuth.rac1.n1Local.Site-A.u":	"authority.01",
   "WLNUDAuth.rac1.n1Local.Site-B.u":	"authority.01",
   "WLNUDAuth.rac1.n1Remote.Site-A.r": "authority.01",
   "WLNUDAuth.rac1.n1Remote.Site-B.r":	"authority.01",
   "WLNUDAuth.rac1.n2Local.Site-A":	   "authority.01",
   "WLNUDAuth.rac1.n2Local.Site-B.u":	"authority.01",
   "WLNUDAuth.rac1.n2Remote.Site-A.r":	"authority.01",
   "WLNUDAuth.rac1.n2Remote.Site-B.r":	"authority.01"
}

PROD_DB_TYPE_DICT = {
   "doc.dataroom.01": "DOC",
   "doc.doc3.01":	"DOC",
   "doc.dockets.01":	"DOC",
   "doc.dockets.02":	"DOC",
   "doc.dockets.03":	"DOC",
   "doc.dockets.01":	"DOC",
   "doc.dockets.02":	"DOC",
   "doc.dockets.03":	"DOC",
   "doc.globalip.01":	"DOC",
   "doc.globalip.02":	"DOC",
   "doc.globalip.03":	"DOC",
   "doc.globalip.04":	"DOC",
   "doc.gsi.01":	"DOC",
   "doc.gsi.02":	"DOC",
   "doc.gsi.03":	"DOC",
   "doc.gsi.04":	"DOC",
   "doc.gsi.05":	"DOC",
   "doc.gsi.06":	"DOC",
   "doc.ha.01":	"DOC",
   "doc.ha.02":	"DOC",
   "doc.ha.03":	"DOC",
   "doc.ha.04":	"DOC",
   "doc.gsi.01":	"DOC",
   "doc.gsi.02":	"DOC",
   "doc.gsi.03":	"DOC",
   "doc.gsi.04":	"DOC",
   "doc.gsi.05":	"DOC",
   "doc.gsi.06":	"DOC",
   "doc.ha.01":	"DOC",
   "doc.ha.02":	"DOC",
   "doc.ha.03":	"DOC",
   "doc.ha.04":	"DOC",
   "dlc":	"DLC",
   "hadlc":	"DLC",
   "doc.medlit.01":	"DOC",
   "doc.news.01":	"DOC",
   "doc.news.02":	"DOC",
   "doc.news.03":	"DOC",
   "doc.news.04":	"DOC",
   "doc.news.05":	"DOC",
   "doc.news.06":	"DOC",
   "doc.news.07":	"DOC",
   "doc.news.08":	"DOC",
   "doc.medlit.01":	"DOC",
   "doc.news.01":	"DOC",
   "doc.news.02":	"DOC",
   "doc.news.03":	"DOC",
   "doc.news.04":	"DOC",
   "doc.news.05":	"DOC",
   "doc.news.06":	"DOC",
   "doc.news.07":	"DOC",
   "doc.news.08":	"DOC",
   "doc.qtar.01":	"DOC",
   "doc.saegis.01":	"DOC",
   "doc.saegis.02":	"DOC",
   "doc.shared.01":	"DOC",
   "doc.shared.02":	"DOC",
   "doc.shared.03":	"DOC",
   "doc.shared.04":	"DOC",
   "doc.tax.01":	"DOC",
   "doc.westlaw.01":	"DOC",
   "doc.westlaw.02":	"DOC",
   "doc.westlaw.03":	"DOC",
   "doc.westlaw.04":	"DOC",
   "doc.westlaw.05":	"DOC",
   "doc.westlaw.06":	"DOC",
   "doc.westlaw.07":	"DOC",
   "doc.saegis.01":	"DOC",
   "doc.saegis.02":	"DOC",
   "doc.Tax.01":	"DOC",
   "doc.westlaw.01":	"DOC",
   "doc.westlaw.02":	"DOC",
   "doc.westlaw.03":	"DOC",
   "doc.westlaw.04":	"DOC",
   "doc.westlaw.05":	"DOC",
   "doc.westlaw.06":	"DOC",
   "doc.westlaw.07":	"DOC",
   "doc.dataroom.01a":	"DOC",
   "doc.westlaw.09":	"DOC",
   "doc.westlaw.10":	"DOC",
   "doc.westlaw.11":	"DOC",
   "doc.westlaw.12":	"DOC",
   "doc.westlaw.13":	"DOC",
   "doc.westlaw.14":	"DOC",
   "doc.westlaw.15":	"DOC",
   "doc.westlaw.16":	"DOC",
   "doc.westlaw.17":	"DOC",
   "doc.westlaw.18":	"DOC",
   "doc.westlaw.19":	"DOC",
   "doc.westlaw.20":	"DOC",
   "doc.westlaw.21":	"DOC",
   "doc.westlaw.09":	"DOC",
   "doc.westlaw.10":	"DOC",
   "doc.westlaw.11":	"DOC",
   "doc.westlaw.12":	"DOC",
   "doc.westlaw.13":	"DOC",
   "doc.westlaw.14":	"DOC",
   "doc.westlaw.15":	"DOC",
   "doc.westlaw.16":	"DOC",
   "doc.westlaw.17":	"DOC",
   "doc.westlaw.18":	"DOC",
   "doc.westlaw.19":	"DOC",
   "doc.westlaw.20":	"DOC",
   "doc.westlaw.21":	"DOC",
   "authority":	"AUTHORITY",
   "authority.01":	"AUTHORITY",
   "authority.02":	"AUTHORITY",
   "metadoc.fermi.01":	"METADOC",
   "metadoc.fermi.01":	"METADOC",
   "metadoc.fermi.01":	"METADOC",
   "metadoc.fermi.01":	"METADOC",
   "metadoc.gsi.01":	"METADOC",
   "metadoc.gsi.01":	"METADOC",
   "metadoc.ha.01":	"METADOC",
   "metadoc.ha.01":	"METADOC",
   "metadoc.ha.01":	"METADOC",
   "metadoc.ha.01":	"METADOC",
   "metadoc.nonfermi.01":	"METADOC",
   "metadoc.shared.01":	"METADOC",
   "nims.docfam.01":	"nims",
   "nims.docfam.01":	"nims",
   "nims.docfam.01":	"nims",
   "nims.docfam.01":	"nims",
   "nims.intl.01":	"nims",
   "nims.names.01":	"nims",
   "nims.names.01":	"nims",
   "nims.names.01":	"nims",
   "nims.names.01":	"nims",
   "norm.bigregs.01":	"norm",
   "norm.bigregs.01":	"norm",
   "norm.bigregs.01":	"norm",
   "norm.bigregs.01":	"norm",
   "norm.intl.01":	"norm",
   "norm.keycite.01":	"norm",
   "norm.keycit.shar.01":	"norm",
   "norm.ml.citgref.01":	"norm",
   "norm.ml.citgref.01":	"norm",
   "norm.patents.01":	"norm",
   "norm.shared.01":	"norm",
   "norm.wlncluster.01":	"norm",
   "norm.wlncluster.01":	"norm",
   "norm.wlncluster.01":	"norm",
   "norm.wlncluster.01":	"norm",
   "nort.shared.01":	"norm",
   "nort.trtax.01":	"norm",
   "dlc":	"DLC",
   "docloc.ha.01":	"DLC"
}  



CLIENT_INF_RSC_DICT = {
   "status": "status",
   "cci": "cci",
   "lager": "lager",
   "loadqueueoraprimary": "loadqueue",
   "loadqueueprimary": "loadqueue",
   "loadqueue": "loadqueue",
   "loadqueueora": "loadqueue",
   "perfmart": "perfmart",
   "persist01a.persist": "persist01a.persist",
   "persist01b.persist": "persist01b.persist",
   "dlc": "dlc",
   "ecpqueue": "ecpqueue",
   "authority": "authority"
}

CLIENT_BKT_RSC_DICT = {
   "wkccitngr": 		   "norm.shared.01",        #4
   "wtoc31": 			   "nort.shared.01",        #32     
   "noa38a0": 			   "norm.intl.01",          #16              
   "noa03a0": 			   "norm.keycit.shar.01",   #4
   "mda07a": 			   "metadoc.shared.01",     #16	
   "nimswest1": 		   "nims.kcflaghist.01",    #4
   "metadocwestha": 	   "metadoc.ha.01",         #16
   "metadocwest2": 	   "metadoc.nonfermi.01",   #32
   "MetaDocWest1": 	   "metadoc.fermi.01",      #32 *metadoc.fermi.01, metadoc.fermi.02
   "nimswest4": 		   "nims.docfam.01",        #32 *nims.docfam.01, nims.docfam.02
   "wwlkcciterefqa": 	"norm.patents.01",       #32 *norm.patents.01, norm.patents.02, norm.patents.03, norm.patents.04
   "wwlkcciterefss": 	"norm.intl.01",         #16 *norm.intl.01
   "normwest4": 		   "norm.patents.01",       #32 *norm.patents.01, norm.patents.02, norm.patents.03, norm.patents.04
   "trtanort1": 		   "nort.trtax.01",         #32 *nort.trtax.01, nort.trtax.02
   "normwest7": 		   "norm.keycite.01",       #32 *norm.keycite.01, norm.keycite.02, norm.keycite.03, norm.keycite.04
   "wwltrtmtphrs32qa":  "nims.names.01",         #32 *nims.names.01                 ****
   "wwlnames32qa": 	   "nims.names.02",         #32 *nims.names.02, nims.names.03  ****
   "wwlnames32": 	 	   "nims.names.03",         #32 *nims.names.04	               ****
   "normwest6": 		   "norm.profiler.01",      #16 *norm.profiler.01, norm.profiler.02

   "gs.cdq0296":	      "doc.gsi.01",
   "medlit.rac1.n1":	   "doc.medlit.01",
   "medlit.rac1.n2":	   "doc.medlit.01",
   "sga.rac3.n1":	      "doc.saegis.01",
   "sha.rac4.n1":	      "doc.shared.01",
   "sha.rac4.n2":	      "doc.shared.01",
   "sha.rac5.n1":	      "doc.shared.03",
   "SHA.RAC5.N2":	      "doc.shared.03",
   "shq.node114.n1":	   "doc.shared.02",
   "tta.rac1.n1":	      "doc.tax.01",
   "wl.cda0319.n1":	   "doc.westlaw.05",
   "wl.cda0320":	      "doc.westlaw.01",
   "wla.rac29.n1":	   "doc.westlaw.04",
   "wla.rac29.n2":	   "doc.westlaw.04",
   "WLA.RAC30.N1":	   "doc.dataroom.01",
   "WLA.RAC30.N2":	   "doc.dataroom.01",
   "WLNUDDOC":	         "doc.dataroom.01",
   "WLNUDHADOCA":	      "doc.ha.03",
   "WLNUDHADOCB":	      "doc.ha.03",
   "wlnv.rac2.n1":	   "doc.westlaw.02",
   "wlnv.rac2.n2":	   "doc.westlaw.02",
   "wlnv.rac5.n1":	   "doc.westlaw.03",
   "wlnv.rac5.n2":	   "doc.westlaw.03",
   "wlnv.rac7.n1":	   "doc.westlaw.07",
   "wlnv.rac7.n2":	   "doc.westlaw.07"
}

CLIENT_DOC_RSC_DICT = {
   "cdq0296gs.": "doc.gsi.01", #????
   "sha.rac4.n1": "doc.shared.01",
   "sha.rac4.n2": "doc.shared.01",
   "sha.rac5.n1": "doc.westlaw.03",
   "sha.rac5.n2": "doc.westlaw.03",
   "shq.node114.n1": "doc.shared.02", 
   "wl.cda0320": "doc.westlaw.04",
   "wla.rac29.n1": "doc.westlaw.04",
   "wla.rac29.n2": "doc.westlaw.04",
   "wla.racc30.n1": "doc.dataroom.01",
   "wlnuddoc": "doc.dataroom.01",
   "wlnv.rac2.n1": "doc.westlaw.01",
   "wlnv.rac2.n2": "doc.westlaw.02",
   "wlnv.rac5.n1": "doc.westlaw.03",
   "wlnv.rac5.n2": "doc.westlaw.03",
   "wlnuddoc": "doc.dataroom.01",
   "gs.cdq0296": "doc.gsi.01",
   "dha.rac1.n1": "doc.ha.01",
   "dha.rac2.n1": "doc.ha.02",
   "wlnudhadoca": "doc.ha.03",
   "medlit.rac1.n1": "doc.medlit.01",
   "medlit.rac1.n2": "doc.medlit.01",
   "bna.cdq0283.n1": "doc.news.01",
   "bna.cdq0284.n1": "doc.news.03",
   "bna.rac04.n1": "doc.news.04",
   "sha.rac02.n1": "doc.news.02",
   "qatar": "doc.qtar.01",
   "sga.rac3.n1": "doc.saegis.01",
   "sga.rac2.n1": "doc.saegis.02",
   "wha.rac4.n1": "doc.shared.01",
   "shq.node114.n1": "doc.shared.02",
   "sha.rac5.n1": "doc.shared.03",
   "tta.rac1.n1": "doc.tax.01",
   "wl.cda0320": "doc.westlaw.01",
   "wlnv.rac2.n1": "doc.westlaw.02",
   "wlnv.rac5.n1": "doc.westlaw.03",
   "wla.rac29.n1": "doc.westlaw.04",
   "wl.cda0319.n1": "doc.westlaw.05",

   "wlnv.rac7.n1": "doc.westlaw.06",
   "wlnv.rac6.n1": "doc.westlaw.07",
   
   "wla.rac30.n1": "doc.westlaw.08",
   "dlc": "dlc",
   "WLNPreDocketAuthLocal": "authority.wlnpdl.01",
   "WLNPreDocketAuthMain": "authority.wlnpdm.01",
   "WLNPreDocketAuthRemote": "authority.wlnpdr.01",
   "WLNUDAuthorityLocal": "authority.wlnudl.01",
   "WLNUDAuthorityRemote": "authority.wlnudr.01",

   "gs.cdq0296":	      "doc.gsi.01",
   "medlit.rac1.n1":	   "doc.medlit.01",
   "medlit.rac1.n2":	   "doc.medlit.01",
   "sga.rac3.n1":	      "doc.saegis.01",
   "sha.rac4.n1":	      "doc.shared.01",
   "sha.rac4.n2":	      "doc.shared.01",
   "sha.rac5.n1":	      "doc.shared.03",
   "SHA.RAC5.N2":	      "doc.shared.03",
   "shq.node114.n1":	   "doc.shared.02",
   "TTA.RAC1.N1":	      "doc.tax.01",
   "wl.cda0319.n1":	   "doc.westlaw.05",
   "wl.cda0320":	      "doc.westlaw.01",
   "wla.rac29.n1":	   "doc.westlaw.04",
   "wla.rac29.n2":	   "doc.westlaw.04",
   "WLA.RAC30.N1":	   "doc.dataroom.01",
   "WLNUDDOC":	         "doc.dataroom.01",
   "WLNUDHADOCA":	      "doc.ha.03",
   "WLNUDHADOCB":	      "doc.ha.03",
   "wlnv.rac2.n1":	   "doc.westlaw.02",
   "wlnv.rac2.n2":	   "doc.westlaw.02",
   "wlnv.rac5.n1":	   "doc.westlaw.03",
   "WLNV.RAC5.N2":	   "doc.westlaw.03",
   "WLNV.RAC7.N1":	   "doc.westlaw.07",
   "WLNV.RAC7.N2":	   "doc.westlaw.07"

}

QC_RSC_DICT = {
      "alpha": "norm.alpha.01", #0-3
      "a.doc": "SKIP",
      "anchor.toc": "SKIP",
      "bigboy.or.doc": "SKIP",
      "bpi3norm": "norm-bpi3-01", #0-31
      "cci":	"cci",
      "cci-not":	"cci",
      "cci.ora":	"cci",
      "ccireplica.slave": "cci", #1-2
      "ccnimsscalingretr": "nims-ccscaleretr-02", #0-31
      "ccunitoracoomp": "norm-ccunitcoomp-01", #0-31
      "cloudy": "SKIP",
      "loadqueue": "loadqueue",
      "cn=perfcsloc1": "SKIP",
      "of": "SKIP",
      "dale0": "SKIP",
      "datesec.doc": "SKIP",
      "DB2QCLOADNOREL": "SKIP", #0-3
      "DB2QCLOADREG": "SKIP", #0-3
      "dlc": "dlc", #0-7
      "doc": "doc.02",
      "doc.ora": "doc.02",
      "DOC1_25MB": "doc.01",
      "docregression2.doc": "doc.02",
      "docregression2.toc": "doc.02",
      "dummy": "SKIP",
      "dummy.toc": "SKIP",
      "dyndd.doc": "SKIP",
      "dyndd.toc": "SKIP",
      "dynddctl.toc": "SKIP",
      "dynddctl.doc": "SKIP",
      "dynddDowningtown.doc": "SKIP",
      "ecpqueue": "ecpqueue",
      "EHAQCAUTHORITY": "authority.01",
      "EHAQCAUTHORITY.SLAVE": "authority.02",
      "fsupp.doc": "SKIP",
      "generic": "SKIP", #0-3
      "genericNoRel": "SKIP", #0-3
      "hadlc": "doc.ha.01", #0-7
      "hansborodoc": "doc.ha.01",
      "hansborodoc.slave": "doc.ha.01",
      "keycite": "SKIP", #0-3
      "lager": "lager",
      "loadqueueora": "loadqueue",
      "loadtst": "SKIP", #0-3
      "maverick7doc.doc": "SKIP",
      "metadoc.cms": "metadoc.cms", #0-31 + .slave
      "metadocmain": "metadoc.quick.01", #10-17 + .slave
      "metadocperfquick": "metadoc.perfquick.01", #0-7
      "metadocperftest": "metadoc.perfquick.01", #0-31 + .slave
      "metadocquick": "metadoc.quick.01", #0-7
      "nathan2.doc": "SKIP",
      "nathan2.toc": "SKIP",
      "nims1connect": "nims.connect.01", #0-31
      "nimsangmultdmn": "nims.ccscaleretr.02", #0-3
      "nimsqccourts": "nims.ccscaleretr.02", #0-3
      "nimsqceasel": "nims.ccscaleretr.02", #0-3
      "nimsqceaselload": "nims.ccscaleretr.02", #0-3
      "nimsqcload": "nims.ccscaleretr.02", #0-3
      "nimsqconline": "nims.ccscaleretr.02", #0-3
      "nimsqcregress": "nims.ccscaleretr.02", #0-3
      "nimsqcregressload": "nims.ccscaleretr.02", #0-3
      "nimsqctempuser": "nims.ccscaleretr.02", #0-3
      "nimsravi": "nims.ccscaleretr.02", #0-3
      "nimsscalingload": "nims.ccscaleretr.02", #0-31 + .slave
      "nimsscalingperf": "nims.ccscaleretr.02", #0-31
      "nimsscalingretr": "nims.ccscaleretr.02", #0-31
      "nimssharedconn": "SKIP", #0-31
      "norm1connect": "norm.connect.02", #0-31
      "normperf1": "norm.perf1.01", #0-31
      "normscalingload": "norm.perf.bpi2.01", #0-31
      "normscalingperf": "norm.perf.bpi2.01", #0-31 + .slave
      "normscalingretr": "norm.perf.bpi2.01", #0-31
      "normsharedconn": "norm.perf.bpi2.01", #0-31
      "normsharedconnload": "norm.perf.bpi2.01", #0-31
      "normspanish1": "norm.bpi3.01", #0-31
      "normspanish2": "norm.bpi3.01", #0-31
      "normrtermhighret": "norm.bpi3.01", #0-31
      "normTestResource0": "norm.bpi3.01",
      "nortperf1": "nort.perf1.01", #0-31
      "nss.doc": "SKIP",
      "nut.doc": "SKIP",
      "nvc01a.persist": "persist", #0-3
      "nvc01z.persist": "persist", #0-3
      "nvc01z.persistsummary": "persist",
      "nvc04.doc.slave": "doc.04",
      "nvc04.doc": "doc.04",
      "nvc05a.content.slave": "doc.06",
      "nvc04a.doc": "doc.04",
      "nvc04a.doc.slave": "doc.04",
      "nvc05a.doc": "doc.06",
      "nvc05a.toc": "doc.06",
      "nvc05a.doc.slave": "",
      "nvc08a.persist": "persist",
      "nvc08z.persist": "persist",
      "nvc08a.persistsummary": "persist",
      "nvc18a.content": "doc.02", #slave
      "nvc19a.content": "doc.01", #slave
      "nvc20a.content": "configmon.01", #slave
      "nvd18a.content": "doc.03", #slave
      "nxhdoc.doc": "SKIP",
      "nxhdoc": "SKIP",
      "nxhtest.doc": "SKIP",
      "nxhtoc.toc": "SKIP",
      "oradoc": "doc.02",
      "oradoc2": "doc.02",
      "oradoc.slave": "doc.02",
      "oradoc-dev": "SKIP",
      "orageneric": "SKIP", #0-3
      "oramig.doc": "SKIP",
      "oramig.toc": "SKIP",
      "oramigrperf": "SKIP",
      "oraqcloadreg": "SKIP", #0-3
      "oraqcloadregnorel": "SKIP", #0-3
      "oraqcregr": "SKIP", #0-3
      "oraqcregrNoRel": "SKIP", #0-3
      "oratoc-dev": "SKIP",
      "partialupreg.doc": "SKIP",
      "payload": "norm.bpi3.01", #0-31
      "pdbd0378_1.doc": "doc.S3QC.01", #slave
      "pdbd1067_1.doc": "doc.01", #slave
      "PERFBPI2norm": "norm.bpi3.01", #0-3
      "perfcsloc": "doc.06", #0-31
      "perfmetadoc": "metadoc.perfquick.01", #0-31

      "persist": "persist", #0-3 +slave
      
      "nvd08a.persist0": "persist", #persist.01a0
      "nvd08a.persist1": "persist", #persist.01a1
      "nvd08a.persist2": "persist", #persist.01a2
      "nvd08a.persist3": "persist", #persist.01a3

      "nvd08z.persist0": "persist", #persist.01a0
      "nvd08z.persist1": "persist", #persist.01a1
      "nvd08z.persist2": "persist", #persist.01a2
      "nvd08z.persist3": "persist", #persist.01a3
      

      "persist01a.persist0": "persist", #persist.01a0
      "persist01a.persist1": "persist", #persist.01a1
      "persist01a.persist2": "persist", #persist.01a2
      "persist01a.persist3": "persist", #persist.01a3

      "persist01a.persist0": "persist", #persist.01a0
      "persist01a.persist1": "persist", #persist.01a1
      "persist01a.persist2": "persist", #persist.01a2
      "persist01a.persist3": "persist", #persist.01a3
      
      "persist01b.persist0": "persist", #persist.01a0
      "persist01b.persist1": "persist", #persist.01a1
      "persist01b.persist2": "persist", #persist.01a2
      "persist01b.persist3": "persist", #persist.01a3



      "qcmichaelh": "norm.perf.bpi2.01", #0-31
      "qcmrregdb2": "norm.perf.bpi2.01", #0-3
      "qcnortload": "norm.perf.bpi2.01", #0-3
      "qcnortretr": "norm.perf.bpi2.01", #0-3
      "qcregtestoraclemr": "norm.perf.bpi2.01", #0-3
      "qcregtestoranorelmr": "norm.perf.bpi2.01", #0-3
      "qcunittestoraclemr": "norm.perf.bpi2.01", #0,3
      "qcunittestoracomp": "norm.perf.bpi2.01", #0-31
      "qcunittestoranorelmr": "norm.perf.bpi2.01", #0-3
      "RegionSyncBB": "SKIP",
      "repltest.doc": "SKIP",
      "repltest.toc": "SKIP",
      "rtc01a.doc": "SKIP",
      "saegis.swat": "SKIP",
      "satatest": "SKIP", #1-3
      "SearchDocLimit.doc": "SKIP",
      "SearchDocLimit.toc": "SKIP",
      "searchviews.doc": "SKIP",
      "searchviewsdyn.doc": "SKIP",
      "SectionSymbol": "SKIP",
      "sharedconnload": "norm.bpi3.01", #0-31
      "sharedconnretr": "norm.bpi3.01", #0-31
      "srchreg2.doc": "SKIP",
      "srchreg2.toc": "SKIP",
      "status": "status",
      "test.tf.oradoc": "SKIP",
      "toc": "SKIP",
      "toc.ora": "SKIP",
      "tocrollbackora": "SKIP",
      "tocrollbacktest": "SKIP",
      "wkccitng": "SKIP", #0,3
      "wldir.doc": "SKIP",
      "wldir.toc": "SKIP",
      "zztop2.doc": "SKIP"
   }