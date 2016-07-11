import operator, editdistance, math

class Util:
    @staticmethod
    def distinct(samples):
        noDupes = {}
        for i in samples:
            if not i["encoded"] in noDupes:
                noDupes[i["encoded"]]=i
        return noDupes.keys()

    @staticmethod
    def sort_by_date(self, data_set):
        sorted(data_set, key=lambda k: k['date'])

    @staticmethod
    def simscore(a1, b1):
        max_len = max([len(a1), len(b1)])
        if max_len == 0:
            return 0
        dist = editdistance.eval(a1, b1)
        return 1.0 - (float(dist)/float(max_len))

    @staticmethod
    def groupmap_to_data(grp_map, data_set):
        return filter(lambda d: d["id"] in grp_map, data_set)

class Variant:
    def cluster(self, data_set, threshold):
        prev_map = {}
        grp_id = 0
        for index in range(len(data_set)):
            sample = data_set[index]
            print sample["id"]
            scores = {prev["id"] : Util.simscore(sample["encoded"], prev["encoded"]) for prev in data_set[:index]}
            if len(scores) > 0 and max(scores.values()) > threshold:
              closest = max(scores.iteritems(), key=operator.itemgetter(1))[0]
              print "Closet:", closest
              cur_grp_id = prev_map[closest]
            else:
              grp_id += 1
              cur_grp_id = grp_id
            prev_map[sample["id"]] = cur_grp_id
        grp_info = {}
        for sid, gid in prev_map.iteritems():
            if gid not in grp_info:
                grp_info[gid] = []
            grp_info[gid].append(sid)
        return grp_info

    def pretty_print_grp(self, grp_map):
        for gid, gdata in grp_map.iteritems():
            print gid, "\n\t", gdata

class Version:
    def cluster(self, data_set, threshold):
        grp_map = {}
        grp_id = 0
        for index in range(len(data_set)):
            sample = data_set[index]
            print sample["id"]
            scores = {}
            for prev_grp_id, prev_grp_data in grp_map.iteritems():
              scores[prev_grp_id] = min([Util.simscore(sample["encoded"], prev["encoded"]) for prev in prev_grp_data])
            if len(scores) == 0 or max(scores.values()) < threshold:
                grp_id += 1
                cur_grp_id = grp_id
                grp_map[cur_grp_id] = []
            else:
                cur_grp_id = max(scores.iteritems(), key=operator.itemgetter(1))[0]
                print "Closet:", cur_grp_id
            grp_map[cur_grp_id].append(sample)
        grp_info = {}
        for prev_grp_id, prev_grp_data in grp_map.iteritems():
            grp_info[prev_grp_id] = [prev["id"] for prev in prev_grp_data]
        return grp_info 
