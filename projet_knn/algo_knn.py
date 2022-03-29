import pandas as pd 
import numpy as np
from math import *
from decimal import *

def p_root(value, root):   
	#pour le calcul de la distance de minkoswki 
    root_value = 1 / float(root)
    return round (Decimal(value) ** Decimal(root_value), 3)


def distance(*argv) :
	#calcul des différentes distances
	metrics = argv[0]
	a = argv[1]
	b = argv[2]
	if metrics == 'euclidienne' :
		return np.linalg.norm(a-b)
	if metrics == 'manhathan' :
		return sum(abs(val1-val2) for val1, val2 in zip(a,b))
	if metrics == 'minkowski' :
		 return (p_root(sum(pow(abs(x-y), argv[3]) for x, y in zip(a, b)), argv[3]))
	 	




def KNN(data_train, data_test, k, metrics) :
	#version 1 de mon KNN, utilise le df complet comme features donc fournis des résultats plus précis
	list_dist=[]
	val_ref = np.asarray(data_test)
	data = np.asarray(data_train)
	for train_row in data :
		#on met dans une liste la distance entre le vecteur cible (val_ref) et les différent vecteur du jeu d'entrainement
		if metrics == 'minkowski' :
			#la distance de minkowski à besoin de plus de paramètre losr de l'appel
			list_dist.append((train_row, distance(metrics, train_row, val_ref, len(val_ref))))
		else :
			list_dist.append((train_row, distance(metrics, train_row, val_ref)))
	#on ordonne la liste des distance par ordre croissant
	list_dist.sort(key=lambda tup: tup[1])
	voisins = []
	for i in range (k) :
		#on sélectionne les k premiers voisins
		voisins.append(list_dist[i][0])
	#on effectue le jugement majoritaire sur les interprétations
	output_values = [row[-1] for row in voisins]
	prediction = (max(set(output_values), key=output_values.count))
	return prediction
	




def KNN_V2(data_train, Y_train, data_test, k, metrics) :
	#version 2 de mon KNN n'utilisant que les réponses aux questions en features
	list_dist=[]
	val_ref = np.asarray(data_test)
	data = np.asarray(data_train)
	longueur = range(len(Y_train))
	data_train.index = longueur		#permet de garder une trace de l'endroit ou l'on est dans le jeu d'entrainement pour pouvoir ensuite récupérer les interpretation et faire le jugement majoritaire
	Y_train.index = longueur
	index = data_train.index
	l = 0
	for train_row in data :
		if metrics == 'minkowski' :
			list_dist.append((train_row, distance(metrics, train_row, val_ref, len(val_ref)), index[l]))
		else :
			list_dist.append((train_row, distance(metrics, train_row, val_ref), index[l]))
		l+=1
	list_dist.sort(key=lambda tup: tup[1])
	voisins = []
	for i in range (k) :
		voisins.append((list_dist[i][0], list_dist[i][2]))
	S=[]
	for m in voisins :
		S.append(m[1])
		#liste avec les indices des k plus proches voisins pour récupérer leurs interprétation dans y_train
	Pred = Y_train.iloc[S]
	Pred = [np.sum((Pred == 'A').astype(int)), np.sum((Pred == 'B').astype(int)), np.sum((Pred == 'C').astype(int))]
	Pred = np.argmax(Pred)
	if Pred == 0 :
		P = 'A'
	elif Pred == 1 :
		P = 'B' 
	else : P = 'C'
	#jugement majoritaire pour faire la prédiction
	return P