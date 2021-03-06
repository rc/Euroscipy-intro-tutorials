lena = scipy.lena()
noisy_lena = np.copy(lena)
noisy_lena += lena.std()*0.5*np.random.standard_normal(lena.shape)
gaussian_lena = ndimage.gaussian_filter(noisy_lena, sigma=3)
median_lena = ndimage.median_filter(blurred_lena, size=5)
import scipy.signal
wiener_lena = scipy.signal.wiener(blurred_lena, (5,5))
