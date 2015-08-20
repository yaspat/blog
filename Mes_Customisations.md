# Mes modifications du thème `zen-ipython` (20 août 2015)

Ce thème est basé sur le thème `zen-jinja`

> j'ai modifié les dossiers `zen-jinja` et `zen-ipython` mais conservé les dossiers originaux  en copie


## Les modififcations :

1. Placé à la source le fichier `toggle.tpl` pour pouvoir caché le code python sur les billets rédigé depuis le `ipython notebook`.
2. Placé dans le dossier `themes\zen-ipython\assets\js\` le fichier `toggle.js` (contient la fonction qui permet de cacher la sortie) et aussi .
3. Placé dans `\themes\zen-jinja\assets\images\` le fichier `fond_bleu_nikola.jpeg`. Voir ligne 242  du fichier `zen-jinja\assets\css\main.css` (finalement je ne charge pas l'image, mais j'ai remplacé la couleur par du bleu `#3366aa`)
4. Retiré le fond en ligne 233 du même fichier.
5. Enlevé le fichier `themes\zen-jinja\assets\css\bitter.css` (parce que je n'aime pas trop cette fonte, et en ligne 2151/2161, placé des fontes sans-serif standard. 
6. Ligne 19 du fichier `theme\zen-ipython\assets\css\nikola_ipython.css\`  : enlevé l'image et mis le fond gris pour les marges de la cellule de sortie du Ipynb.
