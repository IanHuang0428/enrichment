import numpy as np
import pandas as pd
import scipy.stats
import time
from statsmodels.stats.multitest import multipletests
# https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html

start = time.time()
def fisher(A,B,C,D) :

    T = int(A)      #交集數         1      剩下的交集處
    S = int(B)      #輸入 genes數   18    輸入一總數
    G = int(C)      #genes 樣本數   1117   篩選的樣本
    F = int(D)      #總 genes數     6572  輸入二總數

    S_T = S-T
    G_T = G-T
    F_G_S_T = F-G-S+T

    oddsratio, pvalue_greater = scipy.stats.fisher_exact( [ [T,G_T] , [S_T,F_G_S_T]] ,'greater')
    oddsratio, pvalue_less = scipy.stats.fisher_exact( [ [T,G_T] , [S_T,F_G_S_T]] ,'less')

    return pvalue_greater

# ================================================================================================
# ================================================================================================


domain_data = pd.read_csv("protein_domain_map_id.csv")
go_f_data = pd.read_csv("go_f_map_id.csv")

# print(list(domain_data_2['Systematic Name']))

list_associated = []

number=0
for x in list(go_f_data['Systematic Name']):
    number+=1
    print(number)
    input_list = eval(x)
    # print(len(input_list))

    # D = [6611 for n in range(len(domain_data))]
    D = [6611]*len(domain_data)
    C = list(domain_data["count"])
    B = [len(input_list) for n in range(len(domain_data))]

    list_A = list(range(len(domain_data)))
    A = list(range(len(domain_data)))
    test = list(range(len(domain_data)))

    for n in range(len(domain_data["protein_domain"])):

        list_A[n] = list(set(input_list)&set(eval(domain_data["Systematic Name"][n])))
        A[n] = len(list_A[n])

        test[n] = fisher(A[n], B[n], C[n], D[n])

    #校正p-value
    cut_off = 0.01
    P_value_corr_FDR = multipletests(test,alpha=cut_off, method= "fdr_bh")
    P_value_corr_Bon = multipletests(test,alpha=cut_off, method= "bonferroni")

    result = pd.DataFrame({"Systematic Name":domain_data["protein_domain"],"P-value":test,"FDR":P_value_corr_FDR[1],"Bonferroni":P_value_corr_Bon[1]})


    # print(len(P_value_corr_FDR))
    # print("[ [小於cut off 回傳True], [校正後的P-value], [corrected alpha for Sidak method], [corrected alpha for Bonferroni method] ]")
    # print(result)
    # print(result[result["FDR"]<=0.01])

    
    list_id = []
    result = (result[result["FDR"]<=0.01]).reset_index()

    for i in range(len(result['Systematic Name'])):
        # print('------------------------------')
        list_id.append(result['Systematic Name'][i])
        # print(str_result)
    
    list_associated.append(list_id)


    # result.to_excel("result.xlsx",index=None)

go_f_data['Associated domains'] = list_associated
go_f_data.to_excel('go_f_to_domain_results.xlsx',index=None)
close = time.time()
print(close-start)
