'''''
Created on 6 nov. 2017

@author: Karudev
'''
import uuid
import random as r


if __name__ == '__main__':
    
    dict = {}
    
    def build_dict(codeisin, product_name, value, user_list):
        
        id_client = user_list[0]
        fistname_client = user_list[1]
        lastname_client = user_list[2]
        id_cgpi = user_list[3]
        firstname_cgpi = user_list[4]
        lastname_cgpi = user_list[5]
        id_cabinet = user_list[6]
        firstname_cabinet = user_list[7]
        lastname_cabinet = user_list[8]
        id_groupement = user_list[9]
        firstname_groupement = user_list[10]
        lastname_groupement = user_list[11]
        
        
        
        try:
            dict[id_client]
        except:
            dict[id_client] = {'statistic' : [], 'user' : {}}
            
            
            dict[id_client]['statistic'].append({'name' : product_name, 'codeisin' : codeisin, 'value' : value})
            dict[id_client]['user'] =   {
                                    'type' : 'R',
                                    'id_client' : id_client,
                                    'firstname_client' : fistname_client,
                                    'lastname_client' : lastname_client,
                                    'id_cgpi': id_cgpi,
                                    'firstname_cgpi' : firstname_cgpi,
                                    'lastname_cgpi' : lastname_cgpi,
                                    'id_cabinet': id_cabinet,
                                    'firstname_cabinet' : firstname_cabinet,
                                    'lastname_cabinet' : lastname_cabinet,
                                    'id_groupement': id_groupement,
                                    'firstname_groupement' : firstname_groupement,
                                    'lastname_groupement' : lastname_groupement
                                }
            
        try:
            dict[id_cgpi]
        except:
            dict[id_cgpi] = {'statistic' : [], 'user' : {}}
            
            
            dict[id_cgpi]['statistic'].append({'name' : product_name, 'codeisin' : codeisin, 'value' : value})
            dict[id_cgpi]['user'] =   {
                                    'type' : 'K',
                                    'id_client' : id_client,
                                    'firstname_client' : fistname_client,
                                    'lastname_client' : lastname_client,
                                    'id_cgpi': id_cgpi,
                                    'firstname_cgpi' : firstname_cgpi,
                                    'lastname_cgpi' : lastname_cgpi,
                                    'id_cabinet': id_cabinet,
                                    'firstname_cabinet' : firstname_cabinet,
                                    'lastname_cabinet' : lastname_cabinet,
                                    'id_groupement': id_groupement,
                                    'firstname_groupement' : firstname_groupement,
                                    'lastname_groupement' : lastname_groupement
                                }
        
        try:
            dict[id_cabinet]
        except:
            dict[id_cabinet] = {'statistic' : [], 'user' : {}}
            
            
            dict[id_cabinet]['statistic'].append({'name' : product_name, 'codeisin' : codeisin, 'value' : value})
            dict[id_cabinet]['user'] =   {
                                    'type' : 'B',
                                    'id_client' : id_client,
                                    'firstname_client' : fistname_client,
                                    'lastname_client' : lastname_client,
                                    'id_cgpi': id_cgpi,
                                    'firstname_cgpi' : firstname_cgpi,
                                    'lastname_cgpi' : lastname_cgpi,
                                    'id_cabinet': id_cabinet,
                                    'firstname_cabinet' : firstname_cabinet,
                                    'lastname_cabinet' : lastname_cabinet,
                                    'id_groupement': id_groupement,
                                    'firstname_groupement' : firstname_groupement,
                                    'lastname_groupement' : lastname_groupement
                                }
            
        try:
            dict[id_groupement]
        except:
            dict[id_groupement] = {'statistic' : [], 'user' : {}}
            
            
            dict[id_groupement]['statistic'].append({'name' : product_name, 'codeisin' : codeisin, 'value' : value})
            dict[id_groupement]['user'] =   {
                                    'type' : 'G',
                                    'id_client' : id_client,
                                    'firstname_client' : fistname_client,
                                    'lastname_client' : lastname_client,
                                    'id_cgpi': id_cgpi,
                                    'firstname_cgpi' : firstname_cgpi,
                                    'lastname_cgpi' : lastname_cgpi,
                                    'id_cabinet': id_cabinet,
                                    'firstname_cabinet' : firstname_cabinet,
                                    'lastname_cabinet' : lastname_cabinet,
                                    'id_groupement': id_groupement,
                                    'firstname_groupement' : firstname_groupement,
                                    'lastname_groupement' : lastname_groupement
                                }
            
    
    encours = [
        ('AAAA','XXXY', "Produit 1", 3000.99),
        ('AAAA','XXXZ', "Produit 2", 1000.99),
        ('AAAB','XXX1', "Produit 3", 2000.99),
        ('AAAC','XXXA', "Produit 4", 99),
    ]
    
    encours +=10000 * [(str(r.random()),str(r.random()), "Produit "+str(r.random()), r.random())]
    
    users = [
        ('AAAA',[1000, "Nom-client","Prenom-client", 1001, "Nom-cgpi", "Prenom-cgpi", 1002, "Nom-cabinet", "Prenom-cabinet",1003, "Nom-groupement", "Prenom-groupement"]),
        ('AAAA',[10000, "Nom-client2","Prenom-client2", 10001, "Nom-cgpi2", "Prenom-cgpi2", 10002, "Nom-cabinet2", "Prenom-cabinet2",10003, "Nom-groupement2", "Prenom-groupement2"]),
        ('AAAB',[1000, "Nom-client","Prenom-client", 1001, "Nom-cgpi", "Prenom-cgpi", 1002, "Nom-cabinet", "Prenom-cabinet",1003, "Nom-groupement", "Prenom-groupement"]),
        ('AAAC',[1000, "Nom-client","Prenom-client", 1001, "Nom-cgpi", "Prenom-cgpi", 1002, "Nom-cabinet", "Prenom-cabinet",1003, "Nom-groupement", "Prenom-groupement"]),
    ]
    
    #print(encours)
    #raise SystemExit
    
    #users = [{'accounts' : ['AAAA','AAAB']},{'accounts' : ['AAAC']},{'accounts' : []} ]
    users += 13000 * [(str(r.random()),[1000, "Nom-client","Prenom-client", 1001, "Nom-cgpi", "Prenom-cgpi", 1002, "Nom-cabinet", "Prenom-cabinet",1003, "Nom-groupement", "Prenom-groupement"])]
    
    #print(users)
    #raise SystemExit
    
    print("nb encours => " + str(len(encours)))
    print("nb users => " +str(len(users)))
    
    {
        #list_by_account(compte, codeisin, name, value) 
        #codeisin : [name, value]
        build_dict(codeisin, name, value, user_list)
        for compte, codeisin, name, value in encours
        for compte_user,user_list in users 
        if compte_user == compte                   
    }
        
        
       
    
    print(dict)