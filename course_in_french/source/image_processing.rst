Le traitement d'images avec Numpy et Scipy 
===========================================

Le module consacré au traitement d'image est `scipy.ndimage`

::

    >>> from scipy import ndimage


Les routines de traitement d'image disponibles peuvent être classées par
type de traitement.

* **Transformations géométriques des images** : orientation, résolution, ..

::

    >>> lena = scipy.lena()
    >>> shifted_lena = ndimage.shift(lena, (50, 50))
    >>> shifted_lena2 = ndimage.shift(lena, (50, 50), mode='nearest')
    >>> rotated_lena = ndimage.rotate(lena, 30)
    >>> cropped_lena = lena[50:-50, 50:-50]
    >>> zoomed_lena = ndimage.zoom(lena, 2)
    >>> zoomed_lena.shape
    (1024, 1024)

.. image:: lena_transforms.png
   :align: center 


.. sourcecode:: ipython

    In [35]: subplot(151)
    Out[35]: <matplotlib.axes.AxesSubplot object at 0x925f46c>

    In [36]: imshow(shifted_lena, cmap=cm.gray)
    Out[36]: <matplotlib.image.AxesImage object at 0x9593f6c>

    In [37]: axis('off')
    Out[37]: (-0.5, 511.5, 511.5, -0.5)

    In [39]: # etc.


* **Utilisation de filtres**

::

    >>> lena = scipy.lena()
    >>> noisy_lena = np.copy(lena)
    >>> noisy_lena += lena.std()*0.5*np.random.standard_normal(lena.shape)
    >>> gaussian_lena = ndimage.gaussian_filter(noisy_lena, sigma=3)
    >>> median_lena = ndimage.median_filter(blurred_lena, size=5)
    >>> import scipy.signal
    >>> wiener_lena = scipy.signal.wiener(blurred_lena, (5,5))

.. image:: filtered_lena.png
   :align: center 



Et bien d'autres filtres dans ``scipy.ndimage.filters`` et
``scipy.signal``.

**Exercice** : comparer les histogrammes des différentes images filtrées de
Lena.

* **Morphologie mathématique**

La morphologie mathématique est une théorie mathématique issue de la
théorie des ensembles, qui caractérise et transforme des structures
géométriques. Elle s'applique en particulier aux images binaires ; les
ensembles sont alors les groupes de pixels voisins non-nuls. On peut
également étendre la théorie aux images en niveaux de gris.

.. image:: morpho_mat.png
   :align: center 

Pour les opérations de base de la morphologie mathématique, on se sert
d'un "élément structurant" pour modifier d'autres éléments.

Génération d'un élément structurant ::

    >>> el = ndimage.generate_binary_structure(2, 1)
    >>> el
    array([[False,  True, False],
	   [ True,  True,  True],
	   [False,  True, False]], dtype=bool)
    >>> el.astype(np.int)
    array([[0, 1, 0],
	   [1, 1, 1],
           [0, 1, 0]])

Erosion ::

    >>> a = np.zeros((7,7), dtype=np.int)
    >>> a[1:6, 2:5] = 1
    >>> a
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])
    >>> ndimage.binary_erosion(a).astype(a.dtype)
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])
    >>> #Erosion removes objects smaller than the structure
    >>> ndimage.binary_erosion(a, structure=np.ones((5,5))).astype(a.dtype)
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])

Dilatation
::

    >>> a = np.zeros((5, 5))
    >>> a[2, 2] = 1
    >>> a
    array([[ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.]])
    >>> ndimage.binary_dilation(a).astype(a.dtype)
    array([[ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  1.,  1.,  1.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.]])

Ouverture

::
    >>> a = np.zeros((5,5), dtype=np.int)
    >>> a[1:4, 1:4] = 1; a[4, 4] = 1
    >>> a
    array([[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 0, 0, 1]])
    >>> # Opening removes small objects
    >>> ndimage.binary_opening(a, structure=np.ones((3,3))).astype(np.int)
    array([[0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0]])
    >>> # Opening can also smooth corners
    >>> ndimage.binary_opening(a).astype(np.int)
    array([[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 1, 1, 1, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]])

**Exercice** : vérifier que l'ouverture correspond bien à la succession d'une
érosion et d'une dilatation.

Une ouverture permet de supprimer les petits éléments, et une fermeture
de refermer les petits trous : on peut donc utiliser ces opérations pour
"nettoyer" une image.
::

    >>> a = np.zeros((50, 50))
    >>> a[10:-10, 10:-10] = 1
    >>> a += 0.25*np.random.standard_normal(a.shape)
    >>> mask = a>=0.5
    >>> opened_mask = ndimage.binary_opening(mask)
    >>> closed_mask = ndimage.binary_closing(opened_mask)

.. image:: morpho.png
   :align: center 

**Exercice** : vérifier que le carré reconstruit a une aire inférieure à
l'aire du carré initial. (Ce serait le contraire si on faisait la
fermeture avant l'ouverture).

En **niveaux de gris**, l'érosion (resp. la dilatation) correspond à
remplacer un pixel par le minimum (resp. le maximum) des pixels
recouverts par l'élément structurant. 
::

    >>> a = np.zeros((7,7), dtype=np.int)
    >>> a[1:6, 1:6] = 3
    >>> a[4,4] = 2; a[2,3] = 1
    >>> a
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 3, 3, 3, 3, 3, 0],
           [0, 3, 3, 1, 3, 3, 0],
           [0, 3, 3, 3, 3, 3, 0],
           [0, 3, 3, 3, 2, 3, 0],
           [0, 3, 3, 3, 3, 3, 0],
           [0, 0, 0, 0, 0, 0, 0]])
    >>> ndimage.grey_erosion(a, size=(3,3))
    array([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 3, 2, 2, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]])


* **Mesures sur l'image**

::

    >>> x, y = np.indices((100, 100))
    >>> sig = np.sin(2*np.pi*x/50.)*np.sin(2*np.pi*y/50.)*(1+x*y/50.**2)**2
    >>> mask = sig > 1
    >>> labels, nb = ndimage.label(mask)
    >>> nb
    8
    >>> areas = ndimage.sum(mask, labels, np.arange(1, labels.max()+1))
    >>> areas
    [190.0, 45.0, 424.0, 278.0, 459.0, 190.0, 549.0, 424.0]
    >>> maxima = ndimage.maximum(sig, labels, np.arange(1, labels.max()+1))
    >>> maxima
    [1.8023823799830032, 1.1352760475048373, 5.5195407887291426,
    2.4961181804217221, 6.7167361922608864, 1.8023823799830032,
    16.765472169131161, 5.5195407887291426]
    >>> ndimage.find_objects(labels==4)
    [(slice(30, 48, None), slice(30, 48, None))]
    >>> sl = ndimage.find_objects(labels==4)
    >>> imshow(sig[sl[0])


.. image:: measures.png
   :align: center 

Application à une image réelle : comptage des infondus dans un verre
---------------------------------------------------------------------

.. image:: MV_HFV_012.jpg
   :align: center 
   :width: 600px


1. Ouvrir l'image MV_HFV_012.jpg. On cherche à déterminer la fraction du
matériau occupée par des grains infondus (gris foncés), du verre (gris
clair), et des bulles (noir). On veut aussi estimer la taille typique des
grains de sable, leur nombre, les voisinages entre grains, etc.

2. Enlever le bandeau avec les informations de mesure.

3. Filtrer légèrement l'image avec un filtre médian afin d'affiner
l'histogramme des niveaux d'intensité. Vérifier sur les histogrammes.

4. A partir de l'image filtrée, déterminer des seuils permettant de
définir un masque pour les pixels du sable, un pour le verre et un pour
les bulles. Variante : écrire une fonction permettant de détecter
automatiquement les pics à partir de l'histogramme.

5. Afficher une image où les trois phases sont coloriées chacune dans une
couleur différente. 

6. Utiliser la morphologie mathématique pour nettoyer les différentes phases. 

7. Attribuer un label à chaque bulle et chaque grain de sable, et
supprimer les grains de sable de taille plus petite que 10 pixels. Pour
celà, utiliser ``ndimage.sum`` ou ``np.bincount`` afin d'obtenir la taille 
des grains.

8. Calculer la taille moyenne des bulles.

