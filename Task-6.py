with open('Task-6_file.txt', 'r', encoding='utf-8') as tf6:
    dict_lessons = dict()
    for raw in tf6.readlines():
        h_l = (0 if raw.split()[1] == '-' else int(raw.split()[1][0:-3]))
        h_pr = (0 if raw.split()[2] == '-' else int(raw.split()[2][0:-4]))
        h_lab = (0 if raw.split()[3] == '-' else int(raw.split()[3][0:-5]))
        dict_lessons.update({raw.split()[0][0:-1]: sum([h_lab, h_l, h_pr])})
print(dict_lessons)
