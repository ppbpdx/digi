import os
import json

path = 'projects'
project_list = []
output_dict= {}

jsonfile_list = [f for f in os.listdir(path)]

for file in jsonfile_list:
    file_path = f'{path}/{file}'
    file = json.load(open(file_path))
    file['label'] = file.pop('project')
    file['image'] = file.pop('logoURL')
    project_list.append(file)
    
    
output_dict['elements'] = project_list
output_file = 'map.json'
with open(output_file, 'w') as f:
    json.dump(output_dict, f)
