Image processing with Numpy and Scipy 
===========================================

The submodule dedicated to image processing in scipy is `scipy.ndimage`.

::

    >>> from scipy import ndimage

Image processing routines may be sorted according to the category of
processing they perform.


* **Geometrical transformations on images** : orientation, resolution, ..

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


* **Using filters**

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



And many other filters in ``scipy.ndimage.filters`` and ``scipy.signal``.

**Exercise** : compare histograms for the different filtered images.

* **Mathematical morphology**

Mathematical morphology is a mathematical theory that stems from set
theory. It characterizes and transforms geometrical structures. Binary
(black and white) images, in particular, can be transformed using this
theory: the sets to be transformed are the sets of neighboring
non-zero-valued pixels. The theory was also extended to gray-valued images.

.. image:: morpho_mat.png
   :align: center 

Elementary mathematical-morphology operations use a *structuring element*
in order to modify other geometrical structures.

Let us first generate a structuring element ::

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

Dilation
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

Opening

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

Closing: ``ndimage.binary_closing``

**Exercise** : check that opening amounts to eroding, then dilating.

An opening operation removes small structures, while a closing operation
fills small holes. Such operation can therefore be used to "clean" an
image.

::

    >>> a = np.zeros((50, 50))
    >>> a[10:-10, 10:-10] = 1
    >>> a += 0.25*np.random.standard_normal(a.shape)
    >>> mask = a>=0.5
    >>> opened_mask = ndimage.binary_opening(mask)
    >>> closed_mask = ndimage.binary_closing(opened_mask)

.. image:: morpho.png
   :align: center 

**Exercise** : check that the area of the reconstructed square is smaller
than the area of the initial square. (The opposite would occur if the
closing step was performed *before* the opening).


For **gray-valued** images, eroding (resp. dilating) amounts to replacing
a pixel by the minimal (resp. maximal) value among pixels covered by the
structuring element centered on the pixel of interest.

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


* **Measures on the image**

Let us first generate a nice synthetic binary image.

::

    >>> x, y = np.indices((100, 100))
    >>> sig = np.sin(2*np.pi*x/50.)*np.sin(2*np.pi*y/50.)*(1+x*y/50.**2)**2
    >>> mask = sig > 1

Now we look for various information about the objects in the image::

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

Application: counting bubbles and unmolten grains
----------------------------------------------------

.. image:: MV_HFV_012.jpg
   :align: center 
   :width: 600px


1. Open the image file MV_HFV_012.jpg and display it. Browse through the
keyword arguments in the docstring of ``imshow`` to display the image
with the "right" orientation (origin in the bottom left corner, and not
the upper left corner as for standard arrays).

This Scanning Element Microscopy image shows a glass sample (light gray
matrix) with some bubbles (on black) and unmolten sand grains (dark
gray). We wish to determine the fraction of the sample covered by these
three phases, and to estimate the typical size of sand grains and
bubbles, their sizes, etc.

2. Crop the image to remove the lower panel with measure information.

3. Slightly filter the image with a median filter in order to refine its
histograme. Check how the histogram changes.

4. Using the histogram of the filtered image, determine thresholds that
allow to define masks for sand pixels, glass pixels and bubble pixels.
Other option (homework): write a function that determines automatically
the thresholds from the minima of the histogram.

5. Display an image in which the three phases are colored with three
different colors.

6. Use mathematical morphology to clean the different phases.

7. Attribute labels to all bubbles and sand grains, and remove from the
sand mask grains that are smaller than 10 pixels. To do so, use
``ndimage.sum`` or ``np.bincount`` to compute the grain sizes.

8. Compute the mean size of bubbles.

Answers can be found in 
:ref:`image-answers` 
