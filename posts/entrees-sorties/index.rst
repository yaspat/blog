.. title: Informatique : Leçon 2
.. slug: entrees-sorties
.. date: 2015-09-16 13:39:19 UTC+02:00
.. tags: python, entrées, sorties, leçon 
.. category: 
.. link: 
.. description: 
.. type: text

Python :  Leçon 2 
==================

.. class:: alert alert-info pull-right

.. contents::


Objet de cette leçon :

1. Connaître les actions d'échange utilisateur-machine.

   a. Les sorties

.. raw:: html     

	 <!-- TEASER_END -->
   
   
   b. Les entrées de caractères

2. Utiliser les notions de la leçon 1.



Sorties
-------

La commande ``print(y)`` affiche l'objet ``y`` à l'écran :

.. code:: python

    print(256) # un nombre


.. parsed-literal::

    256


.. code:: python

    print('yoyo') # une chaîne de caractères


.. parsed-literal::

    yoyo


.. code:: python

    print(ma_variable) # cette variable n'existe pas


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-c53d5fc5091d> in <module>()
    ----> 1 print(ma_variable) # cette variable n'existe pas
    

    NameError: name 'ma_variable' is not defined


On récolte donc, c'était prévisible, un message d'erreur.

Entrées
-------

La commande ``x = input('un texte')`` a pour effet :

1. D'afficher à l'écran la chaîne de caractères ``un texte``
2. De bloquer le prompt de ``Python`` (il est en suspens) : ce dernier
   attend que vous saisissiez une instruction.
3. Stocke votre instruction dans la variable ``x``.

**Remarque.** La variable ``x`` est donc, avec une telle instruction :

1. Soit actualisée si elle existait auparavant.
2. Soit initialisée si elle n'existait pas avant.

**Question.** mais dans ce cas, quel est le type de l'objet contenu dans
``x`` ?

**Réponse.** Essayons. Tapez ce qui suit dans la console et répondez ce
que vous voulez :

.. code:: python

    prenom = input("Comment t'appelles-tu ?")


.. parsed-literal::

    Comment t'appelles-tu ?58


**Remarque.** Si des points de supension ``...`` s'affichent, c'est que
vous avez ouvert un délimiteur sans le fermer. Typiquement : ``(`` ou
``[``. Vous ne pouvez pas répondre à la requête et récupérer la main
tant que vous n'avez pas fermé votre délimiteur. Fermez une parenthése
pour reprendre la main et ressaisissez votre instruction.

Vous pouvez constater que j'ai saisi un objet de type entier. Voyons
comment ``Python`` le considère :

.. code:: python

    type(prenom)




.. parsed-literal::

    int



Il semble que Python considère le type de l'objet entré en réponse.
Vérifions :

.. code:: python

    prenom = input("Comment t'appelles-tu ?")


.. parsed-literal::

    Comment t'appelles-tu ?'Miguel'


.. code:: python

    type('prenom')




.. parsed-literal::

    str



Dernier essai :

.. code:: python

    prenom = input("Comment t'appelles-tu ?")


.. parsed-literal::

    Comment t'appelles-tu ?Miguel


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-8ccfe9f58e52> in <module>()
    ----> 1 prenom = input("Comment t'appelles-tu ?")
    

    /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/IPython/kernel/zmq/ipkernel.pyc in <lambda>(prompt)
        145             self._sys_eval_input = builtin_mod.input
        146             builtin_mod.raw_input = self.raw_input
    --> 147             builtin_mod.input = lambda prompt='': eval(self.raw_input(prompt))
        148         self._save_getpass = getpass.getpass
        149         getpass.getpass = self.getpass


    /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/IPython/kernel/zmq/ipkernel.pyc in <module>()


    NameError: name 'Miguel' is not defined


Le message d'erreur est :``name 'Miguel' is not defined``. Python
considère que Miguel est le nom d'une variable. Or, elle n'a jamais été
initialisée.

**Exercice** Dans l'éditeur de Spyder (et pas la console !) écrire
un Dialogue dans un fichier que vous nommerez ``myfirst.py`` et que vous
sauvegarderez dans un dossier nommé ``TP01`` que vous placerez dans
votre dossier ``Python`` (ce dernier dossier est créé par défaut et se
trouve dans trouve dans votre dossier ``Mes Documents``).

On veut un dialogue avec Python qui :

1. Vous dit ``"Bonjour Biwane, quel est ton nom ?"``
2. Enregistre votre réponse dans une variable nommée ``prenom``.
3. Vous dit ensuite : ``" Quel âge as-tu ?"``
4. Enregistre votre réponse dans une variable nommée ``age``.
5. Répond : ``" [prenom], tu es né en [votre année de naissance]".``

Voici la solution :

.. code:: python

    prenom = input(u'Bonjour Biwane, quel est ton prénom ?')
    age = input(u'Quel est ton âge ?')
    print(prenom  + u' tu es né(e) en ' + str(2015-age)+ '!')


.. parsed-literal::

    Bonjour Biwane, quel est ton prénom ?'Toto'
    Quel est ton âge ?18
    Toto tu es né(e) en 1997!


**Commentaires**

0. Si votre console est bloquée, cliquer sur la petite icône en haut à
   droite sur la console et redémarrez lz noyau. Réexécutez avec la
   touche ``F5``

1. félicitations, vous avez créé votre premier script.
2. Ce script comporte plusieurs défauts ou limitations.

   a. Quand vous entrez votre prénom, vous êtes obligé de taper les
      guillemets pour faire savoir à Python que vous entrez une chaîne
      de caractères.

   b. Les caractères accentués s'affichent mal.

   c. Quand la question de l'âge est posée, on a envie de répondre p. ex
      18 ans, et pas 18.

**Solutions proposées**

**Réponse à 3. a)** La commande ``raw_input`` fait comme ``input`` à la
différence que l'entrée est *toujours* considérée comme une chaîne de
caractères :

::

       i. Avantage : vous n'avez plus à saisir les guillemets si vous entrez une chaîne de caractères.
       
       ii. Inconvénient : même un entier est considéré comme une chaine de caractères. 
       

**Réponse à 3. b)** C'est un problème d'encodage de caractères : le plus
simple est de préfixer votre chaîne par la lettre ``u`` (pour encodage
unicode). Tapez ``input(u'Quel est ton âge ?')`` au lieu
``input(u'Quel est ton âge ?')``

**Question.** Améliorez votre programme pour que ``Python`` extraie
d'une réponse comme ``18 ans`` la sous-chaîne ``18`` et réponde
correctement enfin.

**Solution** :

.. code:: python

    prenom =raw_input('Bonjour Biwane, quel est ton prenom ?')
    age = raw_input(u'Quel est ton âge ?')
    
    agenum = age[:-4] # J'enlève les 4 derniers caractères
    agenum = int(agenum) # Je convertis la chaîne en nombre entier
    
    print(prenom  + ' tu es né(e) en ' + str(2015-agenum)+ ' !')


.. parsed-literal::

    Bonjour Biwane, quel est ton prenom ?Chuck
    Quel est ton âge ?56 ans
    Chuck tu es né(e) en 1959 !

