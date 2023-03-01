import json
import os
from sklearn.metrics import cohen_kappa_score

dir_list = os.listdir('AnnotationOutput_annotator_KN/')
# dir_list = ['2022.11.30_22.25.56.json']
cohen_avg = 0
relation_array1 = ['Left (Object based)', 'Left (Camera based)', 'Behind (Object based)', 'Behind (Camera based)', 'Across', 'Above']
relation_array2 = ['Right (Object based)', 'Right (Camera based)', 'Front (Object based)', 'Front (Camera based)', 'Along', 'Below']

for r in range(len(relation_array1)):
     relation1 = relation_array1[r]
     relation2 = relation_array2[r]
     # print(relation_array1[r])
     for i in dir_list:
          # print(i)
          p1 = 'AnnotationOutput_annotator_KN/' + i
          p2 = 'AnnotationOutput_annotator_RS/' + i

          relation_dict = {}
          relation_dict2 = {}

          with open(p1, 'r', encoding="utf_8_sig") as fcc_file:
               fcc_data = json.load(fcc_file)
               for rel_pair in fcc_data["AnotationResults"]:
                    obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
                    for anno in rel_pair['Anotations']:
                         key = str([obj1, obj2])
                         if key in relation_dict.keys():
                              relation_dict[key].append(anno)
                         else:
                              relation_dict[key] = [anno]

          with open(p2, 'r', encoding="utf_8_sig") as fcc_file:
               fcc_data = json.load(fcc_file)
               for rel_pair in fcc_data["AnotationResults"]:
                    obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
                    for anno in rel_pair['Anotations']:
                         key = str([obj1, obj2])
                         if key in relation_dict2.keys():
                              relation_dict2[key].append(anno)
                         else:
                              relation_dict2[key] = [anno]

          rater1 = []
          rater2 = []
          
          merge_dict = relation_dict | relation_dict2

          for key in merge_dict.keys():
               if key in relation_dict.keys() and key in relation_dict2.keys():
                    # print(key, relation_dict[key], relation_dict2[key])
                    set_rels1 = set(relation_dict[key])
                    set_rels2 = set(relation_dict2[key])
                    
                    if relation1 in set_rels1:
                         if relation1 in set_rels2:
                              rater1 = rater1 + [1]
                              rater2 = rater2 + [1]
                         elif relation2 in set_rels2:
                              rater1 = rater1 + [1]
                              rater2 = rater2 + [0]
                    if relation2 in set_rels1:
                         if relation2 in set_rels2:
                              rater1 = rater1 + [0]
                              rater2 = rater2 + [0]
                         elif relation1 in set_rels2:
                              rater1 = rater1 + [0]
                              rater2 = rater2 + [1]
                    # print(rater1)
                    # print(rater2)  
          if rater1 != [] and rater1 == rater2:
               cohen_avg += cohen_kappa_score(rater1, rater2)

     cohen_avg = cohen_avg/len(dir_list) 
     print(cohen_avg, len(dir_list))
     print("#####################")
     r = r+1






