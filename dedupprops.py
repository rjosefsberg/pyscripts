import ConfigParser

config = ConfigParser.RawConfigParser()
config.optionxform = str
config.read('apropfile')
props = []
dprops = []
fprops = {}
nprops = []
gprops = []
for item in config.items('all'):
    props.append(item[0].split('.')[1])

props.sort()

for p in props:
    pp = "general." + p
    pp += '=' + config.get('all',pp)
    print pp

# for p in props:
#     if props.count(p) > 1:
#         dprops.append(p)
#
# dprops = set(dprops)
#
# for item in config.items('all'):
#     if item[1] in dprops:
#         s = item[0].split('.')[1]
#         res = s[0].lower() + s[1:]
#         nk = "General." + res + '=' + item[1]
#         if nk.lower() not in (gp.lower() for gp in gprops):
#             gprops.append(nk)
#
# for g in gprops:
#     print g
