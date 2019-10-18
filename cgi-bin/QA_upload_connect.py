#!D:/Python/Python36/python.exe
#!C:/ProgramData/Anaconda3/python.exe
import cgi, cgitb
import os
import pandas as pd
import numpy as np
import json
from module.QA_train import QA_train

def text2df(data,owner):
    sentence_list = data.split('\n')
    result = []
    for i in range(len(sentence_list)):
        temp = sentence_list[i].split(',')
        for j in range(len(temp)):
            temp[j] = temp[j].lstrip().rstrip()
            temp[j] = temp[j].replace('\r','')
            temp[j] = temp[j].replace('\n','')
        if len(temp) != 2:
            continue
        result.append(temp)
    result = pd.DataFrame(np.array(result))
    # result['owner'] = owner
    result.columns = ["課文","題目"]
    return result
        
parameter = cgi.FieldStorage()
data = parameter.getvalue('data')
owner = parameter.getvalue('owner')
p_name = parameter.getvalue('p_name')
text = data
# with open('C:\\Users\\student\\Desktop\\test.txt','w',encoding='utf_8_sig') as fout:
#     fout.write(data)
df = text2df(text,owner)
# df.to_csv(os.path.join('C:\\Users\\student\\Desktop','test.csv'),encoding='utf_8_sig',index=0)
# data_dir = 'D:\\dektop\\QA_test_demo\\cgi-bin\\module\\QA_data\\test.csv'
# df = pd.read_csv(data_dir)
QA_train = QA_train(owner,p_name)
QA_train.insert_training_data(df)
#轉成dict回傳
print("Content-type:text/html") #必須
print('') #必須
print('QA upload finish')