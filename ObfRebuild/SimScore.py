import editdistance, math

def similarity(a1, b1):
  max_len = max([len(a1), len(b1)])
  if max_len == 0:
      return 0
  dist = editdistance.eval(a1, b1)
  return 1.0 - (float(dist)/float(max_len))

