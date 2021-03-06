.. _aide:

Savoir chercher (trouver) de l'aide
====================================


Il n'est pas très utile de connaître toutes les fonctions de numpy et
scipy, mais plutôt de savoir rapidement chercher les informations
qu'on cherche. Voici quelques moyens de trouver ces informations (qui
peuvent être plus rapides que de demander à Google...) :

* Sous Ipython, ``help fonction`` ouvre la page d'aide de la
  fonction. On peut taper le début de la fonction et se servir de la
  tab complétion pour faire apparaître les fonctions qui existent.

.. sourcecode:: ipython

    In [204]: help np.v
    np.vander     np.vdot       np.version    np.void0      np.vstack
    np.var        np.vectorize  np.void       np.vsplit     
    
    In [204]: help np.vander
	

Il n'est pas possible d'ouvrir une fenêtre séparée pour la
documentation, mais on peut très bien ouvrir un deuxième shell ``Ipython``  
qui sert exclusivement à afficher l'aide...

* On peut parcourir la documentation de numpy et scipy sur
  http://docs.scipy.org/doc/, et utiliser en particulier le bouton
  ``search`` à l'intérieur des pages de référence des deux librairies
  (http://docs.scipy.org/doc/numpy/reference/ et
  http://docs.scipy.org/doc/scipy/reference/). 

   Pour chaque package, la documentation est séparée en une partie
   "**Tutorials**", qui explique de manière synthétique l'utilisation des
   différents sous-packages, avec un certain nombre de cas d'utilisation, et
   une partie "**API**" qui reproduit exactement la documentation de chacune
   des fonctions.

.. image:: Scipy_doc.png
   :align: center
   :width: 900px 

* La documentation est régulièrement améliorée et mise à jour par les
  utilisateurs sur un wiki http://docs.scipy.org/numpy/, où on peut donc
  parfois trouver une **documentation plus fournie** pour certaines
  fonctions, notamment ``scipy.ndimage`` à l'heure actuelle (mai 2010).
  Chacun peut créer un compte et améliorer la documentation existante,
  c'est donc un moyen facile de contribuer au développement de ``numpy`` et
  ``scipy`` !

.. image:: docwiki.png
   :align: center
   :width: 900px 


* Pour savoir comment attaquer un problème, le Cookbook de
  scipy/numpy donne beaucoup d'exemples de cas d'utilisation courants
  http://www.scipy.org/Cookbook

* Le site web de Matplotlib http://matplotlib.sourceforge.net/ possède
  une gallerie d'images très utile quand on cherche à réaliser un graphe
  particulier, puisque le code source est joint à l'image.

.. image:: matplotlib.png
   :align: center
   :width: 900px 

* Le site web de Mayavi 
  http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/
  possède lui aussi une gallerie d'examples
  http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/auto/examples.html permettant de trouver plus
  vite comment faire différents types de visualisation.

.. image:: mayavi_website.png
   :align: center
   :width: 900px 

Enfin, deux autres possibilités un peu plus "techniques" mais qui peuvent
rendre service.

* Sous Ipython, si on ne connaît pas le nom exact de la fonction, ou 
  si on ne connaît pas les fonction qui existent on peut aussi utiliser
  la fonction magique ``%psearch`` dans Ipython : 

.. sourcecode:: ipython

    In [3]: import numpy as np
    In [4]: %psearch np.diag*
    np.diag
    np.diagflat
    np.diagonal

* On peut chercher des mots clés à l'intérieur des docstrings des
  différents modules grâce à numpy.lookfor

.. sourcecode:: ipython

    In [45]: numpy.lookfor('convolution')
    Search results for 'convolution'
    --------------------------------
    numpy.convolve
        Returns the discrete, linear convolution of two one-dimensional
    sequences.
    numpy.bartlett
        Return the Bartlett window.
    numpy.correlate
        Discrete, linear correlation of two 1-dimensional sequences.
    In [46]: numpy.lookfor('remove', module='os')
    Search results for 'remove'
    ---------------------------
    os.remove
        remove(path)
    os.removedirs
        removedirs(path)
    os.rmdir
        rmdir(path)
    os.unlink
        unlink(path)
    os.walk
        Directory tree generator.



* Si vous n'avez toujours pas trouvé après avoir fouillé l'aide, fait
  de nombreuses requêtes google, ... ne vous désepérez pas ! Il
  existe des mailing-lists (en anglais) très réactives où on obtient
  rapidement des réponses données par un certain nombre d'experts de
  Python scientifique :
  
    * **Numpy discussion** (numpy-discussion@scipy.org) : tout ce qui
	  concerne les tableaux numpy, leur manipulation, l'indexation,
	  etc.

    * **SciPy Users List** (scipy-user@scipy.org) : autour de scipy
      et des divers algorithmes, trucs et astuces pour traiter des
      données scientifiques.  

    * Il y a également une mailing-list pour les questions de plot
      avec matplotlib, matplotlib-users@lists.sourceforge.net                                
                                             
