.. title: Fonction du DM2
.. slug: fonction-du-dm-2
.. date: 2015-09-20 19:20:34 UTC+02:00
.. tags: python, fonction
.. category: 
.. link: 
.. description: 
.. type: text

Voici un exemple de script de fonction (c'est celle du DM2, à savoir, celle définie par :math:`f(x)= \ln\left(\frac{e^{x}}{x} -1\right)`).

.. raw:: html  

	 <!-- TEASER_END -->


Vous pouvez télécharger le script de la fonction `ici <https://github.com/yaspat/Biwane15-16/raw/master/DM/DM02/Scripts_Python/scriptExo2.py>`_.



.. code:: python

	 # -*- coding: utf-8 -*-
	 """
	 Created on Sat Sep 12 07:40:45 2015

	 @author: Yas
	 """
	 from __future__ import division
	 from math import log,exp

	 def f(x):
	     """fonction f de l'exercice 1 du DM2"""
             y = log(exp(x)/x -1)
             return y


Et pour voir le code en action : depuis l'éditeur : appuyez sur la touche F5 (après avoir sauvegardé votre script). Les Mac users, vous penserez à appuyer simultanément sur la touche fn en bas à gauche de votre clavier pour échapper ladite touche F5.  Vous verrez alors dans la console :

.. code:: python

   runfile(r"le chemin d'accès jusqu' à votre fichier", wdir=r"le chemin d'accès à votre répertoire de travail")
   

Ce qui signifie : votre fichier a été exécuté (sans avoir trouvé d'erreurs normalement !). Enfin, dans la console, tapez :

.. code:: python
	 
	  >>> f(0.5)
	  0.8317965657511863

C'est tout.
