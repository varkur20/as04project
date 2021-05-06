def aminofile():
  dictTable = {}
  with open("/srv/datasets/amino-monoisotopic-mass", "r") as m:
    for line in m:
      (key, val) = line.split()
      dictTable[key] = float(val)
    return dictTable
