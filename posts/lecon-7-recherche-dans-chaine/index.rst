.. title: Informatique : Leçon 7. Recherche dans une chaîne de caractères  
.. slug: lecon-7-recherche-dans-chaine
.. date: 2016-01-24 12:36:59 UTC+01:00
.. tags: python, informatique,  chaînes de caractères, leçon
.. link: 
.. description: 
.. type: text
.. category: informatique

.. class:: alert alert-info pull-right

.. contents::








Formulation du problème
-----------------------

Donnée : une chaîne de caractères.

    **Problème 1.** je veux savoir si ma chaîne contient un caractère
    donné.

Ce dernier problème est un cas particulier du problème plus général
suivant :

    **Problème 2.** étant donné un tuple (resp. une liste), est-ce qu'un
    objet donné figure dans ce tuple (resp. cette liste) ?


.. raw:: html

       <!-- TEASER_END-->



**Réponse au problème 1.** Il y a plusieurs approches à ce problème,
donc on peut proposer différentes solutions. Mettons que je cherche le
caractère **'k'** dans une chaîne :

.. code:: python

    magik = 'iuhfguihguhgmuazhmurohgfzattzaijghaùzjg' # Définissons une chaîne







Des solutions différentes
-------------------------

Approche 1.
~~~~~~~~~~~

J'utilise une fonction prédéfinie de **Python** :

.. code:: python

    'k' in magik  # ne pas confondre nom de variable et contenu




.. parsed-literal::

    False



Approche 2.
~~~~~~~~~~~

Je parcours systématiquement toutes les lettres du mot (j'ai donc une
boucle **for**). J'initialise un compteur à :math:`\mathtt{0}` et je
l'incrémente chaque fois que je rencontre le caractère cherché. Ainsi, le  
caractère cherché est bien dans la chaîne si et seulement si à la sortie de la boucle
le compteur a une valeur non nulle.

.. code:: python

    def est_dans_chaine(mot, caractere):
        """ 
        mot : une chaine de caractère (type str)
        k : un caractère (type str)
        fonction qui retourne 1 si <k> est dans <mot>,
        et 0 sinon.     
        """
        compteur = 0
        for k in mot:                   # on peut faire des boucles sur 
                                        # les caractères d'une chaîne :
                if k == caractere:     # k prend successivement comme
                                       # valeur chaque caractère se trouvant
                    compteur += 1     # dans la chaîne <mot>
        if compteur > 0:
            return 1
        else:
            return 0 

.. code:: python

    est_dans_chaine(magik, 'k') # ne pas confondre nom de variable et contenu




.. parsed-literal::

    0



.. code:: python

    est_dans_chaine('goldorak', 'k')




.. parsed-literal::

    1



.. code:: python

    est_dans_chaine('tchoupi', 'k')




.. parsed-literal::

    0



.. code:: python

    est_dans_chaine('goldorakkkkkkkkkkkk', 'k')




.. parsed-literal::

    1



Approche 3.
~~~~~~~~~~~

Je parcours les lettres du mot et je m'arrête quand j'ai soit rencontré
le caractère que je cherche soit quand j'ai parcouru toutes lettres.
(j'ai donc une boucle **while**).

Boucle **while** : je dois examiner la condition de sortie. On arrête la
boucle quand :

1. ou bien on a rencontré le caractère cherché.
2. ou bien on a examiné tous les caractères sans succès.

Puisque la condition d'arrêt contient un "ou", la condition **while**
contient un **et**. Ce qui donne :

.. code:: python

    def est_dans_chaine3(mot, caractere):
        """ 
        mot : une chaine de caractère (type str)
        caractere : un caractère (type str)
        fonction qui retourne 1 si <caractere> est dans <mot>, et 0 sinon,
        en suivant l'approche 3.
        """
        reponse = 0  # sera actualisée et retournée en sortie
        n = len(mot) # donne  le nb. de caractères dans <mot>
        i =0         # je commence par examiner le 1er caractère
        
        while(i!= n-1 and mot[i]!=caractere):
            i+=1 # on passe au caractère suivant
        
        if  mot[i]==caractere: # j'examine la lettre qui a
                               # provoqué la sortie de boucle    
            reponse = 1
        else:
            reponse = 0
        return reponse

.. code:: python

    est_dans_chaine3('toti','i')




.. parsed-literal::

    1



**Remarque.** **Python** fait de l'évaluation paresseuse : quand il
calcule la valeur de l'assertion ::math:`[A` **et** :math:`B]`, dès lors
que :math:`A` est faux, il retourne **faux** sans chercher à savoir la
valeur de :math:`B`.

Quelques mots sur l'interruption de boucle
------------------------------------------

On pourrait parler de l'interruption du flot d'instructions en général.

Ces techniques d'interruptions dans les boucles servent typiquement dans
le cas où on sait **au plus** combien d'itérations faire dans la boucle.
C'est particulièrement adpaté ici, puisque quand on cherche un caractère
dans un mot, on sait qu'on aura au plus :math:`n` examens à faire, où
:math:`n=` la longueur du mot.

**Intérêt :** évite la programmation d'un **while** si on sait qu'on ne
dépassera pas un nombre d'itérations donné.

En pratique, on construit une boucle **for** qu'on interrompt si la
condition souhaitée est réalisée :

.. code:: python

    def est_dans_chaine4(mot,caractere):
        """ 
        mot : une chaine de caractère (type str)
        caractere : un caractère (type str)
        fonction qui retourne 1 si <caractere> est dans <mot>,
        0 sinon. Repose sur l' interruption d'une boucle for.
        """
        
        reponse = 0
        for lettre in mot: # on peut itérer sur les caractères 
                           # d'une chaîne.
            if lettre == caractere:
                reponse = 1
                break #si le if est réalisé,j'interromps la boucle
        return reponse

.. code:: python

    est_dans_chaine4('toti','o')




.. parsed-literal::

    1



.. code:: python

    est_dans_chaine4('toti','i')




.. parsed-literal::

    1



.. code:: python

    est_dans_chaine4('toti','k')




.. parsed-literal::

    0



**Remarque.** On a vu aussi qu'un **return** termine l'exécution d'une
fonction. Dans ce contexte, on peut interrompre la boucle par un
**return** de la manière suivante :

.. code:: python

    def est_dans_chaine5(mot,caractere):
        for lettre in mot: # on peut itérer sur les caractères d'une chaîne.
            if lettre == caractere:
                return 1
        return 0

.. code:: python

    est_dans_chaine5('toti','i')




.. parsed-literal::

    1



**Exercice** (*répond au problème 2*). Progammer une fonction
**est\_dans\_liste(ma\_liste,objet)** qui prend en entrée une liste
**ma\_liste**, un item **objet** quelconque et qui retourne **1** si
**objet** est dans **ma\_liste**, et **0** sinon.

.. code:: python

    def est_dans_liste(ma_liste,objet):
        for element in ma_liste:
            if element == objet:
                return 1
        return 0

.. code:: python

    L = [1, 545, 'toto', (1,2,54), 'e']
    est_dans_liste(L,54) #54 ne figure pas en tant qu'item de L !




.. parsed-literal::

    0



**Exercice** Améliorer le programme précédent pour que la fonction
retourne (le cas échéant) le premier indice **i** où se trouve **objet**
dans **ma\_liste**, sinon **-1**.

.. code:: python

    def position_dans_liste(ma_liste,objet):
        i=0
        for element in ma_liste:
            if element == objet:
                return i
            i+=1    
        return -1

.. code:: python

    position_dans_liste(L,'toto')




.. parsed-literal::

    2


