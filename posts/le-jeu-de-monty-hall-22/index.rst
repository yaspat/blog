.. title: Le jeu de Monty Hall 2/2
.. slug: le-jeu-de-monty-hall-22
.. date: 2016-03-07 10:03:07 UTC+01:00
.. tags: probabilités
.. category: 
.. link: 
.. description: 
.. type: text


.. class:: alert alert-info pull-right
.. contents::                                                       


Maintenant que vous connaissez `le jeu de Monty Hall <link://slug/le-jeu-de-monty-hall-12>`_, on peut par
exemple simuler 100 000 parties du jeu dans lesquelles le candidat
choisit systématiquement la stratégie de changer son choix. Si Marylin a
raison (mais vous en êtes convaincus maintenant), la fréquence des
parties gagnées devrait être voisine de :math:`2/3`, et non pas de
:math:`1/2` comme l'ont hurlé ses détracteurs.


.. raw:: html

 <!--TEASER_END -->

Importation des fonctions utiles
--------------------------------

le module **random** contient des fonctions permettant de simuler des
tirages aléatoires. Ici, je n'importe qu'une seule de ses fonctions, la
fonction :math:`\texttt{randrange}` :

.. code:: python

    from random import randrange

Si **a** et **b** sont deux entiers, la commande **randrange(a,b)**
choisit au hasard un entier dans l'intervalle :math:`[a,b[`.

Simulation d'une partie du jeu de *Let's make a deal*
-----------------------------------------------------

Je vais créer une fonction :math:`\texttt{makeDeal}` qui ne prend aucun
argument en entrée mais retourne :math:`\texttt{1}` en sortie si le
joueur gagne la partie, et :math:`\texttt{0}` sinon.

Je suppose dans mon modèle :

1. Que la voiture est toujours derrière la porte 1 (cela ne nuit en rien
   à la généralité du problème, il suffit par exemple, une fois placée
   la voiture, de renommer les portes et d'appeler 1 celle qui cache le
   gros lot).

2. Que le joueur change toujours son choix après que le présentateur lui
   a dévoilé une chèvre.

Je veux donc vérifier que sur un grand nombre de parties, le joueur
gagne environ 2 fois sur 3.

Pour cela, il faut que je sache :

1. Choisir une porte au hasard (action du joueur). C'est simple avec
   **randrange(a,b)**, je réalise cela avec la fonction
   :math:`\texttt{choixJoueur}`.
2. Choisir une porte a, utre que celle choisie par le joueur et derrière
   laquelle se trouve une chèvre (action du présentateur). Je réalise
   cela avec la fonction :math:`\texttt{montreChevre}`

C'est tout !

Pour le point 1., c'est facile :

.. code:: python

    def choixJoueur():
        return randrange(1,4) # choisit un entier au hasard entre 1 et 3.

Pour le point 2., il suffit de savoir choisir un entier autre que 1 (car
la porte 1 recèle la voiture !), et que celui choisi par le joueur.

.. code:: python

    def montreChevre(porteJoueur):
        """Entrée : porteJoueur, le numéro de la porte choisie par le joueur
           Sortie : un entier entre 2,3 qui est le numéro de la porte ouverte
           par le présentateur connaissant porteJoueur
        """
        if porteJoueur == 1:         # le joueur avait bien trouvé la voiture
            return randrange(2,4)    # le présentateur choisit au hasard une porte entre la 2 et la 3
        else:
            return 5-porteJoueur # ce nombre vaut 2 si porteJoueur=3 et vice-versa !

Il ne me reste plus qu'à constuire la fonction
:math:`\texttt{makeDeal}`. Lisez le code, vous verrez, il est clair
qu'en changeant de choix on gagne deux fois sur trois !

.. code:: python

    def makeDeal():
        print('*** Simulation d\'une partie du jeu Let\'s make a deal!***')
        print('la voiture est derrière la porte 1.')
        a = choixJoueur() # Le joueur choisit une porte
        print('     Le candidat a choisi la porte {}.'.format(a))
        b = montreChevre(a) # Monty ouvre une porte
        print('     Monty Hall lui dévole la porte {}.'.format(b))
        print('     Le candidat change son choix...')
        if a<>1: # mettons a =2, dans ce cas Monty ouvre la porte 3 (il ne peut ouvrir la 1!)
                 # donc en changeant choix, le candidat gagne si et seulement si a <> 1 !
            print('*** le candidat a gagné !                          ***')
            return 1
        else:
            print('*** le candidat a perdu !                          ***')
            return 0

Maintenant, je peux suivre une partie de ce jeu comme à la télé, avec
l'ambiance en moins toutefois ...

.. code:: python

    makeDeal()


.. parsed-literal::

    *** Simulation d'une partie du jeu Let's make a deal!***
    la voiture est derrière la porte 1.
         Le candidat a choisi la porte 1.
         Monty Hall lui dévole la porte 3.
         Le candidat change son choix...
    *** le candidat a perdu !                          ***




.. parsed-literal::

    0



L'heure de vérité : fréquence des victoires sur un grand nombre de parties
--------------------------------------------------------------------------

Une petite boucle pour finir. Mais j'allègel la fonction
:math:`\texttt{makeDeal}` pour ne pas avoir tous les affichages dûs au
:math:`\texttt{print}` :

.. code:: python

    def makeDeal():
        a = choixJoueur() 
        b = montreChevre(a) # Monty ouvre une porte
        if a<>1: 
            return 1
        else:
            return 0

.. code:: python

    Nombre_parties = 100000
    Nombre_victoires = 0.
    for p in range(Nombre_parties):
        Nombre_victoires += makeDeal()
    print('Fréquence des victoires en changeant son choix = {}%'.format(100*Nombre_victoires/Nombre_parties) )



.. parsed-literal::

    Fréquence des victoires en changeant son choix = 66.502%


Marylin a raison : ce n'est pas du 50-50 !
