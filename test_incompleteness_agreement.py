import json
import os
import matplotlib.pyplot as plt

def calc_incomp_agrmnt(all_annotations):
    incomp_KN = 0
    incomp_NH = 0
    incomp_RS = 0
    agr = 0

    for edge, anns in all_annotations.items():
        if len(anns.keys()) > 1:
            # There are atleast two annotators, so calc ageement by IoU
            anns_sets = [set(val) for _,val in anns.items()]

            intersection = len(set.intersection(*anns_sets))
            union = len(set.union(*anns_sets))
            agr += intersection/union
        
        if "KN" not in anns:
            incomp_KN += 1
        if "NH" not in anns:
            incomp_NH += 1
        if "RS" not in anns:
            incomp_RS += 1
        
    total_edges = len(all_annotations.keys())

    incompleteness = (incomp_KN + incomp_NH + incomp_RS) / (3*total_edges)
    ageement = agr / total_edges

    return incompleteness, ageement
    
files_list = os.listdir('AnnotationOutput_annotator_KN/')

# Fractions for each annotation file
all_incompleteness = []
all_agreement = []

for file_name in files_list:
    p1 = 'AnnotationOutput_annotator_KN/' + file_name
    p2 = 'AnnotationOutput_annotator_NH/' + file_name
    p3 = 'AnnotationOutput_annotator_RS/' + file_name

    # All annottaions from all three files merged into one dict
    all_annotations = {}
    with open(p1, 'r', encoding="utf_8_sig") as fcc_file:
        fcc_data = json.load(fcc_file)
        for rel_pair in fcc_data["AnotationResults"]:
            key = str(rel_pair['Selections'])
            if not key in all_annotations:
                all_annotations[key] = {}
            all_annotations[key]["KN"] = rel_pair['Anotations']

            
    with open(p2, 'r', encoding="utf_8_sig") as fcc_file:
        fcc_data = json.load(fcc_file)
        for rel_pair in fcc_data["AnotationResults"]:
            key = str(rel_pair['Selections'])
            if not key in all_annotations:
                all_annotations[key] = {}
            all_annotations[key]["NH"] = rel_pair['Anotations']

    with open(p3, 'r', encoding="utf_8_sig") as fcc_file:
        fcc_data = json.load(fcc_file)
        for rel_pair in fcc_data["AnotationResults"]:
            key = str(rel_pair['Selections'])
            if not key in all_annotations:
                all_annotations[key] = {}
            all_annotations[key]["RS"] = rel_pair['Anotations']

    incompleteness, agreement = calc_incomp_agrmnt(all_annotations)

    all_incompleteness.append(incompleteness)
    all_agreement.append(agreement)

total_files = len(files_list)

print(f"Average Incompleteness = {sum(all_incompleteness)/total_files}")
print(f"Average agreement (IoU) = {sum(all_agreement)/total_files}")

plt.subplot(1, 2, 1)
plt.gca().set_title("Incompleteness distribution")
plt.hist(all_incompleteness)

plt.subplot(1, 2, 2)
plt.gca().set_title("Agreement (IoU) distribution")
plt.hist(all_agreement)

plt.savefig("test_incompleteness_agreement.png")