.. title: Informatique : Leçon 6. Tuples  - Listes 
.. slug: lecon-6-tuples-listes
.. date: 2015-12-17 21:36:59 UTC+01:00
.. tags: python, informatique, tuples, listes, chaînes de caractères, leçon, split, join
.. link: 
.. description: 
.. type: text
.. category: informatique

.. class:: alert alert-info pull-right

.. contents::



C'est quoi un tuple ?
~~~~~~~~~~~~~~~~~~~~~

1. C'est un nouveau type d'objets. Il correspond en maths, aux
   :math:`p`-listes ou :math:`p`-upplets : suites ordonnées de :math:`p`
   objets.

2. En **Python**, les tuples sont délimités, comme en maths, par des
   parenthèses.

3. En maths, les éléments d'un :math:`p`-upplet s'appellent les
   *coordonnées* ou les *composantes* du :math:`p`-upplet. En
   **Python**, les éléments d'un tuple sont appelés les *items* du
   tuple. Ils sont séparés par des virgules, comme en maths.


.. raw:: html    

	 <!-- TEASER_END-->



+----------------------------------------------+------------------------------------------+
| Maths                                        | Analogue **Python**                      |
+==============================================+==========================================+
| :math:`p`-upplet = :math:`p`-liste           | tuple                                    |
+----------------------------------------------+------------------------------------------+
| coordonnée ou composante                     | item                                     |
+----------------------------------------------+------------------------------------------+
| délimité par des parenthèses                 | délimité par des parenthèses             |
+----------------------------------------------+------------------------------------------+
| séparateur : la virgule :math:`\mathtt{,}`   | *idem* : la virgule :math:`\mathtt{,}`   |
+----------------------------------------------+------------------------------------------+

Premiers exemples
~~~~~~~~~~~~~~~~~

.. code:: python

    my_first_tuple = ( -3 , 2, 0.5, 0)
    print my_first_tuple


.. parsed-literal::

    (-3, 2, 0.5, 0)


.. code:: python

    type(my_first_tuple)




.. parsed-literal::

    tuple



Ce tuple possède 4 items qui sont des flottants ou des entiers.

\*\* Remarque.\*\* Cela veut dire que dans un tuple, on peut mettre des
items de type divers. En particulier, on peut mêler chaînes de
caractères et flottants, ou même mettre un tuple dans un tuple.

**Exemple.**

.. code:: python

    t1 = ('toto', 25, (1,2.5)) ; type(t1)




.. parsed-literal::

    tuple



Le tuple :math:`\mathtt{t_1}` est un tuple constitué de trois items qui
sont :

1. une chaîne de caractères
2. un entier.
3. un tuple, lui-même constitué d'un entier et d'un flottant.

Nombre d'items d'un tuple
~~~~~~~~~~~~~~~~~~~~~~~~~

Comme pour les chaînes de caractères, pour connaître le nombre d'items
d'un tuple, on utilise la fonction :math:`\mathtt{len}` :

.. code:: python

    t1 = ('toto', 25, (1,2.5))
    len(t1)




.. parsed-literal::

    3



Accès aux items d'un tuple
~~~~~~~~~~~~~~~~~~~~~~~~~~

Comme pour les chaînes de caractères, **les éléments d'un tuple sont
numérotés à partir de 0**, et on peut y faire les mêmes opérations que
dans les chaînes de caractères.

.. code:: python

    t1 = ('toto', 25, (1,2.5))
    t1[-1] # le dernier item




.. parsed-literal::

    (1, 2.5)



.. code:: python

    t1[0] # le premier  item




.. parsed-literal::

    'toto'



\*\* Exercice \*\*. Récupérer le :math:`\mathtt{1}` dans
:math:`\mathtt{t_1}` en une seule instruction.

.. code:: python

    t1 




.. parsed-literal::

    ('toto', 25, (1, 2.5))



.. code:: python

    t1[-1]




.. parsed-literal::

    (1, 2.5)



.. code:: python

    t1[-1][0] # le premier item  du dernier item de t1 ...




.. parsed-literal::

    1



**Remarque**. On a déjà rencontré des tuples, dans la construction des
fonctions, notamment les fonctions qui retournent plusieurs arguments de
sortie.

.. code:: python

    def inutile(x):
        """
        fonction inutile qui prend un réel x et retourne en sortie
        son carré et son cube
        """
        return x**2,x**3 # Deux arguments de sortie x^2 et x^3

.. code:: python

    z = inutile(4) # je calcule inutile(4)
    print(z)


.. parsed-literal::

    (16, 64)


.. code:: python

    type(z)




.. parsed-literal::

    tuple



**Remarque**. En particulier, les parenthèses sont optionnelles dans un
tuple : :math:`\texttt{(x,y)}` est la même chose que
:math:`\texttt{x,y}`.

**Exercice.** Comment construire un tuple ne possédant qu'un seul item,
l'entier 3 par exemple ?

.. code:: python

     x=(3); type(x)




.. parsed-literal::

    int



Ne marche pas. Essayons avec le séparateur : la virgule.

.. code:: python

    x=(3,) # grâce à la virgule on sait qu'on a un tuple

.. code:: python

    type(x)




.. parsed-literal::

    tuple



JE LE REDIS (je ne m'énerve pas, j'explique) : les parenthèses sont
optionnelles :

.. code:: python

    y =  3,
    type(y)




.. parsed-literal::

    tuple



**Remarque.** Un nombre complexe est aussi un tuple. Mais il constitue
en **Python** un type d'objets à part entière.

Une utilisation intéressante des tuples : échange de variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    x = 'toto'
    y = 2

**Solution.** Si j'échange bêtement, j'écrase le contenu d'une variable
par celui de l'autre. L'idée est d'introduire une variable tierce qui
sert de transition :

.. code:: python

    t = x # j'envoie x dans la variable tierce
    x = y # je peux sans scrupules écraser le contenu de x
    y = t # j'envoie dans y le contenu de x.
    
    x,y




.. parsed-literal::

    (2, 'toto')



**Réponse pythonique.** Sous **Python**, les tuples permettent d'éviter
le passage par une variable intermédiaire :

.. code:: python

    x = 'toto'
    y = 2
    
    x,y = y,x
    print x,y


.. parsed-literal::

    2 toto


**Exercice.** Utilisez cette fonctionnalité pour le problème suivant :

Soit :math:`a,b` deux réels donnés et :math:`(u_n)` la suite définie par
:

.. math::

   (R) \qquad \left\{ \begin{array}{rl}
               u_0,u_1  &\text{donnés} \\
              \forall n\in \mathbf{N} &   u_{n+2}+au_{n+1}+bu_n=0.
                  \end{array}\right.

1. Créez une fonction :math:`\texttt{def srl2(a,b,u0,u1,n):}` qui
   retourne en sortie le terme :math:`u_n` de la suite définie par la
   relation :math:`(R)`.

2. Pour vérifier que votre fonction est correctement programée, vérifiez
   que :math:`\texttt{ srl2(-1,-1,0,1,6)}` renvoie :math:`\texttt{8}`.

.. code:: python

    def srl2(a,b,u0,u1,n):
                               # à chaque étape k : 
        u = u0                 # u joue le rôle de u_k
        v = u1                 # v joue le rôle de u_{k+1}
        
        for k in range(0,n-1): # pour avoir u_n, on fait n-1 calculs
                               # successifs
            w = -a*v - b*u
            v,u = w,v          # le nouveau v est le w calculé
                               # le nouveau u est le v d'avant !
        if n==0:
            return u           # le programme doit renvoyer u0
        else:                  # si l'utilisateur rentre n = 0
            return v

.. code:: python

    
    srl2(-1,-1,0,1,6) # C'est la suite de Fibonnaci: u0 = 0, u1 = 1, on demande u6





.. parsed-literal::

    8



Les tuples ne sont pas mutables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Question naturelle.** Est-ce que je peux changer la valeur d'un item
dans un tuple ? Regaronds ! Je reprends le tuple :math:`\mathtt{t_1}` :

.. code:: python

    t1




.. parsed-literal::

    ('toto', 25, (1, 2.5))



Je vais par exemple essayer de remplacer le :math:`\texttt{25}` par un
:math:`\texttt{30}` :

.. code:: python

    t1[1] = 30 # je  remplace le 25 par un 30


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-42-3f7b83bf835b> in <module>()
    ----> 1 t1[1] = 30 # je  remplace le 25 par un 30
    

    TypeError: 'tuple' object does not support item assignment


Le message d'erreur me dit (si on traduit la fin en français) : on ne
peut pas faire d'affectation d'item dans un tuple. Morale : > 1. \*\*
Vous ne pouvez pas modifier un tuple : on dit que les tuples ne sont pas
mutables. ** > > 2. ** De même, les chaînes de caractères ne sont pas
mutables. \*\*

Un autre type voisin des tuples : les listes.
---------------------------------------------

C'est exactement la même chose que les tuples, mais les listes, ont le
bon goût d'être mutables. Du point de vue de la construction d'une
liste, les listes sont délimitées par des crochets.

+------------------------+--------------------+--------------------+
|                        | Tuples en Python   | Listes en Python   |
+========================+====================+====================+
| délimiteurs            | ( )                | []                 |
+------------------------+--------------------+--------------------+
| séparateur des items   | ,                  | ,                  |
+------------------------+--------------------+--------------------+
| mutable                | non                | oui                |
+------------------------+--------------------+--------------------+

Ces deux types d'objets peuvent servir\* suivant les besoins\* à
représenter des :math:`p`-listes mathématiques.

.. code:: python

    t2 = (7,22,11,34,17) # un tuple

.. code:: python

    L2 = [7,22,11,34,17] # ce qui lui correspondrait en termes de listes

Regardons le type :

.. code:: python

    type(L2)




.. parsed-literal::

    list



La plupart des opérations vues sur les tuples ou chaînes de caractères
s'appliquent :

.. code:: python

    len(L2)




.. parsed-literal::

    5



.. code:: python

    L2[-2] # Le deuxième élément de L2 en partant de la fin




.. parsed-literal::

    34



Mutons notre liste en modifiant un coefficient :

.. code:: python

    L2[0] = 10000000 #  Pas de message d'erreur : ma liste a muté !

Vérifions :

.. code:: python

    L2




.. parsed-literal::

    [10000000, 22, 11, 34, 17]



Vous voyez bien que :math:`\mathtt{L2}` est mutable, contrairement à
:math:`\mathtt{t2}`.

\*\* Remarque \*\* On a déjà rencontré des listes :

.. code:: python

    range(1,10)




.. parsed-literal::

    [1, 2, 3, 4, 5, 6, 7, 8, 9]



.. code:: python

    type( range(1,10))




.. parsed-literal::

    list



**Remarque.**

1. En **Python 3**, :math:`\mathtt{range}` n'est plus de type *liste*,
   mais de type *range* (type à part entière).
2. On verra plus tard le problème des clones et des siamois pour les
   listes.

Petite digression sur les mots et les listes. Split et join
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un autre exemple de liste en lien avec le cours de combinatoire, pour
vous rappeler qu'un mot n'est qu'une liste de lettres, et pourquoi on
les identifie dans les raisonnement combinatoires :

.. code:: python

    L3 = ['a','t','t','e','n','t','i','o','n'] # je crée une liste de lettres
    L3




.. parsed-literal::

    ['a', 't', 't', 'e', 'n', 't', 'i', 'o', 'n']



Cela vous évoque sans difficultés le mot : **attention**

**Remarque.**

1. Vous pouvez générer la liste des mots appraissant dans une phrase
   avec :math:`\mathtt{split( )}`

2. inversement, vous pouvez générer la chaîne de caractères avec la
   liste de ses lettres par :math:`\mathtt{join( )}`

.. code:: python

    'a t t e n t i o n'.split() # toutes les séquences séparées par des espaces 
                                # sont splittés et consignées dans une liste 




.. parsed-literal::

    ['a', 't', 't', 'e', 'n', 't', 'i', 'o', 'n']



Inversement, dans une liste de chaînes de caractères, je peux joindre
les chaînes par la séquence que je veux.

.. code:: python

    ''.join(L3) # je relie tous les caractères de la liste
                # par le caractère ''.




.. parsed-literal::

    'attention'



.. code:: python

    '----'.join(L3)  # pourquoi pas ainsi




.. parsed-literal::

    'a----t----t----e----n----t----i----o----n'



