import json
import os
from sklearn.metrics import cohen_kappa_score

dir_list = os.listdir('AnnotationOutput_annotator_KN/')
# dir_list = ['2022.11.30_22.25.56.json']
cohen_avg = 0
# print(dir_list)
for i in dir_list:
     print(i)
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

     print(len(relation_dict))
     print(len(relation_dict2))
     print("################################")

     rater1 = []
     rater2 = []
     num_rels = 0
     
     merge_dict = relation_dict | relation_dict2
     print(len(merge_dict))
     for key in merge_dict.keys():
          num_rels = num_rels+1
          if key in relation_dict.keys() and key in relation_dict2.keys():
               print(key, relation_dict[key], relation_dict2[key])
               set_rels1 = set(relation_dict[key])
               set_rels2 = set(relation_dict2[key])
               intersection = list(set_rels1 & set_rels2)
               if len(set_rels1) >= len(set_rels2):
                    rater1 = rater1 + [1]*len(set_rels1)
                    rater2 = rater2 + [1]*len(intersection) + [0]*(len(set_rels1) - len(intersection))
               else:
                    rater2 = rater2 + [1]*len(set_rels2)
                    rater1 = rater1 + [1]*len(intersection) + [0]*(len(set_rels2) - len(intersection))
               print(rater1)
               print(rater2)  
               # print(cohen_kappa_score(rater1, rater2))
          elif key in relation_dict.keys() and not key in relation_dict2.keys():
               print(key, relation_dict[key], "NA")
               set_rels1 = set(relation_dict[key])
               rater1 = rater1 + [1]*len(set_rels1)
               rater2 = rater2 + [0]*len(set_rels1)
               print(rater1)
               print(rater2) 
          elif key in relation_dict2.keys() and not key in relation_dict.keys():               
               print(key, "NA", relation_dict2[key])
               set_rels2 = set(relation_dict2[key])
               rater2 = rater2 + [1]*len(set_rels2)
               rater1 = rater1 + [0]*len(set_rels2)
               print(rater1)
               print(rater2)

     cohen_avg += cohen_kappa_score(rater1, rater2)
     print(num_rels)
# print(len(dir_list))
cohen_avg = cohen_avg/len(dir_list) 
print(cohen_avg)






