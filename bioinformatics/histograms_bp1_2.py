# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:55:59 2017

@author: sap21
"""

from goldilocks import Goldilocks
from goldilocks.strategies import GCRatioStrategy

#FIGURE 1
sequence_data = {
    "bp_v1": {"file": "/home/samantha/Bioinformatics/bp_v1/BP_v1.fasta.fai"}
}
g = Goldilocks(GCRatioStrategy(), sequence_data, is_faidx=True,
               length="500", stride="500")
g.plot(bins=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
       title="GC Content Profile of bp_v1"
)
#FIGURE 2
sequence_data = {
    "bp_v2": {"file": "/home/samantha/Bioinformatics/bp_v2/BP_v2.fasta.fai"}
}
g = Goldilocks(GCRatioStrategy(), sequence_data, is_faidx=True,
               length="500", stride="500")
g.plot(bins=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
       title="GC Content Profile of bp_v2"
)