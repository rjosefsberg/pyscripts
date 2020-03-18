import json
wi = []
wd = []
boot = {}
with open('somejson.json', 'r') as f:
    data = json.load(f)
    for i in data['WidgetDefinitions']:
        if i:
            base = 'bootstrap.widget.' + i['widgetId'].lower()
            dk = base + '.d'
            if len(i['customFields']) > 0:
                for cf in i['customFields']:
                    fk = base+'.field.'+ cf['fieldName']
                    cf['description'] = fk
            i['description']=dk
            wd.append(i)
    boot['WidgetDefinitions'] = wd



    for i in data['WidgetInstances']:
        if i:
            base = 'bootstrap.wi.' + i['widgetInstanceId'].lower()
            i['name'] = base + '.name'
            i['label'] = base+'.label'
            wi.append(i)
    boot['WidgetInstances'] = wi

with open('/Users/ryan/Utility/convert/nuboot.json', 'w') as b:
    json.dump(boot,b)
