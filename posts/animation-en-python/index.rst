.. title: Créer une animation en Python
.. slug: animation-en-python
.. date: 2016-01-30 16:37:50 UTC+01:00
.. tags: python, animation, video, biomorphes
.. link: 
.. category: images
.. description: 
.. type: text



..  class:: alert alert-info pull-right

.. contents::


Tu sais que tu peux créer des animations en **Python**, Biwane ? Le module **matplotlib** contient ce qu'il faut. Par exemple,  voici un petit film pour générer la génèse du
(coeur du) radiolaire d'ordre 3 à 12 branches, et sa "dégénerescence" vers
un coeur de radiolaire d'ordre 4. Tu ne sais pas ce qu'est un radiolaire
? Aucune importance, voilà le résultat :

+-------------+--------------------------+
|             | .. youtube:: 2qpXhdseGOw |
+-------------+--------------------------+ 


.. raw:: html

   <!--TEASER_END-->

Le radiolaire est le biomorphe de Pickover généré par la fonction :math:`p_3` donnée par :

.. math::  z\mapsto p_3(z) = z^3 +\dfrac{1}{2}.

On l'appelle ainsi car la figure générée évoque  un radiolaire. Voici une image d'un radiolaire dans la vraie vie :


.. thumbnail:: ../../images/Biomorphes3/radiolaire.jpeg
    :align: center


Le radiolaire généré par la fonction :math:`p_3` :

.. thumbnail:: ../../images/Biomorphes/radiolaire.png
    :align: center



et enfin,  un zoom sur  son coeur :

.. thumbnail:: ../../images/Biomorphes/output_30_0.png
    :align: center


`Ce billet <link://slug/biomorphes>`_ permet de  savoir comment générer ces images.
Ensuite, le principe de l'animation est de créer  une suite d'images et de les
faire défiler : c'est littéralement un *feuilleton* qu'on produit.

Je crée mon feuilleton en faisant défiler les images correspondant aux
fonctions :

.. math:: z\mapsto  p_t(z) = z^t + \dfrac{1}{2} \quad t \in[1,4] 

Ainsi, je fais varier l'exposant de :math:`z`  [#]_ . Maintenant, passons donc à la pratique :




Importation des modules utiles
==============================

.. code:: python

    import numpy as np
    import matplotlib.pyplot as plt
    
    # celui-là pour générer les feuilletons
    import matplotlib.animation as animation

Pythonisation de la fonction :math:`p_t`
========================================

.. code:: python

    # Construction de la fonction
    
    def p(t,z):
        return z**(t)+0.5

Fonctions utiles
================

Voici deux fonctions. La première, :math:`\texttt{dureeDeVie}`, est celle qui permet de déterminer de quelle couleur
colorier un point :math:`u` du plan complexe en déterminant son
caractère vis-à-vis de la fonction :math:`p_t`.

La seconde, :math:`\texttt{coloriage}`, réalise  le coloriage des points et génère donc
une image (qu'on va appeler une page, c'est-à-dire un feuillet du feuilleton). Il ne
restera plus qu'à assembler les feuillets du feuilleton pour fabriquer l'animation.

.. code:: python

    def dureeDeVie(t,u):
        """ u : un complexe
            r : un entier
            retourne le plus petit rang n inférieur ou égal à 10 pour
            lequel la partie réelle et la partie imaginaire excèdent 10 
            strictement en valeur absolue pour la suite récurrente de premier
            terme u et associée à la fonction p(t,z)  
            Si cet entier n'existe pas, on le pose égal à 0.
        """
        z = u # on peut faire les deux d'un coup : z,k = u,0 
        k = 0
        while k<= 10 and (abs(z.imag)<=10 or abs(z.real)<=10):
            z= p(t,z)
            k+=1
        if k==11:
            return 0
        else:
            return k       

.. code:: python

    def coloriage(r, xmin, xmax, ymin, ymax, nx,ny):
        """ je n'explique pas pour le moment ... """
        
        X = np.linspace(xmin,xmax,nx)  # je crée les subdivisons le long des X
        Y = np.linspace(ymax,ymin,ny)  # idem le long des Y
        A = np.zeros((ny,nx))          # J'initialise un tableau de taille ny x nx
        for i in range(0,ny):
            for j in range(0,nx):
                A[i,j]= dureeDeVie(r,X[i]+1j*Y[j]) # je place en position [i,j] du tableau la durée de vie du germe
        
        A=12-A                                   # Comme je veux colorier dans des teintes de bleu, je fais des 
        A[0,0]=0                                 # petites transformations sur les coefficients de A 
        A[1,1]=30
        
        return A

Construction du feuilleton
==========================

.. code:: python

    xmin,xmax,ymin,ymax = [-2,2,-2,2] # domaine où se situe le coeur du radiolaire
    
    nx = 500 # résolution : grille de 500 X 500 points
    ny = 500
    
    
    fig = plt.figure(figsize=(20,20)) # J'initialise le graphique
    
    ims = [] # ma liste d'images est vide au départ
    # ims est une liste de listes, ces listes étant des listes d'artists à dessiner dans
    # frame courant. Ici, la liste a un seul élément  par frame : l'image. 
    # artists : types d'objet python animable
    # frame : la page du feuilleton
    
    N = 300
    for k in range(0,N):
        r = 1+0.01*k
        A = coloriage(r, xmin, xmax, ymin, ymax, nx,ny)
        im = plt.imshow(A, animated=True)
        
        ims.append([im]) # J'ajoute mon image à ma liste
        print("génération de l'image {}/{}".format(k,N))
        
    print "Construction du feuilleton... (patience)"
    ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True,  repeat_delay=1500)
    
    
    ani.save('radiolaire.mp4')
    print('fin')
    
    




.. [#] Tu te demandes peut-être (et à juste titre) ce que peut bien siginifier par exemple :math:`z^{\sqrt{2}}` quand :math:`z` n'est pas un nombre réel ? Tu as bien raison ! Sinon tu as encore des problèmes de typo-déficience. Néanmoins, pour l'objet de ce billet, c'est sans importance ! 
