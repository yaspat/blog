..title: Objets et variables en Python
..slug: objets-et-variables
.. date: 2015-08-20 13:39:19 UTC+02:00
.. tags: python, objets, variables
.. category: 
.. link: 
.. description: 
.. type: text


Leçon 1 : Objets principaux et variables
========================================

.. class:: alert alert-info pull-right

.. contents::


Objet de cette introduction :

1. Prendre connaissances de quelques objets manipulables en ``Python``

   1. Quelques types de nombres
   2. Les chaînes de caractères

2. Quelques manipulations simples sur les chaînes de caractères.

.. raw:: html

   <!-- TEASER_END -->

Les nombres
-----------

Les entiers
~~~~~~~~~~~

Ce sont les éléments de l'ensemble :math:`\mathbf{N}` que vous
connaissez. Les opérations arithmétiques de base sont disponibles.
Faites simplement attention au fait que la puissance se code ``**``

.. code:: python

    1




.. parsed-literal::

    1



.. code:: python

    1+2




.. parsed-literal::

    3



.. code:: python

    2**5 # 2 puissance 5. Rem : On peut saisir des commentaires dans la console en les précédant d'un dièse #. 




.. parsed-literal::

    32





La commande ``type`` permet de connaître le type d'un objet dans la
machine

.. code:: python

    type(1)




.. parsed-literal::

    int



Python répond ``int`` : entier

Vous pouvez effectuer les opérations arithmétiques usuelles sur les
entiers. Attention, la division se fait alors en nombres entiers :

.. code:: python

    2/3 # je calcule.




.. parsed-literal::

    0



C'est normal : on obtient le quotient de la division entière
(euclidienne)

Les flottants
~~~~~~~~~~~~~

Ce sont les approximations des nombres réels (et pas les réels eux-mêmes
!). La plupart des réels ont en effet un développement décimal illimité.
Il est donc impossible de stocker toutes ces décimales dans la mémoire
de la machine, qui elle, est limitée. Ce qui pose intrinsèquement le
problème de la précision des calculs.

.. code:: python

    from math import sin, pi # Je demande à Python de charger la fonction sinus
                              # et la constante pi

.. code:: python

    sin(pi/4) 




.. parsed-literal::

    0.7071067811865475



Le développement décimal de :math:`\sqrt{2}` est illimité alors que le
résultat affiché est donné avec troncature. Le calcul qui suit est
instructif, puisqu'il nous dit que :math:`\sin(\pi)` n'est pas nul (!) :

.. code:: python

    sin(pi)




.. parsed-literal::

    1.2246467991473532e-16



**Morale.** soyez critiques sur les résultats numériques que vous
obtenez. La précision par défaut de ``Python`` est de l'orde de
:math:`10^{-16}`. En ``Python``, ``e-16`` siginifie : :math:`10^{-16}`

.. code:: python

    2 + 1e-16 # Combien ça fait pour Python ?




.. parsed-literal::

    2.0



On constate qu'à :math:`10^{-16}` prés, ``Python`` ne fait pas la
différence.

**Question :** le nombre :math:`2` est un entier ou un flottant ?
Utilisons la commande ``type``

.. code:: python

    type(2)




.. parsed-literal::

    int



**Question :** Mais si je veux travailler avec le nombre
:math:`2\in\mathbf{R}` et non pas l'entier :math:`2\in \mathbf{N}` ?

**Réponse :** placer de force le point décimal ( rappel : dans les pays
anglo-saxons, le séparateur décimal est le point ``.``, et non pas la
virgue ``,`` . ``Python`` comprendra que le nombre :math:`2` est vu
comme un flottant.

.. code:: python

    type(2.)




.. parsed-literal::

    float



``float`` signifie : flottant. Voyons ce que donne la division entre
flottants :

.. code:: python

    2./3.




.. parsed-literal::

    0.6666666666666666



En précisant que l'on effectue la division entre flottants, ``Python``
comprend que le résultat de cette dernière doit être donné en type
``float``.

\*\* Remarque. \*\* En ``Python 3.``, la division est *toujours*
considérée comme divisione de flottants.

Les caractères et chaînes de caractères
---------------------------------------

Définitions
~~~~~~~~~~~

1. Un *caractère* est en gros n'importe quel symbole accessible par une
   (ou des combinaisons) de touches du clavier.
2. Une *chaîne de caractères* est la concaténation (juxtaposition, ou
   assemblage) de caractères.
3. Un caractère est aussi une chaîne de caractères.
4. Pour que ``Python`` identifie une chaîne de caractères, on les
   entoure d'un délimiteur, qui est au besoin l'apostrophe ``'`` ou les
   guillemets ``"`` . 

**Exemple.**

.. code:: python

    bonjour # Ce n'est pas une chaîne de caractères : pas de délimiteurs.


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-dafbe8cf1de0> in <module>()
    ----> 1 bonjour # Ce n'est pas une chaîne de caractères : pas de délimiteurs.
    

    NameError: name 'bonjour' is not defined


On obtient un message d'erreur. En effet, ``Python`` interprète ce mot
comme un nom de variable, on n'a pas créé de variable. d'où l'erreur.
Ajoutons alors les délimiteurs comme dit précédemment :

.. code:: python

    'bonjour'




.. parsed-literal::

    'bonjour'



Cette fois, pas d'erreur. Je vais vérifier que c'est bien une chaîne de
caractères :

.. code:: python

    type('bonjour')




.. parsed-literal::

    str



Le mot ``str`` est l'abréviation de ``string`` (chaîne en anglais). On a
généré une chaîne de caractères.


**Question \:** Comment je fais si je veux des apostrophes dans ma chaîne
? Si je tape par exemple :

.. code:: python

    'l'arbre' 


.. code-block::


      File "<ipython-input-4-b647b3b75403>", line 1
        'l'arbre'
               ^
    SyntaxError: invalid syntax



Il y a un problème de *syntaxe* \: ``Python comprend`` : la chaîne `'l'`,
puis des caractères. Il ne sait pas quoi faire de ces derniers. Le mieux
dans ce cas est d'utiliser des guillemets :

.. code:: python

    "l'arbre"




.. parsed-literal::

    "l'arbre"



**Question \:** Mais comment je fais si j'ai à la fois des guillemets
et des apostrophes ? Par exemple, une chaîne de caractères comme \:
'il a dit : "je t'aime"' ?



**Réponse \:** Il faut faire jouer aux caractères ``'`` et ``"`` leur
rôle naturel. Pour cela, on introduit une *séquence d'échappement* : le
caractère s'échappe ainsi de son rôle de délimiteur. En ``Python``, on
échappe un caractère en le faisant précéder d'un ``backslash`` \: ``\``
(touches ``alt Gr`` + ``8`` sur les claviers français).

.. code:: python

    print('il a dit : "je t\'aime"') # Pas besoin d'échapper les guillemets : 
                                     # le délimiteur est l'apostrophe ici.
                                     # la fonction print sert à l'affichage.


.. parsed-literal::

    il a dit : "je t'aime"



**Remarques \:**

 1. L'espace est elle-même un caractère (en imprimerie, espace est féminin !) 
 2. La chaîne de caractères vide est : \"\"



.. code:: python

    #je demande à Python si les chaînes '' et ' ' sont égales
    '' == ' ' # le test d'égalité est codé par ==




.. parsed-literal::

    False



``Python`` a répondu faux : ces deux chaînes sont bien distinctes.

Opérations sur les chaînes de caractères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Je vais considérer la chaîne de caractères suivante :

.. code:: python

    'anticonstitutionnellement'




.. parsed-literal::

    'anticonstitutionnellement'



Comme cette chaîne est longue à saisir, je vais la manipuler en la
stockant dans une variable que j'appelle ``mot`` (voir plus tard pour
les variables):

.. code:: python

    mot = 'anticonstitutionnellement'

.. code:: python

    print(mot)


.. parsed-literal::

    anticonstitutionnellement


.. code:: python

    type(mot)




.. parsed-literal::

    str



Accession à un caractère ou une sous-chaîne
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les caractères dans une chaîne sont numérotés à partir de ``0``

.. code:: python

    mot[0] # Python le premier caractère de la chaîne




.. parsed-literal::

    'a'



.. code:: python

    mot[-1] # Le dernier caractère




.. parsed-literal::

    't'



.. code:: python

    mot[-2] # Le deuxième caractère en partant de la fin




.. parsed-literal::

    'n'



.. code:: python

    mot[0:5] # les cinq premiers caractères




.. parsed-literal::

    'antic'



.. code:: python

    mot[3:8] # Je veux la sous-chaîne des caractères numéro 3,4,5,6 et 7




.. parsed-literal::

    'icons'



**Règle.** Dans ``mot[a:b]``, il y a ``b-a`` caractères.

Combien y a-t-il de lettres dans ``anticonstitutionnellement`` ?

.. code:: python

    len(mot) # len est l'abréviation de length (longueur)




.. parsed-literal::

    25



J'extrais de ce mot le mot 'constitution'

.. code:: python

    mot[4:16]




.. parsed-literal::

    'constitution'



Je demande si deux ``l`` se suivent :

.. code:: python

    'll' in mot  # Est-ce que la chaîne `ll` se trouve dans le mot ?




.. parsed-literal::

    True



.. code:: python

    'oui' in mot # on ne trouve pas 'oui' dans le mot.




.. parsed-literal::

    False



Concaténation de chaînes
^^^^^^^^^^^^^^^^^^^^^^^^

On utilise pour cela le ``+``

.. code:: python

    'bonjour'+' Monsieur' # Noter l'espace avant le M de Monsieur




.. parsed-literal::

    'bonjour Monsieur'



.. code:: python

    'bonjour'+'Monsieur'




.. parsed-literal::

    'bonjourMonsieur'



On peut aussi utiliser le ``*<n>`` pour répliquer ``<n>`` fois la
chaîne, ``<n>`` étant un entier. Par exemple, si je veux écrire 60 fois
``tictac`` :

.. code:: python

    'tictac '*60




.. parsed-literal::

    'tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac tictac '



Variables
---------

Les variables servent à manipuler plus aisément les objets de la
machine.

1. (définition informelle) : une variable est l'association d'un nom et
   d'un objet. Ce dernier est stocké dans une région localisée de
   l'espace mémoire de la machine.
2. L'objet associé à la variable s'appelle la *valeur courante* de la
   variable.

Opérations sur les variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On peut :

1. Créer une variable (opération de création ou initialisation d'une
   variable)
2. Modifier le contenu d'une variable (c'est-à-dire sa valeur courante).
   Cette opération s'appelle *affectation* ou *mise à jour* de la
   variable.
3. Utiliser le contenu d'une variable (opération nommée : *appel* de la
   variable)
4. Supprimer une variable.

**Remarque.** En dehors du ``_`` (le "tiret du 8"), ou du point ``.``,
les caractères spéciaux (lettres accentuées, espaces) sont interdits.
Les noms de variables constitués uniquement de chiffres sont interdits
pour des raisons évidentes.

Création de variable
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    toto # Pour l'instant, la variable appelée toto n'existe pas. Pour preuve :


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-47-11a3e2290843> in <module>()
    ----> 1 toto
    

    NameError: name 'toto' is not defined


.. code:: python

    toto = ' bonjour ' # la valeur courante est la chaîne de caractères ' bonjour '

.. code:: python

    type(toto)




.. parsed-literal::

    str



affectation
~~~~~~~~~~~

Pour stocker l'entier :math:`2` dans une variable qu'on appelle
``toto``, on tape :

.. code:: python

    toto = 2

\*\* Attention : \*\* Le nom de la variable est à gauche du symbole
``=`` et à droite, l'objet.

.. code:: python

    print(toto)


.. parsed-literal::

    2


La nouvelle valeur courante affectée écrase donc l'ancienne.

Appel
~~~~~

On récupère le contenu d'une variable en l'appelant par son nom.

.. code:: python

    3 + toto # Qu'y avait-il dans toto ? L'appel se fait simplement en utilisant le nom de la variable




.. parsed-literal::

    5



.. code:: python

    '3' + toto # Soyez rigoureux et analysez la syntaxe


::


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-dc348e9b8641> in <module>()
    ----> 1 '3' + toto # Soyez rigoureux et analysez la syntaxe
    

    TypeError: cannot concatenate 'str' and 'int' objects


**Explication** (bien comprendre). ``Python`` analyse ainsi
l'instuction:

1. Il commence par voir ``3``. Grâce aux apostrophes, il sait que c'est
   une chaîne de caractères.
2. Ensuite, il voit un ``+`` : comme il avait juste avant une chaîne de
   caractères, il comprend que ce ``+`` désigne la concaténation de
   chaînes et pas l'addition des entiers (ou des flottants ou autre).
3. Après ce ``+``, Python s'attend à trouver une chaîne de caractères.
   Or il trouve ``toto``. Comme il n'y a pas délimiteurs autour, il
   comprend que c'est un *appel* de variable.
4. Comme ``toto`` contient un entier, ``Python`` ne peut rien
   concaténer.

Le message d'erreur dit bien : tu ne peux pas concaténer chaîne et
entier. Il faut donc convertir l'entier ``toto`` en chaîne. La commande
``str(objet)`` converit l'objet ``objet`` en chaîne de caractères.

.. code:: python

    '3'+str(toto)




.. parsed-literal::

    '32'



.. code:: python

    '3'+'toto' # Ce n'est pas la même chose que ce qui précède




.. parsed-literal::

    '3toto'



**Ce qui suit est à bien comprendre aussi.**

.. code:: python

    toto = 2  #1
    toto = toto + 8 #1 

**Explication.**

1. Dans ``#1`` on a effectué une actualisation de variable : ``toto``
   contient l'entier :math:`2`.
2. Dans ``#2``, c'est encore une actualisation de la variable toto
   puisque l'instruction commence par ``toto =``
3. Le membre de droite contient :
     
    A. Un appel de la variable ``toto`` : son contenu est :math:`2` d'après ``#1`` 
    B. Une addition d'entiers (puisque le ``+`` est coordonné à l'entier ``toto``) 
    C. cette addition se fait entre :math:`2` et :math:`8`.

4. À la fin, on ``toto`` devrait donc être actualisé à la valeur
   :math:`10`. Vérifions :

.. code:: python

    print(toto)


.. parsed-literal::

    10

