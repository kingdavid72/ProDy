# -*- coding: utf-8 -*-
# ProDy: A Python Package for Protein Dynamics Analysis
# 
# Copyright (C) 2010-2012 Ahmet Bakan
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

"""This module contains features for analyzing protein sequences. 

MSA IO
======

  * :func:`.parseMSA` - parse MSA files
  * :class:`.MSAFile` - read/write MSA files in FASTA/SELEX/Stockholm formats
  * :class:`.MSA` - manipulate MSA in memory
  
Analysis
========

  * :func:`.refineMSA` - refine MSA by removing gapped columns and/or sequences
  * :func:`.calcShannonEntropy` - calculate Shannon entropy
  * :func:`.calcMSAOccupancy` - calculate row (sequence) or column occupancy
  * :func:`.buildMutinfoMatrix` - build mutual information matrix

"""

__author__ = 'Ahmet Bakan'
__copyright__ = 'Copyright (C) 2010-2012 Ahmet Bakan'

__all__ = []

import msa
from msa import *
__all__.extend(msa.__all__)

import msafile
from msafile import *
__all__.extend(msafile.__all__)

import analysis
from analysis import *
__all__.extend(analysis.__all__)

import plotting
from plotting import *
__all__.extend(plotting.__all__)