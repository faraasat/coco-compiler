# ar = [["if(i", ">", "5)"], ["bool", "f", "=", "False"]]
ar = [["if(true)"], ["bool", "f", "=", "False"]]
my_arr = []
scope = 0

for i in ar:
    if "if" in i[0]:
        it = []
        it.append("\t"*scope)
        if len(i) > 1:
            it.append("if(" + i[0].split("(")[1])
            it.append(i[1])
            it.append(i[2].split(")")[0] + "):")
        else:
            bool_f = False
            if "true" in i[0]:
                bool_f = True
                it.append(f"if({bool_f}):")
        scope += 1
        my_arr.append(it)
    else:
        i.insert(0, "\t"*scope)
        my_arr.append(i)

for i in my_arr:
    for j in i:
        if j:
            print(j, end=" ")
    print()