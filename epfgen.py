import glob

file = "/Users/ryan/projects/simflofy-3/connectors/simflofy-jira/src/main/java/com/simflofy/connectors/jira/objects/*"
addText = 'epf.addTextEP({},{},"",{});'
addCheck = 'epf.addCheckEP({},{},false,{});'
addLong =  'epf.addLongEP({},{},0L,{});'
addDT = 'epf.addDateTimeEP({},{},{});'
descs=[]
for fl in glob.glob(file):
    print fl
    with open(fl,"r+") as f:
        data = f.readlines()
        print 'EditPropertyFactory epf = new EditPropertyFactory();'
        for line in data:
            if "fields.add(" in line.replace("\n",''):
                psplit = line.split("(")
                stuff = psplit[2].split(',')
                id = stuff[0]
                dis = stuff[1]
                des = stuff[4]
                base = ''
                if stuff[3].endswith("TEXT"):
                    base = addText
                elif stuff[3].endswith("CHECKBOX"):
                    base = addCheck
                elif stuff[3].endswith("LONG"):
                    base = addLong
                elif stuff[3].endswith("DATETIME"):
                    base = addDT
                print base.format(id,dis,des)
        print 'this.fields.addAll(epf.getEpList());'

