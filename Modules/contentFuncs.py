import numpy as np
import sympy as smp
from pathlib import Path

def createBeginItem():
    beginString = r"\begin{itemize}"
    return beginString

def createEndItem():
    beginString = r"\end{itemize}"
    return beginString

def createItem(parameterValue,nameParameter,symbolParameter,stringUnitParameter):
    itemString = r"\item " + nameParameter + r": $" + symbolParameter + r" = \SI{" + parameterValue + r"}{" + "\\" + stringUnitParameter + r"}$"
    return itemString

def createSectionOpener(sectionName,text):
    opener = r"\section{" + sectionName + "}"
    fullSection = opener + text
    return fullSection

def createEndDocument():
    end = r"\end{document}"
    return end

def createBeginEquation():
    eq = r"\begin{equation}"
    return eq

def createEndEquation():
    eq = r"\end{equation}"
    return eq
