def file_to_cfg(text):
    cnf = []
    for line in text:
        cnf.append(line.split(' -> '))
    product = list()

    count = 0
    for rule in cnf:
        cnf[count][1] = rule[1].split(" | ")
        count+=1        

    count = 0
    for rule in cnf:
        if len(cnf[count][1]) == 1:
            cnf[count][1] = rule[1][0].split(" ")
        count+=1

    count = 0
    for rule in cnf:
        for x in range(len(cnf[count][1])):
            cnf[count].append(cnf[count][1].pop(0))
        cnf[count].pop(1)
        count += 1
    
    return cnf

def open_file(directory):
    text = []
    with open(directory, 'r') as file:
        data = file.readlines()

        for rule in data:
            text.append(rule.strip("\n"))
            
    return text

def main():
    file = open_file("C:/Users/user/Downloads/cyk_algorithm-main/cyk_algorithm-main/model/cnf.txt")    
    cnf = file_to_cfg(file)
    return cnf
