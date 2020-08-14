import json
def convert_file_format(input_file_path, output_file_path):
    fr = open(input_file_path, "r", encoding='utf-8')
    ls = []
    for line in fr:
        line = line.replace("\n", "")
        ls.append(line.split(","))
    fr.close()
    fw = open(output_file_path, "w", encoding='utf-8')
    for i in range(1, len(ls)):
        ls[i] = dict(zip(ls[0], ls[i]))
    b = json.dumps(ls[1:], sort_keys=True, indent=4, ensure_ascii=False)
    fw.write(b)
    fw.close()


convert_file_format("student.csv", "student.json")




