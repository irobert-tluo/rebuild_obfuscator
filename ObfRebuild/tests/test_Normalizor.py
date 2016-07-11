from ObfRebuild import Normalizor
import sys, os

norm = Normalizor()
page = open(sys.argv[1], "r").read()
print norm.normalize(page)
