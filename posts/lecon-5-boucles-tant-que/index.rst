.. class:: alert alert-info pull-right

.. contents::

Principe de la boucle tant que
------------------------------

les boucles **tant que** réalisent aussi des processus itératifs.
Tputefois, à la différence des boucles **pour**, *le nombre d'itérations
n'est pas connu à l'avance, ce qui fait que la sortie de boucle est
soumise à un* **test booléen**. Cette condition constitue le *test
d'arrêt* de la boucle.

**Exemple 1.** Soit :math:`M` un réel donné, et :math:`(S_n)` une suite
tendant vers :math:`+\infty`. Trouver le premier terme parmi
:math:`S_0`, ..., :math:`S_{500}` qui est strictement plus grand que
:math:`M` si il existe.

Trois recommandations pour la construction d'une boucle tant que
----------------------------------------------------------------

1. Il vaut mieux formaliser la condition de sortie de boucle pour ne pas
   se tromper dans la rédaction correcte du test de boucle : on écrit la
   condition de sortie, et sa négation donne la condition de boucle.

2. (*obligatoire*)N'oubliez pas d'actualiser les variables apparaissant
   dans le test d'arrêt **avant** la sortie de la boucle.

3. (optionnel) : stockez vos conditions booléennes dans des variables
   auxquelles vous donnez des noms d'action. N'oubliez dans ce cas
   d'actualiser ces variables booléennes comme le dit 2.

**Exemple2.** Sur l'\ **exemple 1** précédent, on sort de la boucle dès
que :

    le :math:`n`-ème terme :math:`S_n` vérifie :math:`S_n>M ` **ou** que
    l'indice :math:`n` vérifie :math:`n>500`.

Par négation, le test de boucle est donc :

    .. math:: S_n \le M \quad \textbf{et } \quad n\le 500

Premier exercice (d'après poly exemple 5 p.34)
----------------------------------------------

Avant tout, créez un dossier ``TP05`` dans lequel vous stockerez tous
vos scripts.

On considère la suite :math:`(S_n)_{n\ge 1}` donnée par :
:math:`S_n =\displaystyle\sum_{k=1}^n \dfrac{1}{k}`. On admet que cette
suite tend vers :math:`+\infty`.

1. Créer une fonction ``premier_rang(M)`` qui prend en entrée un
   flottant ``M``, et retourne le premier indice :math:`n \le500` tel
   que :math:`S_n>M`. Si jamais cet indice n'existe pas (ce qui est le
   cas si :math:`S_{500} \le M`), ``premier_rang(M)`` retournera la
   phrase ``'aucun des 500 premiers termes ne dépasse M.'``

2. Vérifier avec ce qui a été fait en classe que ``premier_rang(2.15)``
   vaut ``5``.

.. code:: python

    def premier_rang(M):
        """M : flottant.
            calcule le plus petit entier n tel que 1 + 1/2 +...+ 1/n > M  
            si <n> n'existe pas, la fonction retourne une phrase.
        """
        S = 1
        n = 1
        while n <=500 and S<=M:
            n += 1 # je passe à l'entier suivant  (n+=1 signifie : n = n+1)
            S += 1./n # je n'ai pas envie d'importer la division
        if S>M:       # A ce stade, on est sorti de la boucle ...
            return n  # ... pour une des deux raisons. 
        else:
            return 'les  500 premiers termes sont plus petits que '+str(M)
        

.. code:: python

    premier_rang(2.15)




.. parsed-literal::

    5



\*\* Remarque.\*\* Si la consigne avait demandé seulement d'afficher la
phrase ``les  500 premiers termes sont plus petits que M``, un **print**
aurait convenu. Mais dans ce cas, la fonction ne produit aucun objet en
sortie si tous les termes restent inférieurs à :math:`M`.

La fameuse suite de Syracuse
----------------------------

Écrire une fonction ``Syracuse(x,n)`` qui prend en entrée : deux entiers
``x`` et ``n``, et calcule et affiche les termes :math:`u_0,\dots,u_n`
de la suite dite de Syracuse définie par :

.. math::

    \left\{ \begin{array}{rcl}
                   u_0&=& \texttt{x} \\
                   u_{n+1}&=& \dfrac{u_n}{2}   \text{ si } u_n \text{ est pair}\\
                   && 3u_n +1 \text{ sinon }
                   \end{array}\right.

**Rappel.** On peut tester simplement la parité d'un entier :math:`p` en
calculant :math:`(-1)^p`.

**Remarques.**

1. En **Python**, le reste de la division euclidienne de **n** par 2 par
   exemple se calcule avec la commande : **n%2**.

2. La fonction **syracuse** ne fait que des affichages. Il n'y aura donc
   pas d'objet généré en sortie (donc pas de **return** dans la
   fonction).

3. Ici, le nombre d'itérations est connu : il n'y aura pas de tant que !

.. code:: python

    def syracuse(x,n):
        """ calcule et affiche les n premières escales du vol numéro x. 
        Attention : pas d'objet en sortie """
        u = x
        print(u)
        for k in range(0,n): #Pas de boucle tant que ici !
            if (-1)**u == 1: # on teste la parité de l'entier x_k
                u = u/2
            else:
                u = 3*u+1
            print u

.. code:: python

    syracuse(7,5)


.. parsed-literal::

    7
    22
    11
    34
    17
    52


Modifier la fonction ``syracuse`` en une fonction ``syracuse2`` de sorte
que cette nouvelle fonction retourne en sortie une chaîne de caractères
contenant les valeurs de :math:`u_0,\dots,u_n`

.. code:: python

    def syracuse2(x,n):
        """ donne la chaine de caractères contenant  les
            n premières escales du vol numéro x. 
        """
        u = x
        chaine = str(x)        # au début, la chaine contient u_0.
        for k in range(0,n):  #Pas de boucle tant que ici !
            if (-1)**u == 1:  # On teste la parité de l'entier u_k.
                u = u/2
            else:
                u = 3*u+1
            chaine +=' '+str(u)  # je concatène dans ma chaine ... 
                                 # ... le dernier terme calculé.  
        return chaine           # Ne pas oubler de retourner la chaine

.. code:: python

    syracuse2(7,5)




.. parsed-literal::

    '7 22 11 34 17 52'



**Exercice.** Faire une fonction ``affiche_escales(N,k)`` qui affiche
les :math:`k` premières escales des vols 1,2,...,\ ``N``, où ``N`` est
un entier rentré par l'utilisateur

.. code:: python

    def affiche_escales(N,k):
        """ affiche les k premières escales des vols 1 à N"""
        for j in range(1,N+1):
            print(syracuse2(j,k))

.. code:: python

    affiche_escales(10,20)


.. parsed-literal::

    1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2
    2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4
    3 10 5 16 8 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4
    4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1
    5 16 8 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1
    6 3 10 5 16 8 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1
    7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 4 2 1 4
    8 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2
    9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 4
    10 5 16 8 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2


On constate que les 10 premiers vols bouclent sur le triangle
:math:`1 \to 4 \to 2`. On pense que c'est le cas pour tous les vols,
mais on ne sait pas le prouver.

Combien de temps dure le vol ?
------------------------------

Construire une fonction ``duree_du_vol(x)`` qui prend un entier ``x`` et
retourne le premier rang ``n`` pour lequel :math:`u_n=1`. Par exemple,
``duree_du_vol(7)`` devrait valoir ``16``. 

.. code-block:: python
  :number-lines:

    def duree_du_vol(x):
        """ on considère la suite la suite de Syracuse de premier
            terme x. Cette fonction calcule le premier rang n au bout
            duquel un terme de la suite vaut 1.  
            Par exemple  : duree_du_vol(1) vaut 0,
                           duree_du_vol(7) vaut 16.
        """
        duree = 0 
        u=x
        while u != 1:
            duree += 1
            if (-1)**u == 1: # on teste la parité de l'entier x_k
                u = u/2
            else:
                u = 3*u+1
        return duree


Quelle est la durée du vol 714 ?

.. code:: python

    duree_du_vol(714)




.. parsed-literal::

    33



**Remarque.** On peut créer une fonction pour éviter de remettre les
lignes 12-15 qu'on a tapé bien plus d'une fois (et c'est tout l'intérêt
des fonctions).

.. code:: python

    def transfo(z):
        if (-1)**z == 1: # on teste la parité de l'entier x_k
            return   z/2
        else:
            return  3*z+1
        

La fonction ``duree_du_vol`` prend alors la forme suivante

.. code:: python

    def duree_du_vol(x):
        duree = 0 
        u=x
        while u != 1:
            duree += 1
            u = transfo(u)
        return duree

On peut toujours tester cette variante :


.. code:: python

    duree_du_vol(7)




.. parsed-literal::

    16



Quel est le premier vol dont la durée est 111 ?
-----------------------------------------------

**Exercice.** Créer une fonction ``premier_vol(t)`` qui détermine le
premier vol dont la durée est ``t``.

.. code:: python

    def premier_vol(t):
        vol = 1                    # je considère le vol  1
        duree = duree_du_vol(vol)  # je calcule sa durée
        while duree !=t:          # Si elle ne vaut pas t
            vol+=1                 # je passe au vol suivant
            duree = duree_du_vol(vol)
        return vol

.. code:: python

    premier_vol(111)




.. parsed-literal::

    27



Ainsi le vol 27 a une durée de 111. Et tous les vols précédents ont une
durée autre.
