import os
import xml.etree.ElementTree as ET

rootDir = 'yourdir'
count = 0
done = []
for dirName, subdirList, fileList in os.walk(rootDir):
    for fl in fileList:
        if 'simflofy-connector' in fl and '.xml' in fl and 'test' not in fl and fl not in done:
            print fl
            tree = ET.parse(dirName + '/' + fl)
            for beans in tree.getroot():
                clazz = beans.get('class', '')
                if clazz != '' and clazz not in done:

                    if beans.get('id','') != '':
                        beanid = beans.get('id')
                        print '@Component("'+beanid+'")'
                    mb = ''
                    nm = ''
                    dsc = ''
                    ios = ''
                    irs = ''
                    isAuth = 'Auth' in clazz
                    isCS = 'Content' in clazz
                    isSearch = 'Search' in clazz
                    hashelper = False
                    for prop in list(beans):
                        if prop.attrib['name'] == 'messageBase':
                            mb = prop.attrib['value'][0].lower() + prop.attrib['value'][1:]
                        elif prop.attrib['name'] == 'name':
                            nm = prop.attrib['value']
                        elif prop.attrib['name'] == 'description':
                            dsc = prop.attrib['value']
                        elif prop.attrib['name'] == 'isOutputSupported':
                            ios = prop.attrib['value']
                        elif prop.attrib['name'] == 'isRepositorySupported':
                            irs = prop.attrib['value']
                        elif prop.attrib['name'] == 'helper':
                            hashelper = True
                    if mb != '':
                        print
                        print '@Autowired'
                        if hashelper:
                            print 'public ' + clazz.split('.')[-1] + '(OutputHelper helper){'
                        else:
                            print 'public ' + clazz.split('.')[-1] + '(){'
                        print '\tsetMessageBase("' + mb + '");'
                        if isAuth:
                            print '\tsetDescription(getMessage("authDesc"));'
                        elif isSearch:
                            print '\tsetName(getMessage("searchName"));'
                            print '\tsetDescription(getMessage("searchDesc"));'
                        elif isCS:
                            print '\tsetName(getMessage("csName"));'
                            print '\tsetDescription(getMessage("csDesc"));'
                        else:
                            print '\tsetName(getMessage("connName"));'
                            print '\tsetDescription(getMessage("connDesc"));'
                        if ios != '' and ios == "false":
                            print '\tsetIsOutputSupported(false);'
                        if irs != '' and irs == "false":
                            print '\tsetIsRepositorySupported(false);'
                        if hashelper:
                            print '\tthis.helper = helper;'
                        print '}'
                        if nm != '' or dsc != '':
                            if isAuth:
                                print mb + '.authDesc=' + dsc
                            elif isSearch:
                                print mb + '.searchName=' + nm
                                print mb + '.searchDesc=' + dsc
                            elif isCS:
                                print mb + '.csName=' + nm
                                print mb + '.csDesc=' + dsc
                            else:
                                print mb+'.connName='+nm
                                print mb+'.connDesc='+dsc
                        print
            done.append(fl)
