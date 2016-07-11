import sys, os
import ObfRebuild

folder = sys.argv[1]
data_set = []
inputs = [i for i in os.listdir(folder) if (not i.startswith("s-")) and (not i.startswith(".DS_Store")) ]
for i in inputs:
  with open(os.path.join(folder, i), "r") as myfile:
    data = {'id': i, "date": "", "page": myfile.read(), "encoded": ""}
    data_set.append(data)

#data_set = data_set[:40]
print "Load Total Samples:", len(data_set)

norm = ObfRebuild.Normalizor()
for sample in data_set:
  sample["encoded"] = norm.normalize(sample["page"])

uniques = ObfRebuild.Util.distinct(data_set)
print "Unique Normalized Sample:", len(uniques)

var_cluster = ObfRebuild.Variant()
variants = var_cluster.cluster(uniques, 0.5)
var_cluster.pretty_print_grp(variants)

# Finer_grained Variant SubVersion Clustering
group1_data = ObfRebuild.Util.groupmap_to_data(variants[1], uniques)

ver_cluster = ObfRebuild.Version()
versions = ver_cluster.cluster(group1_data, 0.9)
ver_cluster.pretty_print_grp(versions)
