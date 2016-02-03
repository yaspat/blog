.. title: Informatique : Leçon 8. Matrices
.. slug: lecon-8-matrices
.. date: 2016-02-03 17:41:55 UTC+01:00
.. tags: python, matrices, listes en compréhension
.. category: informatique
.. link: 
.. description: 
.. type: text


Comment représenter les matrices ?
==================================

.. class:: alert alert-info pull-right

.. contents::

**Rappel.** Une matrice est un tableau bi-dimensionnel de nombres. Il
existe un module dédié au calcul matriciel, mais pour le moment on va
construire artisanalement nos matrices. ça fera un bon exercice de
programmation.





**Exemple.**
:math:`A =\begin{pmatrix} 1&1&1\\ 1&1&0\\ 1&0&1 \end{pmatrix}` ou
:math:`M =\begin{pmatrix} 1&2&3\\ 4&5&6 \end{pmatrix}`

Vous pouvez considérer ainsi qu'une matrice est une liste de lignes,
chaque ligne étant elle-même une liste de flottants. Ainsi, on peut
définir des matrices comme des listes de listes.

.. code:: python

    A = [[1,1,1],[1,1,0],[1,0,1]] # les séparateurs des items sont 
                                  # des virgules


.. raw:: html

	<!--TEASER_END-->



.. code:: python

    M = [[1,2,3],[4,5,6]]


Accéder à un coefficient
------------------------

Si vous vous voulez récupérer le coefficient :math:`m_{i,j}` dans
:math:`M`, par exemple :math:`m_{2,3} = 6`, vous taperez :

.. code:: python

    M[1][2] # En Python, la numération commence à  0 ...




.. parsed-literal::

    6



Fonction cousue main : taille d'une matrice
-------------------------------------------

**Exercice.**

1. Construire une fonction :math:`\texttt{taille(A)}` qui prend en
   entrée une matrice :math:`\texttt{A}` et retourne en sortie le tuple
   :math:`\texttt{(n,p)}` donnant son format. Par exemple, pour la
   matrice :math:`\texttt{M}` précédente, :math:`\texttt{taille(M)}`
   doit vous retourner le tuple :math:`\texttt{(2,3)}`.

2. Testez votre fonction sur les matrices :math:`A`,\ :math:`M`
   précédentes.

3. Pourquoi cela ne marche pas pour ``L = [1,2,3,4]`` ?

4. Testez alors sur la matrice ligne
   :math:`L=\begin{pmatrix} 1&12&-1&0 \end{pmatrix} ` et la matrice
   colonne :math:`C= \begin{pmatrix} 1\\ 2\\ -1\\ 0 \end{pmatrix}`

**Réponse à la question 1.**

.. code:: python

    def taille(M):
        """ fonction qui prend en entrée une matrice vue comme
            une liste de listes, et qui retourne en sortie son format.
            Exemple : M = 1 2 3
                          4 5 6 
            taille(M) vaut (2,3)
        """
        return  len(M), len(M[0]) # C'est bien un tuple !

**Réponse à la question 2.**

.. code:: python

    taille(M) 




.. parsed-literal::

    (2, 3)



.. code:: python

    taille(A)




.. parsed-literal::

    (3, 3)



**Réponse à la question 3.** l'objet :math:`\texttt{L}` ainsi défini est
une liste d'entiers et pas uen liste de listes : en tant que telle, ce
n'est pas une matrice.

**Réponse à la question 4.**

.. code:: python

    L =  [[1,12,-1,0]]       # Ne pas oublier que chaque ligne de
    C =  [[1],[2],[-1],[0]] # toute matrice est une liste !
                             # D'où les (nombreux) crochets

.. code:: python

    taille(L)




.. parsed-literal::

    (1, 4)



.. code:: python

    taille(C)




.. parsed-literal::

    (4, 1)



Opérations matricielles cousues main
====================================

Multiplication par une constante
--------------------------------

**Exercice.** Programmer une fonction :math:`\texttt{mult(mu,A)}` qui
prend en entrée un scalaire :math:`\mu` et une matrice :math:`A` et qui
retourne en sortie la matrice :math:`\mu A`.

*Indications*

1. Si on appelle :math:`\texttt{resultat}` la matrice qu'on veut
   calculer, intialisez votre liste :math:`\texttt{reusltat}` à une
   liste vide.

2. Remplissez :math:`\texttt{resultat}` ligne par ligne : boucle sur les
   lignes.

3. Pour chaque ligne : remplissez :math:`\texttt{resultat}` colonne par
   colonne : boucle sur les colonnes.

Vous aurez besoin de regarder dans l'aide-mémoire comment ajouter un
élément à une liste pour remplir vos lignes et votre matrice.

Votre fonction contient donc une double boucle.

.. code:: python

    def mult(mu,A):
        """ Fonction qui calcule le produit mu X A où mu est un scalaire
        et A une matrice.
        """
        (n,p) = taille(A)
        resultat = []
        for i in range(n):     # je prends les lignes de A une par une
                               # range(k) signifie range(0,k)
            ligne=[]           # je remplis la ligne qui est vide   
            for j in range(p):
                ligne.append(mu*A[i][j])# j'ajoute à la ligne le coeff mu a_ij
            resultat.append(ligne)      # j'ajoute la ligne calculée à la matrice
        return resultat

.. code:: python

    mult(-1,A)




.. parsed-literal::

    [[-1, -1, -1], [-1, -1, 0], [-1, 0, -1]]



Version améliorée : les listes en compréhension c'est super
-----------------------------------------------------------

**Remarque.** Il y a une façon plus pythonique de faire cela. Je pars de
la liste suivante :

.. code:: python

    liste1 = [ 1, -9 ,5, 4]

Comme en maths !
~~~~~~~~~~~~~~~~

Je créé la liste qui s'écrirait ainsi en maths :
:math:`\texttt{liste2} = [ 3x, \quad  x \in  \texttt{liste1}]`. En
**Python**, cela s'écrit de la même façon :

.. code:: python

    liste2=[3*x for x in liste1]
    print liste2


.. parsed-literal::

    [3, -27, 15, 12]


Et en cascade
~~~~~~~~~~~~~

Si je veux construire de la même façon la matrice :math:`3A` où
:math:`A` est la matrice précédemment définie :
:math:`A =\begin{pmatrix} 1&1&1\\ 1&1&0\\ 1&0&1 \end{pmatrix}`

.. code:: python

    [ [3*x for x in ligne] for ligne in A ]




.. parsed-literal::

    [[3, 3, 3], [3, 3, 0], [3, 0, 3]]



Ce qui donne une façon plus simple de programmer :math:`\texttt{mult}` :

.. code:: python

    def mult2(mu,A):
        """version améliorée de mult"""
        return [ [mu*x for x in toto] for toto in A ]

.. code:: python

    mult2(5,A)




.. parsed-literal::

    [[5, 5, 5], [5, 5, 0], [5, 0, 5]]



Produit matriciel cousu main
----------------------------

**Exercice.** Ecrire une fonction :math:`\texttt{fois(A,B)}` qui prend
en entrée deux matrices :math:`\texttt{A}` et :math:`\texttt{B}` et qui
:

1. Retourne en sortie le produit matriciel :math:`\texttt{AB}` si il est
   défini.
2. Affiche un message d'erreur sinon.

*Indication.* Construire la matrice :math:`\texttt{AB}` ligne par ligne
(boucle !) et regarder dans l'aide-mémoire comment ajouter un élément à
une liste.

.. code:: python

    def fois(A,B):
        """ Calcule le produit matriciel A x B si il existe, sinon
            affiche un message d'erreur.
        """
        (n,p) = taille(A)        # j'utilise ma fonction taille !
        (q,r) = taille(B)
        if p != q :
            print 'Matrices incompatibles'
        else:
            produit = []         # j'intialise AB à une matrice vide
            for i in range(0,n): # je calcule la ligne i
                ligne = []       # j'intialiste la ligne à une ligne vide
                for j in range(0,r):
                    coeff = 0
                    for k in range(0,p):
                        coeff += A[i][k]*B[k][j]
                    ligne.append(coeff)
                produit.append(ligne)
        return produit

.. code:: python

    atilla=[[1,1,1],[1,1,1],[1,1,1]]

.. code:: python

    fois(atilla,atilla)




.. parsed-literal::

    [[3, 3, 3], [3, 3, 3], [3, 3, 3]]



.. code:: python

    fois(A,A)




.. parsed-literal::

    [[3, 2, 2], [2, 2, 1], [2, 1, 2]]



.. code:: python

    print A


.. parsed-literal::

    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


Pour rigoler : se bricoler un bel affichage
===========================================

On commence à faire du tuning là. On aimerait bien que :

.. code:: python

    print A


.. parsed-literal::

    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


donne un affichage en tableau. Voici le principe :

1. Déterminer dans la liste des coefficients de la matrice le coeff qui
   prend le plus de place dans la matrice.

2. Réserver le même espace à chaque coeff.

3. Afficher les lignes les unes au-dessus des autres.

Pour 1., je vais faire ça avec la puissance des listes en compréhension.
Accrochez-vous, quand on a compris, c'est facile, mais à lire dans
l'autre sens c'est plus dur :

.. code:: python

    def longueur_max(A):
        """ cherche la chaine de caractères la plus longue parmi les chaînes
            représentant les coeffs de la matrice A 
        """   
        return  max([len(str(coeff)) for ligne in A for coeff in ligne])

Par exemple : je prends la matrice

.. math::

    A = \begin{pmatrix}
   1 & 2 & 4324\\
   333333&1&0
   \end{pmatrix}

.. code:: python

    A = [ [1,2,4324], [333333,1,0]]
    longueur_max(A)  # la chaine '333333' est la plus longue, de longueur 6




.. parsed-literal::

    6



C'est la magie de **Python** : une syntaxe très souple qui permet
d'écrire en peu de mots des choses compliquées. Revers de la médaille :
pour relire du code, c'est souvent compliqué quand on use des astuces
pythoniques.

Pour 2., je crée une fonction qui étant donné une chaîne de caractères,
la complète avec des espaces pour qu'elle atteigne une longueur
:math:`\mathtt{r}` donnée :

.. code:: python

    def ajoute_blancs(chaine,r):
        l = len(str(chaine)) # je mets un str en plus au cas où on 
                             # veut rentrer un flottant.
        return   ' '*(r-l)+str(chaine)

.. code:: python

    ajoute_blancs(12,4)




.. parsed-literal::

    '  12'



Avec ça, je peux faire ma fonction d'affichage

.. code:: python

    def affiche(A):
        p = longueur_max(A)
        for ligne in A:
            print ' '.join([ajoute_blancs(coeff,p) for coeff in ligne])

Si je reprends ma matrice :

.. math::

    A = \begin{pmatrix}
   1 & 2 & 4324\\
   333333&1&0
   \end{pmatrix}

.. code:: python

    affiche(A)


.. parsed-literal::

         1      2   4324
    333333      1      0

