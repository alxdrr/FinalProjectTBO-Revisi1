import streamlit as st
import interface
import import_rule

def convert(lst):
    return ([i for i in lst.split()])

def CYK(sentence):
    rule = import_rule.main()
    cnf = rule.copy()
    word = convert(sentence)
    product = list()
    combinedCNF = list()
    for i in range(len(cnf)):
        product.append(cnf[i].pop(0))
    for i in range(len(cnf)):
        j = (len(cnf[i]))
        if j == 2:
            combinedCNF.append(cnf[i][0]+cnf[i][1])
        elif j == 1:
            combinedCNF.append(cnf[i][0])
        else:
            combinedCNF.append("")

    variabel = dict()

    Table = [["" for x in range(len(word))] for y in range(len(word))]

    for i in range(1,len(word)+1):
        j = i
        variabel[i,j] = []
        for k in range(len(cnf)):
            if word[i-1] in cnf[k]:
                variabel[i,j].append(product[k])
                Table[i-1][j-1] = "V"

    for k in range(len(word)-1):
        for i in range(1,len(word)-k):
            j = i+k+1
            result = list()
            if i != j and i < j and j <= len(word) and Table[i-1][j-1] != "V":   
                if j - i == k+1:
                    for l in range(j-i):        
                        for p in range(len(variabel[i,i+l])):
                            for q in range(len(variabel[i+1+l,j])):
                                result.append(variabel[i,i+l][p]+variabel[i+1+l,j][q])

                variabel[i,j] = []
                for x in range(len(combinedCNF)):
                    if combinedCNF[x] in result:
                        variabel[i,j].append(product[x])
            if j != len(word):
                del result

    if "K" in variabel[1,len(word)]:
        interface.valid = 'y'
        interface.result = result.copy()
    else:
        interface.valid = 'x' 
 
        
    
