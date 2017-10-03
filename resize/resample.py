class resample:

    def resize(self, image, fx, fy, interpolation):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """
        #Write your code for nearest neighbor interpolation here
        w = image.shape[1]
        h = image.shape[0]

        newW = int(w*float(fx))
        newH = int(h*float(fy))

        ratioW = w/newW
        ratioH = h/newH

        import numpy as np

        newImg = np.zeros((newH, newW), np.uint8)
        for i in range(newImg.shape[0]):
            for j in range(newImg.shape[1]):

                x = round(ratioH*i)
                y = round(ratioW*j)

                if x == h:
                    x-=1
                if y == w:
                    y-=1

                temp = image[x, y]
                newImg[i,j] = temp

        image = newImg
        return image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        newW = int(image.shape[1]*float(fx))
        newH = int(image.shape[0]*float(fy))

        import numpy as np
        newImg = np.zeros((newH, newW), np.unit8)
        #for i in range(newImg.shape[0]):
        #    for j in range(newImg.shape[1]):



        return image

