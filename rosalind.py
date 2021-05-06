"""
Usage of Mr. Bergamini's code from Week 04 Lecture Materials
"""

__author__ = 'Var Kurapati, vkurapat@ucsc.edu'

from aminomass import aminofile

class Protein:

  """ Represents an immutable sequence of amino acids. """

  def __init__(self, aminos=None):
    self._aminos = list(aminos) if aminos else []
    if any(base not in 'GALMFWKQUESPVICYHRNDT' for base in self._aminos):
      raise ValueError('Illegal characters in Aminos')
    pass

  def __add__(self, addition):
    return Protein(self._aminos + list(addition))
    pass

  def __eq__(self, other):
    if isinstance(other, Protein):
      return self._aminos == other._aminos
    else:
      return self._aminos == list(other)
    pass

  def __getitem__(self, key):
    if isinstance(key, slice):
      return Protein(self._aminos[key])
    else:
      return self._aminos[key]
    pass

  def __len__(self):
    return len(self._aminos)
    pass

  def __repr__(self):
    return f"Protein('{self}')"
    pass

  def __str__(self):
    return ''.join(self._aminos)
    pass

  def mass(self):
    sum = 0
    a_mass = aminofile()
    for i in self._aminos:
      for j in a_mass:
        if i == j:
          sum += a_mass[j]
    return sum
    pass
