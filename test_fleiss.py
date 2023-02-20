import json

# Adapted from https://gist.github.com/ShinNoNoir/4749548
def fleiss_kappa(ratings, n):
    '''
    Computes the Fleiss' kappa measure for assessing the reliability of 
    agreement between a fixed number n of raters when assigning categorical
    ratings to a number of items.
    
    Args:
        ratings: a list of (item, category)-ratings
        n: number of raters
        k: number of categories
    Returns:
        the Fleiss' kappa score
    
    See also:
        http://en.wikipedia.org/wiki/Fleiss'_kappa
    '''
    items = set()
    categories = set()
    n_ij = {}
    
    for i, c in ratings:
        items.add(i)
        categories.add(c)
        n_ij[(i,c)] = n_ij.get((i,c), 0) + 1
    
    N = len(items)
    
    p_j = dict(((c, sum(n_ij.get((i, c), 0) for i in items) / (1.0 * n * N)) for c in categories))
    P_i = dict(((i, (sum(n_ij.get((i, c), 0) ** 2 for c in categories) - n) / (n * (n - 1.0))) for i in items))

    P_bar = sum(P_i.values()) / (1.0 * N)
    P_e_bar = sum(value ** 2 for value in p_j.values())
    
    kappa = (P_bar - P_e_bar) / (1 - P_e_bar)
    
    return kappa



relation_dict = {}

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator1.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1

#             else:
#                 relation_dict[key] = 1

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator1.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1

#             else:
#                 relation_dict[key] = 1
 

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator2.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator2.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1


# with open('AnnotationOutput/2022.11.30_22.40.11_annotator3.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1


# with open('AnnotationOutput/2022.11.30_22.40.11_annotator3.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator3.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator3.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator3.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1

# with open('AnnotationOutput/2022.11.30_22.40.11_annotator3.json', 'r', encoding="utf_8_sig") as fcc_file:
#     fcc_data = json.load(fcc_file)
#     for rel_pair in fcc_data:
#         obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
#         for anno in rel_pair['Anotations']:
#             key = str([obj1, anno, obj2])
#             if key in relation_dict.keys():
#                 relation_dict[key] += 1
#             else:
#                 relation_dict[key] = 1
import os

dir_list = os.listdir('AnnotationOutput_annotator_KN/')
ans = 0
# print(dir_list)

for i in dir_list:
    p1 = 'AnnotationOutput_annotator_KN/' + i
    p2 = 'AnnotationOutput_annotator_NH/' + i
    p3 = 'AnnotationOutput_annotator_RS/' + i
    relation_dict = {}
    with open(p1, 'r', encoding="utf_8_sig") as fcc_file:
        fcc_data = json.load(fcc_file)
        for rel_pair in fcc_data["AnotationResults"]:
            # print("p1")
            # print(rel_pair["AnotationResults"])
            obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
            for anno in rel_pair['Anotations']:
                key = str([obj1, anno, obj2])
                if key in relation_dict.keys():
                    relation_dict[key] += 1
                else:
                    relation_dict[key] = 1
    # print("2222222222222")
    with open(p2, 'r', encoding="utf_8_sig") as fcc_file:
        fcc_data = json.load(fcc_file)
        for rel_pair in fcc_data["AnotationResults"]:
            obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
            for anno in rel_pair['Anotations']:
                key = str([obj1, anno, obj2])
                if key in relation_dict.keys():
                    relation_dict[key] += 1
                else:
                    relation_dict[key] = 1

    with open(p3, 'r', encoding="utf_8_sig") as fcc_file:
        fcc_data = json.load(fcc_file)
        for rel_pair in fcc_data["AnotationResults"]:
            obj1, obj2 = rel_pair['Selections'][0], rel_pair['Selections'][1]
            for anno in rel_pair['Anotations']:
                key = str([obj1, anno, obj2])
                if key in relation_dict.keys():
                    relation_dict[key] += 1
                else:
                    relation_dict[key] = 1

    

# print(len(relation_dict))

    ratings = []

    iter = 0

    num_anno = 3

    for i in relation_dict:
        # print(i, relation_dict[i])
        ratings += [(iter, 'yes')] * relation_dict[i]
        ratings += [(iter, 'no')] * (num_anno - relation_dict[i])
        iter += 1

    # print(ratings)

    ans += fleiss_kappa(ratings, num_anno)
    # print(ans)

# print('DONEEE')
print(ans/len(dir_list))
