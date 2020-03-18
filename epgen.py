eplisttemplate = 'List<EditPropertyOption> {} = new ArrayList<>();\n'
epoptiontemplate = 'EditPropertyOption {} = new EditPropertyOption("{}","{}");\n'
eplistadd = '{}.add({});\n'
eptemplatesimple = 'editPropertyCollection.addEditProperty(new EditProperty({},Messages.getString({}),docSpec.optString({},""),EditPropertyType.TEXT));\n'  # id,displayName,value,type
eptemplatemulti = 'editPropertyCollection.addEditProperty(new EditProperty({},Messages.getString({}),docSpec.optString({},""),{});\n'  # id,displayName,value,options
posttemplate = 'docSpec.put({}, parameterObject.optString({},""));\n\n'


def make_ep(tup, epfile):
    with open(epfile, 'a') as f:
        if tup[3] is True:
            options = tup[4]
            lname = tup[0] + "List"
            ldec = eplisttemplate.format(lname)
            f.write(ldec)
            for option in options:
                oname = str(option[0]) + 'Option'
                odec = epoptiontemplate.format(oname, str(option[1]), str(option[0]))
                f.write(odec)
                addec = eplistadd.format(lname, oname)
                f.write(addec)
            ep = eptemplatemulti.format(str(tup[2]), str(tup[1]), str(tup[2]), str(lname))
            f.write(ep)
        else:
            ep = eptemplatesimple.format(str(tup[2]), str(tup[1]), str(tup[2]))
            f.write(ep)
        f.write('\n')


def makepost(tup, pfile):
    with open(pfile, 'a') as f:
        param = str(tup[2])
        p = posttemplate.format(param, param)
        f.write(p)
