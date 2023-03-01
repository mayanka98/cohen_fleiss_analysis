import json
import os
from sklearn.metrics import cohen_kappa_score

dir_path = 'AnnotationOutput_annotator_RS/'
dir_list = os.listdir(dir_path)

for i in dir_list:
     print(i)
     count = 0
     relation_dict = {}

     with open(dir_path + i, 'r', encoding="utf_8_sig") as fcc_file:
          fcc_data = json.load(fcc_file)
          for rel_pair in fcc_data["AnotationResults"]:
               obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
               for anno in rel_pair['Anotations']:
                    key = str([obj1, obj2])
                    if key in relation_dict.keys():
                         relation_dict[key].append(anno)
                    else:
                         relation_dict[key] = [anno]

     for key in relation_dict.keys():
          set_rels = set(relation_dict[key])
          # print(key, set_rels)
          if 'Above' in set_rels and 'Below' in set_rels:
               count = count+1
          if 'Across' in set_rels and 'Along' in set_rels:
               count = count+1
          if 'Behind (Camera based)' in set_rels and 'Front (Camera based)' in set_rels:
               count = count+1
          if 'Behind (Object based)' in set_rels and 'Front (Object based)' in set_rels:
               count = count+1
          if 'Left (Camera based)' in set_rels and 'Right (Camera based)' in set_rels:
               count = count+1
          if 'Left (Object based)' in set_rels and 'Right (Object based)' in set_rels:
               count = count+1
          
     percent_wrong_rels = count * 100 / len(relation_dict)
     print(percent_wrong_rels)
     print("##########################")




