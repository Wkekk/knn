# Projet KNN

Ce projet à pour objectif la mise en place d'un algorithme KNN from scratch et d'une version utilisant le module python SKlearn.

## KNN from scratch

Pour mettre en place l'algorithme j'ai d'abors créé des fonction permettant de calculer les différentes distances entre les vecteurs (euclidienne, de Manhathen et de Minkowski). Par la suite j'ai mis en place le coeur du programme, l'algorithme en lui même puis des fonctions permettant le calcul de statistique pour avoir une meilleure approche de l'efficacité de l'algorithme.

### Les fonctions

#### p_roots()

Fonction permettant le calcul de la distance de Minkowski

#### distence()

Fonction permettant de calculer les différentes distances, elle prends en paramètre la distance voulue (euclidienne, manhathan, minkowski), les deux vecteurs dont on veut calculer la distance et la profondeur dans le cas de la distance de Minkowski. les paramètres sont à entrer dans l'ordre donné précédemment.

#### KNN_V1()

Première version de l'algorithme, celle ci utilise le dataframe complet comme feature et fournis donc des résultats plus précis mais elle n'est pas utilisable pour des données sans interprétation. Elle prends en paramètres les features d'entrainement, le vecteur à classer, le nombre de voisins à utiliser et la distance à utiliser *dans cette ordre*.

#### essais_mult()

Fonction mettant en place l'éxecutions de l'algorithme sur le jeu de test complet, elle prends en paramètres la distances à utiliser et le nombre de voisins que l'on veut sélectionner. Elle retourne le pourcentage de prédictions correctes.

#### KNN_V2()

Version 2 de l'algorithme KNN, cette fois si utilisant seulement les réponses aux questions en features. Son taux de réussite est donc plus bas. Elle prends en paramètres les features et target du jeux d'entrainement, le vecteur à classer, le nombre de voisins et la distance, *dans cette ordre*. Attention à bien éxecuter cette fonction avec des features ne comprenant que les questions et des targets en version label ('A', 'B', 'C').

#### essais_mult_V2()

Mets en place l'algorithme KNN_V2 sur le jeu de test complet. 