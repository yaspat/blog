.. title: Informatique : Leçon 3
.. slug: schema-conditionnels 
.. date: 2015-09-29 13:39:19 UTC+02:00
.. tags: python, schémas conditionnels, leçon 
.. category: 
.. link: 
.. description: 
.. type: text

Python :  Leçon 3
==================

.. class:: alert alert-info pull-right

.. contents::


Objet de cette leçon :

1. Donner des exemples de schéma conditionnel
     
2. Sur un problème simple, on montre deux façons différentes d' implémenter l'algorithme : sous forme de simple script ou sous forme de fonction.

3.  Montrer un exemple de schéma conditionnel en cascade : celui de la résolution
de l'équation du second degré.


.. raw:: html     

	 <!-- TEASER_END -->
   



Schéma conditionnel composé
===========================

Le but de cette courte leçon est de 



Version script d'algorithme
---------------------------

Je crée un script qui demande à l'utilisateur de renter deux réels
:math:`x` et :math:`y` et retourne le plus grand des deux.

.. code:: python

    x = input('entrer un réel x --> ')
    y = input('entrer un réel y -- > ')
    if x > y:
        z = x
    else:
        z=y
    print('le plus grand des deux est '+str(z))


.. parsed-literal::

    entrer un réel x --> 12
    entrer un réel y -- > 15
    le plus grand des deux est 15


On constate que dans cette version, qui n'est pas celle d'une fonction,
il faut dialoguer avec la machine, et vous ne pouvez pas récupérer la
variable :math:`z` dans vos calculs.

Version fonction
----------------

.. code:: python

    def maxi(x,y):
        """ fonction qui calcule le plus grand des nombres x et y"""
        if x >y:
            z = x
        else:
            z = y
        return z

.. code:: python

    maxi(12,15)




.. parsed-literal::

    15



Différence notable avec la version script :

1. pas de ``input``, ni ``print`` : les variables d'entrée sont
   présupposées connues lorsque l'on définit la recette de la fonction.
2. pas de dialogue avec l'utilisateur : vous utilisez votre fonction
   comme n'importe quelle fonction usuelle.

Conclusion de cela
==================

Il vaut mieux concevoir ses algorithmes en fonctions et recourir en
dernière phase de réalisation d'un projet complexe.

