import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        import numpy as np
        hist = [0]*256

        for intensity in np.nditer(image):
            hist[intensity] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = int(len(hist)/2)
        delta1prev, delta2prev = 0, 0
        totalNumberOfPixels = sum(hist)

        # first iteration to start
        temp = 0
        for intensity, value in enumerate(hist[:threshold]):
            temp += (intensity * (value / totalNumberOfPixels))
        delta1 = temp

        temp = 0
        for intensity, value in enumerate(hist[threshold:]):
            temp += ((intensity + threshold) * (value / totalNumberOfPixels))
        delta2 = temp

        threshold = int((delta1 + delta2) / 2)

        while True:
            if (delta1 - delta1prev) == 0 and (delta2 - delta2prev) == 0:
                break
            delta1prev = delta1
            delta2prev = delta2

            temp = 0
            for intensity, value in enumerate(hist[:threshold]):
                temp += (intensity * (value / totalNumberOfPixels))
            delta1 = temp

            temp = 0
            for intensity, value in enumerate(hist[threshold:]):
                temp += ((intensity + threshold) * (value / totalNumberOfPixels))
            delta2 = temp

            threshold = int((delta1 + delta2)/2)

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        histogram = self.compute_histogram(image)
        threshold = self.find_optimal_threshold(histogram)
        for i in range(bin_img.shape[0]):
            for j in range(bin_img.shape[1]):
                if image[i, j] >= threshold:
                    bin_img[i, j] = 255
                else:
                    bin_img[i, j] = 0

        return bin_img


