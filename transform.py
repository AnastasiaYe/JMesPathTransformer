import re
import jmespath as jp
import json

#flatten the input document to avoid nested dictionary
def flatten(input):
    out_list = []
    def traverse(pref, tree):
        if pref:
            pref += '.'
        for key in tree.keys():
            if not isinstance(tree[key],dict):
                out_list.append({
                    'key': pref + key,
                    'value': tree[key]
                })
                continue
            traverse(pref+key, tree[key])
    traverse('',input)
    return out_list

#Determines that a string value is a JmesPath if it ends with "$path"
def isJmesPathString(value):
    if isinstance(value,str) and re.search(r"\$path$", value):
        return True
    return False

#Performs a JmesPath query
def jmesPathValue(input,file):
    return jp.search(input, file)

#A JMESPath-based template function
#Transform an input Json file to an optimiazed format regarding the template

def transform(inputFileName, template):
    with open(inputFileName) as json_file:
        inputJson = json.load(json_file)

    with open(template) as json_file:
        out_data = json.load(json_file)

    temp = flatten(out_data)

    for dict in temp:
        if isJmesPathString(dict['key']):
            value = jmesPathValue(dict['value'],inputJson)
            index = dict['key'].split('.')
            this_dict = out_data
            i = 0
            while i < len(index)-2:
                this_dict = this_dict[index[i]]
                i += 1
            this_dict[index[-2]] = value

    j = json.dumps(out_data)

    with open('output.json', 'w') as f:
        f.write(j)



#testing

transform('input.json','template.json')
