'AAAA''''
Created on 6 nov. 2017

@author: Karudev
'''
import uuid
import random as r

new_dict = []

def list_by_account(account, codeisin, name, value):
   
    print('-'+account)
    #print(new_dict)
    
    try:
        pass
    except:
        pass
    else:
        new_dict.append([value,account,codeisin,name])
    
    return new_dict
    
    

if __name__ == '__main__':
    
    
    encours = [
        ('AAAA','XXXY', "Produit 1", 3000.99),
        ('AAAA','XXXZ', "Produit 2", 1000.99),
        ('AAAB','XXX1', "Produit 3", 2000.99),
        ('AAAC','XXXA', "Produit 4", 99),
    ]
    
    encours +=50000 * [(str(r.random()),str(r.random()), "Produit "+str(r.random()), r.random())]
    
    
    #print(encours)
    #raise SystemExit
    
    users = [{'accounts' : ['AAAA','AAAB']},{'accounts' : ['AAAC']},{'accounts' : []} ]
    users += 1000 * [{'accounts' : [  str(r.random()), str(r.random())  ]}]
    
    #print(users)
    #raise SystemExit
    
    tmp = []
    for user in users: 
        new_list =  {
                        #list_by_account(compte, codeisin, name, value) 
                        codeisin : [name, value]
                        for compte, codeisin, name, value in encours
                        for compte_user in user['accounts']
                        if compte_user == compte
                        
                        
                    }
        
        
        tmp.append(new_list)
    
    print(tmp)