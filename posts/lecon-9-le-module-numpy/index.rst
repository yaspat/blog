.. title: Leçon 9. Le module numpy
.. slug: lecon-9-le-module-numpy
.. date: 2016-03-11 16:09:43 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

.. class:: alert alert-info pull-right

.. contents::




Dans la leçon 8, on construit des matrices en les regardant comme des
listes de listes, ce qui a demandé de définir toutes les opérations
matricielles. Or, le module :math:`\texttt{numpy}` est destiné notamment
au calcul matriciel et fait le travail. On s'en servira aussi en
traitement de l'image.

Une subtilité (ou un point fort) du module : les tableaux peuvent être
multidimensionnels. Les matrices sont donc un cas particulier de
tableaux multidimensionels.








Importation des modules
=======================

.. code:: python

    import numpy as np # importation prudente

Rappel : avec **import** vous importez le module. Avec **as** vous lui
donnez un nom de préfixe pour vous rappeler les fonctions provenant du
module. Autrement dit : chaque commande utilisée du module **numpy** est
préfixée par **np**, ce qui permet d'identifier son origine.


.. raw:: html

  <!--TEASER_END-->

Premiers pas avec ``numpy``
===========================

La plupart des commandes suivantes sont dans votre aide-mémoire. Les
matrices sont des objets de type **array** . Si on tape simplement :

.. code:: python

    A = [[1,0,1],[4,2,-8]]

.. code:: python

    type(A)




.. parsed-literal::

    list



alors on obtient, comme au TP précédent, une liste de listes. En
revanche, si vous déclarez votre liste comme un tableau **numpy** (en
anglais : array) vous obtenez :

.. code:: python

    A = np.array( [[1,0,1],[4,2,-8]]) # Le préfixe np provient de l'importation
    print A                          # prudente du module



.. parsed-literal::

    [[ 1  0  1]
     [ 4  2 -8]]


.. code:: python

    type(A)




.. parsed-literal::

    numpy.ndarray



Autrement dit, dans le module **numpy**, c'est la commande **np.array**
qui permet de définir des matrices. L'objet ainsi construitn'est lus un
objet de type liste, mais un objet de type tableau multidimensionnel :
**nd-array**. C'est ce genre d'objet qui va être considéré comme une
matrice à partir de maintenant.

Taille d'une matrice
--------------------

Vous la récupérez avec la commande **shape** (c'est ce qu'on appelle une
*méthode* au sens de la programmation orientée objet. Ce n'est pas
vraiment une fonction, ni l'objet (ah ah!) de ce TP. Les méthodes se
suffixent aux objets auxquelles elles appliquent, ou sur lesquelles
elles opèrent) :

.. code:: python

    A.shape # C'est pourquoi on n'écrit pas shape(A) : shape est une méthode, pas une fonction




.. parsed-literal::

    (2, 3)



Le résultat est un **tuple**. Ici, ce tuple contient 2 items : cela
signifie que le tableau est 2-dimensionnel. Enfin, les valeurs des items
nous disent que :math:`\mathtt{A}` est de taille :math:`2 \times 3`.

Accès aux coefficients
----------------------

Les doubles indices sont d'usage. Restriction habituelle de **Python** :
les indices commencent, on s'en doute, à :math:`0` :

.. code:: python

    print A


.. parsed-literal::

    [[ 1  0  1]
     [ 4  2 -8]]


Par exemple, pour récupérer :math:`a_{2,3}=-8`

.. code:: python

    A[1,2] # inutile d'utiliser A[1][2]




.. parsed-literal::

    -8



Extraction d'une ligne ou d'une colonne
---------------------------------------

De façon plus générale on peut extraire des sous-matrices par tranches :

.. code:: python

    print A 


.. parsed-literal::

    [[ 1  0  1]
     [ 4  2 -8]]


Par exemple, si je veux
:math:`\ell_1 =\begin{pmatrix} 1&0&1 \end{pmatrix}`, la première ligne
de :math:`A` :

.. code:: python

    A[0,:] # les deux points ":" servent de "joker" si vous voulez. 
           # C'est l'opérateur de spécification par tranche (de slicing).




.. parsed-literal::

    array([1, 0, 1])



**Attention. ** Vous observez qu'il n'existe plus qu'une paire de
crochets : les lignes sont des tableaux 1-dimensionnels, et donc, pas
des matrices au sens de tableaux 2-dimensionnels :

.. code:: python

    ligne = A[0,:]
    print ligne


.. parsed-literal::

    [1 0 1]


.. code:: python

    ligne.shape # La réponse ne sera pas (1,3)
                # on devrait récupérer un tuple à
                # un seul item




.. parsed-literal::

    (3,)



On a un tuple ne contenant qu'un seul élément : on a donc un tableau
:math:`\mathtt{1D}` (1-dimensionnel) de longueur :math:`\mathtt{3}`.

Si je veux récupérer :math:`c_2=\begin{pmatrix} 0\\2\end{pmatrix}`, la
deuxième colonne de :math:`\mathtt{A}` :

.. code:: python

    A




.. parsed-literal::

    array([[ 1,  0,  1],
           [ 4,  2, -8]])



.. code:: python

    A[:,1]
    print A[:,1]


.. parsed-literal::

    [0 2]


Ma colonne n'est pas formatée en colonne : c'est encore un tableau
:math:`\mathtt{1D}`. Dans la suite on remédie à ce problème (si on
considère que cela est un problème) grâce à une méthode permettant de
redimensionner un tableau.

Redimensionner un tableau numpy
-------------------------------

Si vous souhaitez vraiment récupérer une colonne non pas pas comme un
tableau :math:`\mathtt{1D}`, mais une "vraie" colonne au sens des
matrices, c'est-à-dire, pour l'exemple précédent, un tableau de format
:math:`(2,1)`, vous avez la méthode :math:`\mathtt{reshape}` pour cela :

.. code:: python

    colonne = A[:,1]               # j'extrais la deuxième colonne de A
    colonne = colonne.reshape(2,1) # avec reshape(2,1) j'en fais une matrice 2 X 1 
    print colonne


.. parsed-literal::

    [[0]
     [2]]


\*\* Exercice. \*\* La commande :math:`\mathtt{range}` a son analogue en
tableau :math:`\mathtt{numpy}` : :math:`\mathtt{arange}` (pour
array-range). Par exemple :

.. code:: python

    np.arange(1,10) # tableau 1D des entiers de 1 à 9.




.. parsed-literal::

    array([1, 2, 3, 4, 5, 6, 7, 8, 9])



Construire la matrice suivante : $ B =

.. raw:: latex

   \begin{pmatrix} 
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9
   \end{pmatrix}

$.

**Solution.**

.. code:: python

    B = np.arange(1,10).reshape(3,3)
    print B


.. parsed-literal::

    [[1 2 3]
     [4 5 6]
     [7 8 9]]


Autres opérations
=================

Reportez-vous à l'aide-mémoire : les opérations les plus utiles y sont
consignées. Voici quelques matrices typiques :

Matrices remarquables
---------------------

Matrices de 1's
~~~~~~~~~~~~~~~

.. code:: python

    atilla = np.ones([3,3])
    print atilla


.. parsed-literal::

    [[ 1.  1.  1.]
     [ 1.  1.  1.]
     [ 1.  1.  1.]]


Matrices de 0's
~~~~~~~~~~~~~~~

.. code:: python

    nulle = np.zeros([3,3])
    print nulle


.. parsed-literal::

    [[ 0.  0.  0.]
     [ 0.  0.  0.]
     [ 0.  0.  0.]]


Matrice unité ou identité
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    identite = np.eye(4) #  Matrice I4 : identité d'ordre 4
    print identite,"\n"  # rappel : "\n" est le saut de ligne
    print 3*identite     # une matrice scalaire


.. parsed-literal::

    [[ 1.  0.  0.  0.]
     [ 0.  1.  0.  0.]
     [ 0.  0.  1.  0.]
     [ 0.  0.  0.  1.]] 
    
    [[ 3.  0.  0.  0.]
     [ 0.  3.  0.  0.]
     [ 0.  0.  3.  0.]
     [ 0.  0.  0.  3.]]


Une remarque sur le produit matriciel
-------------------------------------

En **Python**, vous pouvez faire deux types de produit :

1. Le produit matriciel que vous connaissez avec les restrictions de
   format que cela implique. La commande est :

   .. math::  \texttt{np.dot(A,B)}\quad \text{, et ce n'est pas }\quad \texttt{A*B}

2. Il y a un autre produit qui existe (mais qui ne correspond à rien en
   maths) : le produit élément par élément (broadcasting). Pour deux
   matrices :math:`A` et :math:`B` de même format :

.. math::  \texttt{A*B}

donne la matrice de même format que :math:`A` et :math:`B` de
coefficient général :math:`a_{i,j} \times b_{i,j}`. Opération très utile
pour le calcul en "parallèle" (évite le recours à une boucle).

**Exercice**

1. Calculer :math:`A^2` où :math:`A` est la matrice Attila d'ordre 3.

2. Construire en utilisant la matrice :math:`B` précédente la matrice
   :math:`C` suivante :

$ C =

.. raw:: latex

   \begin{pmatrix} 
   1 \times(2^1) & 2\times(2^2) & 3\times(2^3) \\
   4 \times(2^4)& 5\times(2^5) & 6\times(2^6) \\
   7 \times(2^7)& 8\times(2^8) & 9\times(2^9)
   \end{pmatrix}

$

.. code:: python

    # Réponse à 1.  :
    #----------------
    A = np.ones([3,3])
    np.dot(A,A) #Produit matriciel de A avec A




.. parsed-literal::

    array([[ 3.,  3.,  3.],
           [ 3.,  3.,  3.],
           [ 3.,  3.,  3.]])



.. code:: python

    # Réponse à 2. : 
    #---------------
    B = np.arange(1,10).reshape(3,3)
    print 'B ='
    print B                         # la matrice B de tout à l'heure
    M = np.array([2**k for k in B]) # construction en compréhension
    print 'M = '
    print M
    C = B*M                         # la matrice  est le produit 
    print 'C = '                    # élément par élement de B et M 
    print C


.. parsed-literal::

    B =
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    M = 
    [[  2   4   8]
     [ 16  32  64]
     [128 256 512]]
    C = 
    [[   2    8   24]
     [  64  160  384]
     [ 896 2048 4608]]


Visualiser une matrice 
======================

Voir `ce billet <link://slug/matshow-ca-plait-aux-filles>`_.
