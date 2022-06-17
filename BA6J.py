###6J   radi
def TwoBreakOnGenomeGraph(g,i1,i2,j1,j2):
  g.remove((i1,i2))
  g.remove((j1,j2))
  g.append((i1,j1))
  g.append((i2,j2))
  return g