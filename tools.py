from datetime import datetime
import pytz


class Object:
  def __init__(self):
    return


def getInformation(info=None):
  TZ = 'Japan'
    
  if not info: info = Object()
  info.author = 'TM'
  info.date = "{} (in {})".format(datetime.now(pytz.timezone(TZ)).strftime("%A %d %B %Y %H:%M%:%S"), TZ)
  info.base = ''
  return info


def getNavigation(loop=None):
  if not loop: loop = Object()
  loop.navi = []
  loop.navi.append({
    'href': "index.html",
    'text': 'FrontPage'
  })
  loop.navi.append({
    'href': "presentations.html",
    'text': 'Presentations'
  })
  loop.navi.append({
    'href': "publications.html",
    'text': 'Publications'
  })
  loop.navi.append({
    'href': "links.html",
    'text': 'Links'
  })
  return loop


def getLinks(link=None):
  if not link: link = Object()

  link.news_jp = []
  link.news_jp.append({'text': '読売', 'href': "https://www.yomiuri.co.jp"})
  link.news_jp.append({'text': '産経', 'href': "https://sankei.com"})
  link.news_jp.append({'text': '日経', 'href': "https://www.nikkei.co.jp"})
  link.news_jp.append({'text': '朝日', 'href': "https://www.asahi.com"})
  link.news_jp.append({'text': '毎日', 'href': "https://mainichi.jp"})
  link.news_jp.append({'text': 'FNN', 'href': "https://www.fnn.jp"})
  link.news_jp.append({'text': '夕刊フジ', 'href': "https://www.zakzak.co.jp"})

  link.news_en = []
  link.news_en.append({'text': 'The Washington Post', 'href': "https://www.washingtonpost.com"})
  link.news_en.append({'text': 'The New York Times', 'href': "https://www.nytimes.com"})
  link.news_en.append({'text': 'The Wall Street Journal', 'href': "https://www.wsj.com"})
  link.news_en.append({'text': 'The Telegraph', 'href': "https://www.telegraph.co.uk"})
  link.news_en.append({'text': 'The Guardian', 'href': "https://www.theguardian.com"})
  link.news_en.append({'text': 'CNN', 'href': "https://edition.cnn.com"})
  link.news_en.append({'text': 'BBC', 'href': "https://www.bbc.com"})
  link.news_en.append({'text': 'AlJazeera', 'href': "https://www.aljazeera.com"})
  link.news_en.append({'text': 'Axios', 'href': "https://www.axios.com"})
  link.news_en.append({'text': 'Signal', 'href': "https://www.gzeromedia.com/signal"})
  link.news_en.append({'text': 'ProPublica', 'href': "https://www.propublica.org"})
  link.news_en.append({'text': 'Project Syndicate', 'href': "https://www.project-syndicate.org"})
  link.news_en.append({'text': 'bellingcat', 'href': "https://www.bellingcat.com"})
  link.news_en.append({'text': 'Wiki Tribune', 'href': "https://www.wikitribune.com"})

  return link


def getConferences(loop=None):
  if not loop: loop = Object()
  loop.conf_int = []

  loop.conf_int.append({
    'year': '2016',
    'site': "http://chep2016.org",
    'name': '22nd International Conference on Computing in High Energy and Nuclear Physics',
    'venue': 'San Francisco',
    'title': "Flexible trigger menu implementation on the Global Trigger for the CMS Level-1 trigger upgrade",
    'slides': None,
    'poster': None,
    'proceedings': "http://iopscience.iop.org/article/10.1088/1742-6596/898/3/032033"
  })
  loop.conf_int.append({
    'year': '2015',
    'site': "http://chep2015.kek.jp",
    'name': '22nd International Conference on Computing in High Energy and Nuclear Physics',
    'venue': 'Okinawa',
    'title': "Software for implementing trigger algorithms on the upgraded CMS Global Trigger System",
    'slides': None,
    'poster': None,
    'proceedings': "http://iopscience.iop.org/article/10.1088/1742-6596/664/8/082031",
  })
  loop.conf_int.append({
    'year': '2012',
    'site': "http://rt2012.lbl.gov",
    'name': '18th IEEE REAL-TIME Conference',
    'venue': 'Berkeley',
    'title': 'The ATLAS Muon Trigger Performance in Proton-Proton Collisions at = &radic;<span style="text-decoration: overline">s</span> 7 TeV',
    'slides': None,
    'poster': None,
    'proceedings': "https://ieeexplore.ieee.org/document/6418208/?tp=&arnumber=6418208&refinements%3D4225471300%26filter%3DAND(p_IS_Number:6418089",
  })
  loop.conf_int.append({
    'year': '2012',
    'site': "http://plhc2012.triumf.ca",
    'name': 'Physics at LHC',
    'venue': 'Vancouver',
    'title': 'Onia production at ATLAS',
    'slides': "http://cdsweb.cern.ch/record/1454651/files/ATL-PHYS-SLIDE-2012-348.pdf",
    'poster': None,
    'proceedings': "http://cdsweb.cern.ch/record/1477921/files/ATL-PHYS-PROC-2012-180.pdf",
  })
  loop.conf_int.append({
    'year': '2010',
    'site': "http://dis2010.to.infn.it",
    'name': 'XVIII International Workshop on Deep-Inelastic Scattering and Related Subjects',
    'venue': 'Florence',
    'title': 'Charm and beauty physics at ATLAS',
    'slides': "http://cdsweb.cern.ch/record/1266614/files/ATL-PHYS-SLIDE-2010-069.pdf",
    'poster': None,
    'proceedings': "http://cdsweb.cern.ch/record/1274854/files/ATL-PHYS-PROC-2010-036.pdf",
  })
  loop.conf_int.append({
    'year': '2007',
    'site': "http://www.hep.man.ac.uk/HEP2007/",
    'name': 'International Europhysics Conference on High Energy Physics',
    'venue': 'Manchester',
    'title': 'The MICE scintillating-fibre tracker',
    'slides': None,
    'poster': 'http://www.hep.man.ac.uk/HEP2007/eps07-posters.html',
    'proceedings': None,
  })
  loop.conf_int.append({
    'year': '2001',
    'site': "http://www.bo.infn.it/dis2001/",
    'name': 'IX International Workshop on Deep Inelastic Scattering',
    'venue': 'Bologna',
    'title': 'Isolated High Energy Lepton and Missing Transverse Momentum at ZEUS',
    'slides': "http://www.bo.infn.it/dis2001/wg/overhead/HI/takashi-matsushita.ps.gz",
    'poster': None,
    'proceedings': "https://www.worldscientific.com/worldscibooks/10.1142/4814",
  })
  loop.conf_int.append({
    'year': '2000',
    'site': "",
    'name': '4th International Symposium on Development and Application of Semiconductor Tracking Detectors',
    'venue': 'Hiroshima',
    'title': 'Optical Alignment System for the ZEUS MicroVertex Detector',
    'slides': None,
    'poster': None,
    'proceedings': "https://www.sciencedirect.com/science/article/pii/S0168900201005939?via%3Dihub",
  })
  loop.conf_int.append({
    'year': '1999',
    'site': "",
    'name': 'XXXIVth Rencontres de Moriond on ElectroWeak Interactions and Unified Theories',
    'venue': 'Les Aarcs',
    'title': 'W cross section and events with leptons and missing p<sub>T</sub> at HERA',
    'slides': None,
    'poster': None,
    'proceedings': "https://drive.google.com/open?id=0B9VL39aSWUqiX0RUOTBfQ1ZQNjg",
  })
  loop.conf_int.append({
    'year': '1998',
    'site': "",
    'name': 'XXIX International Conference on High-Energy Physics',
    'venue': 'Vancouver',
    'title': 'W boson production at HERA',
    'slides': None,
    'poster': None,
    'proceedings': "https://drive.google.com/open?id=0B9VL39aSWUqiQmJuV1NMNk9ZN2c",
  })


  loop.conf_dom = []
  loop.conf_dom.append({
    'year': '2012',
    'site': "http://ilcagenda.linearcollider.org/conferenceOtherViews.py?view=standard&amp;confId=5907",
    'name': 'ILC Tokusui Workshop',
    'venue': 'KEK',
    'title': "LHC physics prospect",
    'slides': "http://ilcagenda.linearcollider.org/getFile.py/access?contribId=3&amp;resId=0&amp;materialId=slides&amp;confId=5907",
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '2012',
    'site': "http://ppwww.phys.sci.kobe-u.ac.jp/TeraScale2012",
    'name': 'Particle physics at TeV scale explored by LHC',
    'venue': 'Kobe University',
    'title': "Latest results from precision tests of SM",
    'slides': "http://ppwww.phys.sci.kobe-u.ac.jp/TeraScale2012/Slide/Matsushita.pdf",
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '2011',
    'site': "",
    'name': 'Review of DAQ system developments',
    'venue': 'Kyoto University',
    'title': "Experience from integration of muon trigger detector and DAQ system at ATLAS",
    'slides': None,
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '2011',
    'site': "",
    'name': 'Physical Society of Japan',
    'venue': 'Hirosaki University',
    'title': "LHC status and Standard Model physics",
    'slides': "http://atlas.kek.jp/sub/documents/jps201109/17aSJ2_matsushita.pdf",
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '2011',
    'site': "",
    'name': 'Physics at TeV scale explored by LHC',
    'venue': 'University of Tokyo',
    'title': "SM results",
    'slides': "",
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '2011',
    'site': "",
    'name': 'Physics Beyond the Standard Model and Predictable Observables',
    'venue': 'Kobe University',
    'title': "W/Z and top at the LHC",
    'slides': "",
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '2010',
    'site': "",
    'name': 'Physics at TeV scale explored by LHC',
    'venue': 'University of Tokyo',
    'title': "Muon performance",
    'slides': "",
    'poster': None,
    'proceedings': "",
  })
  loop.conf_dom.append({
    'year': '1999',
    'site': "",
    'name': 'Physical Society of Japan',
    'venue': 'Hiroshima University',
    'title': "Recent results from HERA/ZEUS",
    'slides': "https://drive.google.com/open?id=0B9VL39aSWUqiQnNTc3hBdV91WEE",
    'poster': None,
    'proceedings': "",
  })


  loop.seminar = []
  loop.seminar.append({
    'year': '2010',
    'site': "",
    'name': '',
    'venue': 'Kobe University',
    'title': "Latest results from ATLAS",
    'slides': None,
    'poster': None,
    'proceedings': "",
  })
  loop.seminar.append({
    'year': '2001',
    'site': "",
    'name': '',
    'venue': 'University of Oxford',
    'title': "Searches beyond the Standard Model at HERA",
    'slides': 'https://drive.google.com/open?id=0B9VL39aSWUqiT2lTelR5MlAtZms',
    'poster': None,
    'proceedings': "",
  })
  loop.seminar.append({
    'year': '2000',
    'site': "",
    'name': '',
    'venue': 'KEK',
    'title': "Optical Alignment System for the ZEUS MicroVertex Detector",
    'slides': 'https://drive.google.com/open?id=0B9VL39aSWUqiR19wck5xT1o0MEk',
    'poster': None,
    'proceedings': "",
  })


  loop.symposium = []
  loop.symposium.append({
    'year': '2011',
    'site': "",
    'name': 'Symposium on EU-Japan Collaboration in Education, Research and Exchanges',
    'venue': 'Brussels',
    'title': "Research in Europe at a Large international Collaboration at CERN",
    'slides': None,
    'poster': None,
    'proceedings': "",
  })


  loop.outreach = []
  loop.outreach.append({
    'year': '2012',
    'site': "",
    'name': 'Lectures at the Japanese Schools of Brussels',
    'venue': 'Brussels',
    'title': "Frontiers of high-energy physics experiments",
    'slides': None,
    'poster': None,
    'proceedings': "",
  })
  return loop


def getPublications(loop):
  loop.pub_cms = []
  loop.pub_cms.append({
    'author': 'T. Matsushita',
    'title': "Flexible trigger menu implementation on the Global Trigger for the CMS Level-1 trigger upgrade",
    'link': "http://iopscience.iop.org/article/10.1088/1742-6596/898/3/032033",
    'ref': "<i>J. Phys.:Conf. Ser.</i> <b>898</b> (2017) 032033"
  })
  loop.pub_cms.append({
    'author': 'T. Matsushita',
    'title': "Implementation of Level-1 trigger algorithms on the upgraded CMS Global Trigger System",
    'link': "https://pos.sissa.it/234/246/",
    'ref': "<i>PoS</i> <b>EPS-HEP</b> (2015) 246"
  })
  loop.pub_cms.append({
    'author': 'T. Matsushita',
    'title': "Software for implementing trigger algorithms on the upgraded CMS Global Trigger System",
    'link': "http://iopscience.iop.org/article/10.1088/1742-6596/664/8/082031",
    'ref': "<i>J. Phys.:Conf Ser.</i> <b>664</b> (2015) 082031",
  })


  loop.pub_atlas = []
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': "A Particle Consistent with the Higgs Boson Observed with the ATLAS Detector at the Large Hadron Collider",
    'link': "https://www.sciencemag.org/content/338/6114/1576.full",
    'ref': "<i>Science</i> <b>338</b> (2012) 1576",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC",
    'link': "http://www.sciencedirect.com/science/article/pii/S037026931200857X",
    'ref': "<i>Phys. Lett.</i> B <b>716</b> (2012) 1",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': 'Search for the Standard Model Higgs boson in the H &rarr; WW<sup>(*)</sup> &rarr; l&nu;l&nu; decay mode with 4.7 fb<sup>-1</sup> of ATLAS data at &radic;<span style="text-decoration: overline">s</span> = 7 TeV',
    'link': "http://www.sciencedirect.com/science/article/pii/S0370269312008477",
    'ref': "<i>Phys. Lett.</i> B <b>716</b> (2012) 62",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': 'Measurement of the WZ production cross section and limits on anomalous triple gauge couplings in proton-proton collisions at &radic;<span style="text-decoration: overline">s</span> = 7 TeV with the ATLAS detector',
    'link': "http://www.sciencedirect.com/science/article/pii/S0370269312001943",
    'ref': "<i>Phys. Lett.</i> B <b>709</b> (2012) 341",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': "Performance of the ATLAS Trigger System in 2010",
    'link': "http://link.springer.com/article/10.1140/epjc/s10052-011-1849-1",
    'ref': "<i>Eur. Phys. J.</i> C <b>72</b> (2012) 1849",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': 'Measurement of the differential cross-sections of inclusive, prompt and non-prompt J/&psi; production in proton-proton collisions at &radic;<span style="text-decoration: overline">s</span> = 7 TeV',
    'link': "http://www.sciencedirect.com/science/article/pii/S0550321311002938",
    'ref': "<i>Nucl. Phys.</i> B <b>850</b> (2011) 387",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': 'Measurement of the W charge asymmetry in the W &rarr; &mu;&nu; decay mode in pp collisions at &radic;<span style="text-decoration: overline">s</span> = 7 TeV with the ATLAS detector',
    'link': "http://www.sciencedirect.com/science/article/pii/S0370269311005302",
    'ref': "<i>Phys. Lett.</i> B <b>701</b> (2011) 31",
  })
  loop.pub_atlas.append({
    'author': 'ATLAS Collaboration',
    'title': 'Measurement of the W charge asymmetry in the W &rarr; &mu;&nu; decay mode in pp collisions at &radic;<span style="text-decoration: overline">s</span> = 7 TeV with the ATLAS detector',
     'title': 'Measurement of the W &rarr; l&nu; and Z/&gamma;<sup>*</sup> &rarr; ll production cross sections in proton-proton collisions at &radic;<span style="text-decoration: overline">s</span> = 7 TeV with the ATLAS detector',
    'link': "http://link.springer.com/article/10.1007/JHEP12%282010%29060",
    'ref': "<i>JHEP</i> <b>12</b> (2010) 060",
  })


  loop.pub_atlas_note = []
  loop.pub_atlas_note.append({
    'author': 'ATLAS Collaboration',
    'title': "Performance of the ATLAS muon trigger in 2011",
    'link': "http://cdsweb.cern.ch/record/1462601/files/ATLAS-CONF-2012-099.pdf",
    'ref': "ATLAS-CONF-2012-099",
  })
  loop.pub_atlas_note.append({
    'author': 'ATLAS Collaboration',
    'title': "A measurement of the muon reconstruction efficiency in 2010 ATLAS data using J/ψ decays",
    'link': "https://cdsweb.cern.ch/record/1474642/files/ATLAS-CONF-2012-125.pdf",
    'ref': "ATLAS-CONF-2012-125"
  })
  loop.pub_atlas_note.append({
    'author': 'ATLAS Collaboration',
    'title': "A measurement of the ATLAS muon reconstruction and trigger efficiency using J/ψ decays",
    'link': "https://cdsweb.cern.ch/record/1336750/files/ATLAS-CONF-2011-021.pdf",
    'ref': "ATLAS-CONF-2011-021"
  })


  loop.pub_mice = []
  loop.pub_mice.append({
    'author': 'M. Ellis, P.R. Hobson, P. Kyberd, J.J. Nebrensky, A. Bross, J. Fagan, T. Fitzpatrick, R. Flores, R. Kubinski, J. Krider, R. Rucinski, P. Rubinov, C. Tolian, T.L. Hart, D.M. Kaplan, W. Luebke, B. Freemire, M. Wojcik, G. Barber, D. Clark, I. Clark, P.J. Dornan, A. Fish, S. Greenwood, R. Hare, A. Jamdagni, V. Kasey, M. Khaleeq, J. Leaver, K.R. Long, E. McKigney, <u>T. Matsushita</u>, C. Rogers, T. Sashalmi, P. Savage, M. Takahashi, A. Tapper, K. Yoshimura, P. Cooke, R. Gamet, H. Sakamoto, Y. Kuno, A. Sato, T. Yano, M. Yoshida, C. MacWaters, L. Coney, G. Hanson, A. Klier, D. Cline, X. Yang, D. Adey',
    'title': "The design, construction and performance of the MICE scintillating fibre trackers",
    'link': "http://www.sciencedirect.com/science/article/pii/S0168900211008126",
    'ref': "<i>Nucl. Instrum. Meth.</i> A <b>659</b> (2011) 136"
  })
  loop.pub_mice.append({
    'author': "T. Matsushita",
    'title': "The MICE scintillating-fibre tracker",
    'link': "",
    'ref': "<i>J. Phys.:Conf. Ser.</i> <b>110</b> (2008) 122016"
  })

  loop.pub_zeus = []
  loop.pub_zeus.append({
    'author': 'A. Polini, I. Brock, S. Goers, A. Kappes, U. F. Katz, E. Hilger, J. Rautenberg, A. Weber, A. Mastroberardino, E. Tassi, V. Adler, L. A. T. Bauerdick, I. Bloch, T. Haas, U. Klein, U. Koetz, G. Kramberger, E. Lobodzinska, R. Mankel, J. Ng, D. Notz, M. C. Petrucci, B. Surrow, G. Watt, C. Youngman, W. Zeuner, C. Coldewey, R. Heller, E. Gallo, T. Carli, V. Chiochia, D. Dannheim, E. Fretwurst, A. Garfagnini, R. Klanner, B. Koppitz, J. Martens, M. Milite, K. Tokushuku, I. Redondo, H. Boterenbrood, E. Koffeman, P. Kooijman, E. Maddox, H. Tiecke, M. Vazquez, J. Velthuis, L. Wiggers, R.C.E. Devenish, M. Dawson, J. Ferrando, G. Grzelak, K. Korcsak-Gorzo, <u>T. Matsushita</u>, K. Oliver, P. Shield, R. Walczak, A. Bertolin, E. Borsato, R. Carlin, F. Dal Corso, A. Longhin, M. Turcato, T. Fusayasu, R. Hori, T. Kohno, S. Shimizu, H. E. Larsen, R. Sacchi, A. Staiano, M. Arneodo, M. Ruspa, J. Butterworth, C. Gwenlan, J. Fraser, D. Hayes, M. Hayes, J. Lane, G. Nixon, M. Postranecky, M. Sutton, M. Warren',
    'title': "The design and performance of the ZEUS Micro Vertex detector",
    'link': "http://www.sciencedirect.com/science/article/pii/S0168900207018499",
    'ref': "<i>Nucl. Instrum. Meth.</i> A <b>581</b> (2007) 656"
  })
  loop.pub_zeus.append({
    'author': 'K. Korcsak-Gorzo, G. Grzelak, K. Oliver, M. Dawson, R. Devenish, J. Ferrando, <u>T. Matsushita</u>, P. Shield and R. Walczak',
    'title': "The Optical alignment system of the ZEUS micro vertex detector",
    'link': "http://www.sciencedirect.com/science/article/pii/S0168900207013009",
    'ref': "<i>Nucl. Instrum. Meth.</i> A <b>580</b> (2007) 1227"
  })
  loop.pub_zeus.append({
    'author': 'ZEUS Collaboration',
    'title': "Search for single-top production in ep collisions at HERA",
    'link': "http://www.sciencedirect.com/science/article/pii/S0370269303003332",
    'ref': "<i>Phys. Lett.</i> B <b>559</b> (2003) 153"
  })
  loop.pub_zeus.append({
    'author': '<u>T. Matsushita</u>, S. Boogert, R. Devenish and R. Walczak',
    'title': "Optical alignment system for the ZEUS micro vertex detector",
    'link': "http://www.sciencedirect.com/science/article/pii/S0168900201005939",
    'ref': "<i>Nucl. Instrum. Meth.</i> A <b>466</b> (2001) 383"
  })
  loop.pub_zeus.append({
    'author': 'ZEUS Collaboration',
    'title': "W production and the search for events with an isolated high-energy lepton and missing transverse momentum at HERA",
    'link': "http://www.sciencedirect.com/science/article/pii/S0370269399013581",
    'ref': "<i>Phys. Lett.</i> B <b>471</b> (2000) 411"
  })
  loop.pub_zeus.append({
    'author': 'C. Diaconu, J. Kalinowski, <u>T. Matsushita</u>, H. Spiesberger and D. S. Waters',
    'title': "High p<sub>T</sub> Leptons and W production at HERA",
    'link': "http://iopscience.iop.org/0954-3899/25/7/318",
    'ref': "<i>J. Phys.</i> G <b>25</b> (1999) 1412"
  })
  loop.pub_zeus.append({
    'author': '<u>T. Matsushita</u>, E. Perez and R. Ruckl',
    'title': "High Q<sup>2</sup> Physics at HERA and Searches for New Particles",
    'link': "http://iopscience.iop.org/0954-3899/25/7/319",
    'ref': "<i>J. Phys.</i> G <b>25</b> (1999) 1418"
  })
  loop.pub_zeus.append({
    'author': 'T. Kon, <u>T. Matsushita</u> and T. Kobayashi',
    'title': "Possible excess in charged current events with high-Q<sup>2</sup> at HERA from stop and sbottom production",
    'link': "http://www.worldscientific.com/doi/abs/10.1142/S0217732397003265",
    'ref': "<i>Mod. Phys. Lett.</i> A <b>12</b> (1997) 3143"
  })


  loop.pub_rad = []
  loop.pub_rad.append({
    'author': '<u>T. Matsushita</u>, C. Fukunaga, H. Ikeda and Y. Saitoh',
    'title': "Total-dose effects of γ-ray irradiation on SOI-MOS transistors",
    'link': "http://www.sciencedirect.com/science/article/pii/0168900295006249",
    'ref': "<i>Nucl. Instrum. Meth.</i> A <b>366</b> (1995) 366"
  })
  loop.pub_rad.append({
    'author': '<u>T. Matsushita</u>, C. Fukunaga, H. Ikeda and Y. Saitoh',
    'title': "Radiation susceptivity of a non-radiation-hard 1.2μm CMOS transistors",
    'link': "http://www.sciencedirect.com/science/article/pii/0168900294911649",
    'ref': "<i>Nucl. Instrum. Meth.</i> A <b>350</b> (1994) 199"
  })


  loop.pub_books = []
  loop.pub_books.append({
    'author': 'T. Suginaka, <u>T. Matsushita</u>, K. Nishimura, K. Onishi, T. Unemura, E. Yamada, H. Zhang, T. Kobayashi',
    'title': "Numerical computation with Advance/FrontFlow/red", 
    'link': "",
    'ref': "AdvanceSoft, ISBN-10: 4990214331 (Japanese)"
  })

  return loop

# eof
