.. title: Informatique : Leçon 4
.. slug: Boucles Pour
.. date: 2015-11-4 13:39:19 UTC+02:00
.. tags: python, boucles,for,  leçon 
.. category: informatique
.. link: 
.. description: 
.. type: text

.. class:: alert alert-info pull-right

.. contents::



Les boucles servent à automatiser la répétition de tâches. Il y a
essentiellement deux types de boucles :

1. Celles pour lesquelles *on sait à l'avance* le nombre d'itérations
   (ou répétitions) à effectuer : ce sont les boucles **for**. Par
   exemple : calculer les 100 premiers termes d'une suite :math:`(u_n)`
   donnée.

2. Celles pour lesquelles *on ne sait pas à l'avance* le nombre
   d'itérations à effectuer : ce sont des boucles subordonnées à un
   *test d'arrêt* : les boucles **tant que**. Par exemple : trouver le
   premier terme d'une suite :math:`(u_n)` donnée de limite
   :math:`+\infty` vérifiant :math:`u_n > 10000`.

.. raw:: html

   <!-- TEASER_END -->

Exemples de boucles pour
------------------------

Exemple 1
~~~~~~~~~

Prenons l'exercice 16 p.25 du poly d'algorithmique : écrire un programme
demandant à l'utilisateur d'entrer un entier :math:`N` et calculant et
affichant les termes :math:`r_0, \dots , r_N` de la suite définie par :

.. math::

    \left\{ \begin{array}{rcl}
   r_0 &=& 4 \\
   \forall n \in \mathbf{N} \quad r_{n+1}&=&3r_n
   \end{array}
   \right.

Voici le programme **Python** correspondant obtenu en descendant
l'algorithme vu en classe et pour lequel j'affiche les 11 premiers
termes de la suite , c'est-à-dire :math:`r_0,` :math:`r_1`,
:math:`\dots` :math:`r_n`.

.. code:: python

    N = input('Entrez un entier N naturel : ')
    r = 4                   # C'est la valeur de r0
    print r                # j'affiche r0 comme demandé
    for j in range(1,N+1): 
        r = 3*r             
        print(r)            


.. parsed-literal::

    Entrez un entier N naturel : 10
    4
    12
    36
    108
    324
    972
    2916
    8748
    26244
    78732
    236196


Des commentaires sur ce script :

1. la liste des entiers de :math:`1` à :math:`N` s'obtient avec la
   commande **range(1,N+1)**. Faites bien attention : **range(a,b)**
   prend les entiers de l'intervalle :math:`[a,b[` : **b** est exclu, si
   bien que dans la liste **range(a,b)**, il y a **b-a** éléments.

2. On peut se demander quel est le type de **range(a,b)**. Regardons :

.. code:: python

    type(range(1,5))




.. parsed-literal::

    list



1. C'est un objet de type *liste*, qui correspond en mathématiques au
   type *liste*, appelé indifféremement :math:`p`-liste, ou
   :math:`p`-upplet. On a donc ici un nouveau type d'objet **Python**.

2. Sous **Python 3**, **range(a,b)** n'est pas de type *liste*, mais de
   type *itérable*.

Exemple 2
~~~~~~~~~

Afficher 25 fois la phrase "Merci vous êtes bien gentil !"

.. code:: python

    for j in range(1,25):
        print('Merci vous êtes bien gentil')


.. parsed-literal::

    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil
    Merci vous êtes bien gentil


Variante de l'exemple 2
~~~~~~~~~~~~~~~~~~~~~~~

On voudrait afficher en plus dans la phrase le segment : 'pour la
:math:`j`-ème' fois avec la valeur courante de :math:`j`.

.. code:: python

    for j in range(1,26):
        print('Merci pour la ' + str(j)+ 'eme fois !')


.. parsed-literal::

    Merci pour la 1eme fois !
    Merci pour la 2eme fois !
    Merci pour la 3eme fois !
    Merci pour la 4eme fois !
    Merci pour la 5eme fois !
    Merci pour la 6eme fois !
    Merci pour la 7eme fois !
    Merci pour la 8eme fois !
    Merci pour la 9eme fois !
    Merci pour la 10eme fois !
    Merci pour la 11eme fois !
    Merci pour la 12eme fois !
    Merci pour la 13eme fois !
    Merci pour la 14eme fois !
    Merci pour la 15eme fois !
    Merci pour la 16eme fois !
    Merci pour la 17eme fois !
    Merci pour la 18eme fois !
    Merci pour la 19eme fois !
    Merci pour la 20eme fois !
    Merci pour la 21eme fois !
    Merci pour la 22eme fois !
    Merci pour la 23eme fois !
    Merci pour la 24eme fois !
    Merci pour la 25eme fois !


Encore une amélioration supplémentaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On voudrait qu'au premier affichage, **Python** affiche : *"pour la 1ère
fois"* et non pas : *"pour la 1ème fois"*. On pense tout de suite à
implémenter un **if** pour réaliser cela. Ici, c'est inutile, puisqu'il
suffit d'écrire :

.. code:: python

    print ('Merci pour la première fois')
    for j in range(2,26):
        print('Merci pour la ' + str(j)+ 'ème fois !')


.. parsed-literal::

    Merci pour la première fois
    Merci pour la 2ème fois !
    Merci pour la 3ème fois !
    Merci pour la 4ème fois !
    Merci pour la 5ème fois !
    Merci pour la 6ème fois !
    Merci pour la 7ème fois !
    Merci pour la 8ème fois !
    Merci pour la 9ème fois !
    Merci pour la 10ème fois !
    Merci pour la 11ème fois !
    Merci pour la 12ème fois !
    Merci pour la 13ème fois !
    Merci pour la 14ème fois !
    Merci pour la 15ème fois !
    Merci pour la 16ème fois !
    Merci pour la 17ème fois !
    Merci pour la 18ème fois !
    Merci pour la 19ème fois !
    Merci pour la 20ème fois !
    Merci pour la 21ème fois !
    Merci pour la 22ème fois !
    Merci pour la 23ème fois !
    Merci pour la 24ème fois !
    Merci pour la 25ème fois !


Exercice 18 p. 27 du poly
-------------------------

Calcul et affichage des termes de la suite :math:`(u_n)` donnée par
:math:`u_n = n^2 + 2^{\cos\left( \dfrac{n\pi}{2}\right)}` jusqu'à un
rang :math:`N` fixé par l'utilisateur.

Essayez de présenter l'affichage des termes dans une phrase du style :

**u\_## = la valeur du terme courant**

et les **##** sont remplacés par la valeur courante de l'indice.

.. code:: python

    from math import cos,pi
    N = input('Entrez un entier N : ')
    for j in range(0,N+1):
            a = j**2 + 2**cos(j*pi/2)
            print('u_'+str(j)+' = '+ str(a))


.. parsed-literal::

    Entrez un entier N : 10
    u_0 = 2.0
    u_1 = 2.0
    u_2 = 4.5
    u_3 = 10.0
    u_4 = 18.0
    u_5 = 26.0
    u_6 = 36.5
    u_7 = 50.0
    u_8 = 66.0
    u_9 = 82.0
    u_10 = 100.5


Exercice 19 p.27
----------------

Calcul et affichage des termes de la suite donnée par :

.. math::

    \left\{ \begin{array}{rcl}
   u_1 &=& 1 \\
   \forall n \in \mathbf{N}^\star \quad u_{n+1}&=&2n^2 + u_{n} +4
   \end{array}
   \right.

Attention, la suite :math:`(u_n)` est définie à partir du rang 1.

.. code:: python

    N = input('Entrez un entier N : ')
    u = 1
    print('u_1 = 1')
    for i in range(1,N):
        u = 2*i**2+ u + 4
        print('u_'+str(i+1)+' = '+ str(u))    


.. parsed-literal::

    Entrez un entier N : 10
    u_1 = 1
    u_2 = 7
    u_3 = 19
    u_4 = 41
    u_5 = 77
    u_6 = 131
    u_7 = 207
    u_8 = 309
    u_9 = 441
    u_10 = 607


**Attention.** Ici, la valeur de la variable de boucle est
importante car elle intervient dans le calcul du terme courant de la
suite. Il n'est donc pas indifférent d'écrire **range(1,N)** ou
**range(2,N+1)**, bien que l'on fasse dans les deux cas le bon nombre
d'itérations.


.. sidebar:: À retenir

 Pour programmer le calcul des termes consécutifs d'une suite récurrente donnée par la  règle  :math:`u_{n+1} = f(u _n)`,la clé est 
 d'initialiser une variable :math:`u` au terme initial de la suite puis de 
 répéter l' affectation :math:`\fbox{$u \leftarrow f(u)$}`




Exercice 20 p.28 : calcul de :math:`n!`
---------------------------------------


.. code:: python

    N = input('Entrez un entier N : ')
    F = 1
    for k in range(1,N+1): 
        F = F * k
    print(F)


.. parsed-literal::

    Entrez un entier N : 5
    120


**Remarque.**

1. En toute rigueur, comme vu dans le cours d'algorithmique, il faudrait
   distinguer les cas :math:`N=0` et :math:`N \neq 0` par un schéma
   conditionnel.
2. Néanmoins, en **Python**, si :math:`N=0`, **range(1,N+1)** devient
   **range(1,1)**, qui est vide : **Python** ne rentre donc pas dans la
   boucle. La valeur affichée est bien **F = 1** qui est :math:`0!`.
3. En conclusion : ce programme calcule donc correctement la valeur de
   :math:`n!` dans tous les cas : il est donc inutile d'implémenter un
   **if**.

Dernier exercice
----------------

Dans un script que vous appelerez **binome.py** :

1. Construire une fonction **fact(n)** qui calcule :math:`n!`

2. Compléter le fichier avec un script demandant à l'utilisateur
   d'entrer un entier :math:`N`, et qui affiche les coefficients de la
   ligne :math:`N` du triangle de Pascal.

Je rappelle que la ligne :math:`n` du triangle de Pascal contient les
coefficients binomiaux
:math:`\left(\begin{array}{c} {n}\\k \end{array}\right)` pour :math:`k`
allant de :math:`0` à :math:`n` et que

.. math::

   \left(\begin{array}{c}
   {n}\\k \end{array}\right) = \dfrac{n!}{k! \times (n-k)!}

Il y a donc :math:`n+1` coefficients à afficher.

Par exemple, la ligne :math:`n=3` du triangle est : :math:`1` :math:`3`
:math:`3` :math:`1`

.. code:: python

    # 1. Je définis la fonction factorielle :
    def fact(n): #consiste à modifier le script précédent
        """fonction qui calcule la factorielle de n
        """
        f = 1
        for j in range(1,n+1):
            f = f * j
        return f
    
    # 2. Interaction avec l'utilisateur :
    N = input('Entrez un entier N : ')
    for k in range(0,N+1):
        k_parmi_n = fact(N)/(fact(k)*fact(N-k)) # je donne un nom explicite à ma variable
        print(k_parmi_n)


.. parsed-literal::

    Entrez un entier N : 6
    1
    6
    15
    20
    15
    6
    1


**Remarques** 

1. Il est maladroit d'utiliser la fonction factorielle pour calculer les coefficients binomiaux. Cet exercice est purement académique.

2. Si vous êtes ambitieux, vous pouvez améliorer ce programme pour qu'il
   produise l'affichage de toutes les lignes du triangle de Pascal
   jusqu'à la ligne :math:`N` : il y aura donc deux boucles imbriquées.

3. Les plus ambitieux peuvent tenter de réaliser un programme qui, dans
   un premier temps, linéarise :math:`\cos^{2p}(x)`, puis
   :math:`\cos^{p}(x)`, et enfin :math:`\sin^q(x)`.
