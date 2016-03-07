.. title: Le jeu de Monthy Hall 1/2
.. slug: le-jeu-de-monthy-hall-12
.. date: 2016-03-06 21:38:01 UTC+01:00
.. tags: probabilités
.. category: 
.. link: 
.. description: 
.. type: text




   

   *"Mon unique conseil : si vous parvenez à obtenir de moi que je vous
   offre 5000 dollars pour ne pas ouvrir la porte : prenez l'argent et
   rentrez chez vous !"*                                      (Monthy Hall)

 
                                                      





.. figure:: ../../images/Monthy/Erdos.jpeg   
   :scale: 50 %	    
   :align: right                          

   Paul Erdös


\.\.\. ou comment l'intuition peut être difficile à exercer en probabilités.
Les probabilités sont en effet  un domaine particulier des mathématiques : bien
que la théorie soit  une théorie mathématique à part entière, l'honnête
homme a en vue son application à des problèmes de la vraie vie. Il faut
donc pour cela interpréter des résultats théoriques à des situations concrètes.   Souvent, on comprend *a posteriori* la valeur d'une
probabilité calculée, alors qu'il n'était pas évident de la deviner par
l'intuition. Intuition dont on n'a pas l'air tous dôtés de la même
manière, et  qui plus est, pas liée de façon simple aux aptitudes
mathématiques.









Voici une histoire célèbre pour illustrer ceci.


.. raw:: html

 <!--TEASER_END-->
 



Je  vous retranscris ici  un passage du livre de P. Hoffman,
*Erdös, l'homme qui n'aimait que les nombres* [#]_. Les titres des paragraphes ne
sont pas tirés du livre, mais je les introduis pour que suiviez
l'anecdote.

.. class:: alert alert-info pull-right
.. contents::                                                       




.. image:: ../../images/Monthy/Vos-savant.jpeg
   :align: right
  

----------------------------------------------------------------------------------



Marilyn vos Savant répond à vos questions
-----------------------------------------




    *Bien que les nombres fussent les amis intimes d'Erdös, il lui
    arrivait de se méprendre sur leur compte. Aussi doué fût-il, son
    intuition n'était pas toujours infaillible. En effet, la dernière
    fois qu'il rendit visite à Vázsonyi, dans sa résidence de retraite
    dans les vignobles de Californie, il trébucha contre un délicat
    casse-tête posé dans* Demandez à Marilyn, *une rubrique de
    Marilyn vos Savant dans le magazine*  Parade. *Clinquante et
    pleine d'assurance, Marilyn vos Savant fait partie de ces gens que
    les mathématiciens de métier aiment haïr. Elle s'affiche comme la personne ayant "le Q.I. le plus élevé" jamais enregistré : un énorme
    228, d'après*  le livre Guinness des records. *Elle arbore un
    anneau de mariage en carbone pyrolytique, matériau spécial utilisé
    dans le coeur artificiel de Jarvik, inventé par son mari Robert
    Jarvik. Sa réputation dans le milieu mathématique n'est sortie
    grandie avec son livre*  The world most famous math problem [2]_, 
    *où elle met en doute la démonstration par Wiles au théorème de Fermat, ainsi que la
    théorie de la relativité d'Einstein.* Demandez à Marilyn *a été
    décrit comme une sorte de*  Hints form Heloise [3]_  *pour l'esprit, avec
    beaucoup de mathématiques par-dessus le marché. Une part de
    l'antipathie qu'elle inspire tient à une certaine jalousie : sa
    rubrique dans* Parade, *tous les dimanches, est lue par des millions
    de personnes, et les livres et discours qui la complètent lui
    assurent une vie confortable. Beaucoup de mathématiciens
    professionnels, en revanche, n'ont pas touché un seul centime de la
    publication de leurs livres.*

.. figure:: ../../images/Monthy/Monthy.jpeg
   :align: left
   
   Monthy Hall 	   

.. [2]  Le problème de maths le plus célèbre au monde  (1993)

.. [3] Les tuyaux d'Héloïse, rubrique bien connue de petits conseils
    domestiques qui paraît dans certains journaux américains. Elle est
    rédigée actuellement par une dénommée Héloïse, mais c'est sa mère
    qui en est à l'origine, en 1959. (N.d.T.)



Le jeu de Monthy Hall, et le conseil de Marilyn
-----------------------------------------------



   


    *Dans son article du 9 septembre 1990, Marilyn vos Savant répondit à
    l'un de ses lecteurs qui lui avait soumis une énigme bien connue.
    Vous participez à un jeu où l'on vous propose trois portes au choix.
    L'une des portes cache une voiture à gagner et chacune des deux
    autres une chèvre. Vous choisissez, disons, la porte 1 ;
    l'animateur, qui sait où est la voiture, ouvre une autre porte,
    derrière laquelle se trouve une chèvre. Il vous donne maintenant la
    possibilité de vous en tenir à votre choix initial (porte 1) ou de
    choisir l'autre porte. Qu'avez-vous intérêt à faire ?
    On appelle
    cela le dilemme de Monthy Hall, problème auquel étaient confrontés
    les invités du jeu télévisé*  Let's make a deal *de Monthy
    Hall* [4]_  *sauf que les lots de consolation n'étaient pas des chèvres. Marilyn
    vos Savant recommanda à son correspondant de modifier son choix.
    S'en tenir au choix initial donnait une chance sur trois de gagner
    affirmait-elle, alors que choisir l'autre porte doublait les chances
    : deux sur trois. Pour convaincre ses lecteurs, elle leur demandait
    d'imaginer qu'il n'y ait non pas une, mais un million de portes.* "
    Vous choisissez la porte numéro 1" *expliquait-elle.*
    L'animateur, qui sait ce qui se trouve derrière chaque porte et
    évitera toujours celle qui cache le gros lot, ouvre toutes les
    portes sauf la numéro 777 777 [et la numéro 1 bien sûr]. Vous
    modifierez votre choix assez vite n'est-ce pas ?"



.. [4] Animateur et producteur de télévision américaine (N.d.T.)

Des mathématiciens bien sûrs d'eux
----------------------------------

    *Non, manifestement. Sitôt paru son article, vos Savant fut
    assaillie de lettres de lecteurs en désaccord. Ils maintenaient que
    les chances étaient de cinquante-cinquante, et non de deux sur
    trois, dans le cas où l'on modifiait son choix. Dans son article du
    2 décembre 1990, Marilyn vos Savant publia quelques-unes des lettres:* 

        *Étant mathématicien professionnel, je suis très inquiet du
        manque de compétences mathématiques du grand public. Je vous
        prie d'essayer d'y remédier en reconnaissant votre erreur ...*



                                        Robert Sachs, Ph. D., université George Mason

        *Vous avez faux, archi-faux ! Je m'explique : une fois aue
        l'animateur a dévoilé une chèvre, vous avez dès lors une chance
        sur deux d'avoir juste. Que vous modifiiez votre ou non votre
        réponse, les chances sont les mêmes. Il y a suffisamment
        d'analphabétisme mathéatique dans ce pays ; inutile que le Q.I.
        le plus élevé en sème davantage. C'est honteux !*



                                           Scott Smith, Ph. D., université  de Floride 

La réponse de Marilyn
---------------------

    *Pour bien faire comprendre son analyse, Marilyn vos Savant dressa
    cette fois dans un tableau la liste exhaustive des six possibilités
    :*



Résultats  du jeu en en choisissant la porte 1 et en s'y tenant suivant les différentes configurations :


+---------------+---------------+-------------+----------------+
| **Porte 1**   | **Porte 2**   | **Porte**   | **Résultat**   |
+===============+===============+=============+================+
| Voiture       | Chèvre        | Chèvre      | **Gagnant**    |
+---------------+---------------+-------------+----------------+
| Chèvre        | Voiture       | Chèvre      |   Perdant      |
+---------------+---------------+-------------+----------------+
| Chèvre        | Chèvre        | Voiture     |   Perdant      |
+---------------+---------------+-------------+----------------+



Résultats  du jeu en choisissant la porte 1 et en modifiant son choix :

+---------------+---------------+-------------+----------------+
| **Porte 1**   | **Porte 2**   | **Porte**   | **Résultat**   |
+===============+===============+=============+================+
| Voiture       | Chèvre        | Chèvre      | Perdant        |
+---------------+---------------+-------------+----------------+
| Chèvre        | Voiture       | Chèvre      | **Gagnant**    |
+---------------+---------------+-------------+----------------+
| Chèvre        | Chèvre        | Voiture     | **Gagnant**    |
+---------------+---------------+-------------+----------------+

    *Le tableau démontre, écrivait-elle, que "lorsque vous modifiez
    votre choix vous gagnez deux fois sur trois, alors que si vous vous
    en tenez à votre choix initial, vous ne gagnez qu'une fois sur
    trois ".*

Un troisième article sur la question
------------------------------------

    *Mais le tableau ne fit pas taire ses détracteurs. Dans un troisième
    article sur la question (le 17 février 1991), elle signala que dans
    les milliers de lettres reçues, neuf sur dix étaient contre elle, et
    qu'elle avait eu des reproches d'un statisticien aux National
    Institute of Health* [5]_, *ainsi que du directeur adjoint du Centre
    des renseignements militaires. Les lettres avaient tourné au
    vinaigre, certaines la traitant de chèvre ou affirmant que les
    femmes ne voient pas les problèmes de mathématiques comme les
    hommes. "Vous vous trompez complètement à propoos de la question du
    jeu télévisé", écrivit E. Ray Bobo, un Ph. D. de Gerogetown, "et
    j'espère que cette controverse attirera un peu l'attention du
    public sur la grave crise nationale qui frappe l'enseignement
    supérieur des mathématiques. Si vous pouviez reconnaître votre
    erreur, vous contribueriez de façon constructive à la résolution
    d'une situation déplorable. Combien de mathématiciens furieux vous
    faut-il pour changer d'avis ?*"

.. [5] Instituts nationaux de la santé, l'organisme
    gouvernemental américain qui finance et mène les recherches
    biomédicales (N.d.T.)

Point final de  Marilyn 
-----------------------

    "*Lorsque la réalité heurte si violemment l'intuition*, répondit
    Marilyn vos Savant dans sa rubrique, *les gens sont ébranlés*". *Elle
    essaya autrement. Imaginez, dit-elle, que juste après que
    l'animateur a ouvert la porte dévoilant une chèvre, atterrisse sur
    la scène du jeu une soucoupe volante, et qu'en sorte une petite
    femme verte. Cettre dernière ne sachant pas quelle porte vous avez
    choisie au départ, on lui demande de choisir l'une des deux portes
    restées closes. La probabilité qu'elle tombe sur la voiture est de
    cinquante pour cent,* "Mais c'est qu'il lui manque l'avantage
    qu'avait le candidat d'origine - l'aide de l'animateur [...]. Si le
    gros lot se trouve derrière la numéro 2, l'animateur vous montre la
    numéro 3 ; et si le gros lot se trouve derrière la numéro 3, il vous
    montre la numéro 2. *Donc, quand vous modifiez votre choix, vous
    gagnez si le prix se trouve au numéro 2 ou au numéro 3*.  **Vous ganez
    dans les deux cas !**  *Mais si vous laissez votre choix inchangé,
    vous ne gagnez que si le prix se trouve derrière la porte numéro
    1.*"  *Marilyn vos Savant avait parfaitement raison, comme durent
    finalement l'admettre les mathématiciens, penauds (...).*


Une petite expérience pythonique au `prochain article <link://slug/le-jeu-de-monthy-hall-22>`_ pourrait nous aider à nous faire notre opinion !


.. [#] Paul Erdös est l'un des plus grands mathématiciens de tous les temps, il est décédé en 1996, et ici il s'agit du début du chapitre 6 du livre.


