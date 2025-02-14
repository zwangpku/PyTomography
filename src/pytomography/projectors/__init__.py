r"""This module contains classes/functionality for operators that map between distinct vector spaces. One (very important) operator of this form is the system matrix :math:`H:\mathbb{U} \to \mathbb{V}`, which maps from object space :math:`\mathbb{U}` to image space :math:`\mathbb{V}`"""
from .system_matrix import SystemMatrix
from .SPECT import SPECTSystemMatrix, SPECTSystemMatrixMaskedSegments
from .shared import KEMSystemMatrix