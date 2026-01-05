from HC_Assignment5_SatDesign import *
import repDoc.docCreator as doc
from pathlib import Path

docContent = [] # Vector donde se agrega el contenido
tex_file = Path("C:\\Users\\ELC\\Documents\\ModulesEL\\repDoc\\TestsScripts\\report3Test.tex")

########### --------------------------------------------------------------------------------------------- #########
contentStarter =  r"""
\documentclass[a4paper,11pt]{article}

% ---------- Packages ----------
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath, amssymb}
\usepackage{siunitx}
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs}
\usepackage{hyperref}

% ---------- Formatting ----------
\setlength{\parskip}{1em}
\setlength{\parindent}{0pt}

% ---------- Title ----------
"""
docContent.append(contentStarter)

########### --------------------------------------------------------------------------------------------- #########

contentTitle = r"""
\title{Assignment 5: Sizing of a Spacecraft}
"""
docContent.append(contentTitle)

########### --------------------------------------------------------------------------------------------- #########

contentIntroA = r"""
\author{Eduardo López}
\date{\today}

\begin{document}

\maketitle

"""
docContent.append(contentIntroA)

########### --------------------------------------------------------------------------------------------- #########

textForSection1 = r"""
A communications satellite is being launched using a Delta IV launcher. The satellite can be modeled as a point mass
on top of a thin walled cylinder with the following parameters:    
"""
    
contentSection1 = doc.createSectionOpener("Context",textForSection1)
docContent.append(contentSection1)

########### --------------------------------------------------------------------------------------------- #########

contentSection1 = doc.createSectionOpener("Given Data","")
docContent.append(contentSection1)

########### --------------------------------------------------------------------------------------------- #########

contentItems1Begin = doc.createBeginItem()
contentItems1_1 = doc.createItem(stringVarMassSatellite, 'Mass', 'm', 'kg')
contentItems1_2 = doc.createItem(stringVarDiameterSatellite, 'Diameter', 'd', 'm')
contentItems1_3 = doc.createItem(stringVarHeightSatellite, 'Height', 'L', 'm')
contentItems1End = doc.createEndItem()

docContent.append(contentItems1Begin)
docContent.append(contentItems1_1)
docContent.append(contentItems1_2)
docContent.append(contentItems1_3)
docContent.append(contentItems1End)

########### --------------------------------------------------------------------------------------------- #########

textForSection2 = r"""
The communications satellite is made of aluminum which properties are:   
"""
    
contentSection2 = doc.createSectionOpener("Material Properties",textForSection2)
docContent.append(contentSection2)

########### --------------------------------------------------------------------------------------------- #########

contentItems2Begin = doc.createBeginItem()
contentItems2_1 = doc.createItem(stringVarMaterialESatellite, "Young's Modulus", 'E', 'GPa')
contentItems2_2 = doc.createItem(stringVarMaterialStressUltSatellite, 'Ultimate Stress', '\sigma_ult', 'MPa')
contentItems2End = doc.createEndItem()

docContent.append(contentItems2Begin)
docContent.append(contentItems2_1)
docContent.append(contentItems2_2)
docContent.append(contentItems2End)

########### --------------------------------------------------------------------------------------------- #########

textForSection3 = r"""
The natural frequency of a mass-spring system model is dictated by: 
"""
    
contentSection3 = doc.createSectionOpener("Mathematical Model",textForSection3)
docContent.append(contentSection3)



########### --------------------------------------------------------------------------------------------- #########

contentEq1Begin = doc.createBeginEquation()
expEquation1 = r"f_n = \frac{1}{2\pi}\sqrt{\frac{k}{M}}"
contentEq1End = doc.createEndEquation()

contentEq1Explanation = r"""
Where:
\begin{itemize}
    \item $f_n$ is the natural frequency
    \item $k$ is the system stiffness
\end{itemize}

For the axial loading case, the stiffness is dictated by:
"""

docContent.append(contentEq1Begin)
docContent.append(expEquation1)
docContent.append(contentEq1End)
docContent.append(contentEq1Explanation)
########### --------------------------------------------------------------------------------------------- #########

contentEq2Begin = doc.createBeginEquation()
expEquation2 = r"f_n = \frac{1}{2\pi}\sqrt{\frac{k}{M}}"
contentEq2End = doc.createEndEquation()




########### --------------------------------------------------------------------------------------------- #########
contentEnd = doc.createEndDocument()
docContent.append(contentEnd)

report_content = ""
for content in docContent:
    report_content += content


# Write LaTeX file
tex_file.write_text(report_content, encoding="utf-8")

print("report.tex generated successfully.")
