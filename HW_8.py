import urllib.request as req
from requests import request
import json
import pandas as pd


children_list = []
def crawler(url):
    request = req.Request(url , headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")  #根據觀察，取得資料是JSON格式

    data = json.loads(data) #把原始的 JSON 資料解析成字典/列表的表示形式
    print('children' in data['results'][0])

    if ('children' in data['results'][0]):
        children_list.append(data['results'][0]['children'])
        # for x in data['results'][0]['children']:
        #     print(x)
    else:
        children_list.append('[]')


go_terms = pd.read_csv("go_terms_excel_csv.csv")
go_terms_list = list(go_terms.iloc[:,0])

print(len(go_terms_list))

for x in go_terms_list:
    x= str(x)
    if len(x)== 1:
        x = '000000'+x
    if len(x)== 2:
        x = '00000'+x    
    if len(x)== 3:
        x = '0000'+x
    if len(x)== 4:
        x = '000'+x
    if len(x)== 5:
        x = '00'+x  
    if len(x)== 6:
        x = '0'+x
    url = 'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:'+x+'/complete'
    print(url)
    crawler(url)

# print(children_list)
# for x in children_list:
#     print(x)

go_terms['children'] =  children_list
go_terms.to_csv('go_terms_with_children.csv',index=None)

    

