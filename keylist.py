from bs4 import BeautifulSoup
from epgen import make_ep as ep
from epgen import makepost as pp
lines = []
k = {}
tuples = []
multi = {}
consttemplate = 'public static final String {}_LABEL = {};'
paramfile = "CSVParams.txt"
configname = "CSVConfig."
fin = "/Users/ryan/Utility/convert/done/CSVeps.txt"
finp = "/Users/ryan/Utility/convert/done/CSVpost.txt"
with open('/Users/ryan/Utility/convert/csv.html', 'r') as f:
    data = f.read().replace('\n', '')
    soup = BeautifulSoup(data, 'html.parser')
    for inp in soup.select('.col.s12 .row .col.s12'):
        if inp.input is not None:
            value = inp.input['value'].replace("$Encoder.attributeEscape($", '').replace(')', '')
            inid = inp.input['id']
        elif inp.textarea is not None:
            value = inp.input['value'].replace("$Encoder.attributeEscape($", '').replace(')', '')
            inid = inp.input['id']
        elif inp.select is not None:
            inid = inp.select('select')[0]['id']
            value = inid.upper()
            oplist = []
            for opt in inp.find_all('option'):
                oplist.append((opt['value'], opt.contents[0]))
            multi[value] = oplist
        if inp.label.contents[0].find('$Encoder') > -1:
            label = inp.label.contents[0].strip().replace("\'", "\"").replace(
                '$Encoder.bodyEscape($ResourceBundle.getString(', "").replace("))", "")
        else:
            label = inp.label.contents[0]
        con = consttemplate.format(value,label.strip())
        lines.append(con)
        k[inid] = value
    fname = f.name.split('/')[-1].replace(".html", "_labels.txt")

    with open('/Users/ryan/Utility/convert/done/' + fname, 'w+') as wr:
        for line in lines:
            wr.write(line + "\n")

with open('/Users/ryan/Utility/convert/CSVParams.txt', 'r') as f:
    data = f.readlines()
    for key, val in k.iteritems():
        for line in data:
            if line.strip() and line.find(key) > -1:
                try:
                    param = line[line.index('PARAM'):line.rfind('=') - 1]
                    if val in multi.keys():
                        tuples.append((key,configname+val+"_LABEL", configname+param, True, multi[val]))
                    else:
                        tuples.append((key,configname+val+"_LABEL", configname+param, False))
                except:
                    print line

for tup in tuples:
    print tup
    ep(tup,fin)

for tup in tuples:
    pp(tup,finp)
