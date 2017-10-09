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
        exp1prev, exp2prev = 0, 0
        totalNumberOfPixels = sum(hist)

        # first iteration to start
        temp = 0
        for intensity, value in enumerate(hist[:threshold]):
            temp += (intensity * (value / totalNumberOfPixels))
        exp1 = temp

        temp = 0
        for intensity, value in enumerate(hist[threshold:]):
            temp += ((intensity + threshold) * (value / totalNumberOfPixels))
        exp2 = temp

        threshold = int((exp1 + exp2) / 2)

        while True:
            if (exp1 - exp1prev) == 0 and (exp2 - exp2prev) == 0:
                break
            exp1prev = exp1
            exp2prev = exp2

            temp = 0
            for intensity, value in enumerate(hist[:threshold]):
                temp += (intensity * (value / totalNumberOfPixels))
            exp1 = temp

            temp = 0
            for intensity, value in enumerate(hist[threshold:]):
                temp += ((intensity + threshold) * (value / totalNumberOfPixels))
            exp2 = temp

            threshold = int((exp1 + exp2)/2)

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
                bin_img[i, j] = 255 if image[i, j] >= threshold else 0

        return bin_img


