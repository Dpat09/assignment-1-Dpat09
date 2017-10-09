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

                x = x-1 if x == h else x
                y = y-1 if y == w else y

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
        w = image.shape[1]
        h = image.shape[0]

        newW = int(w*float(fx))
        newH = int(h*float(fy))

        ratioW = w / newW
        ratioH = h / newH

        import numpy as np
        import math as ma
        from . import interpolation as bilinear
        bi = bilinear.interpolation()
        newImg = np.zeros((newH, newW), np.uint8)
        for i in range(newImg.shape[0]):
            for j in range(newImg.shape[1]):

                x = ratioH * i
                y = ratioW * j

                x1 = ma.floor(x)
                x2 = ma.ceil(x)
                y1 = ma.floor(y)
                y2 = ma.ceil(y)

                x1 = x1-1 if x1 == h else x1
                x2 = x2-1 if x2 == h else x2
                y1 = y1-1 if y1 == w else y1
                y2 = y2-1 if y2 == w else y2

                pt1 = (x1, y1, image[x1, y1])
                pt2 = (x1, y2, image[x1, y2])
                pt3 = (x2, y1, image[x2, y1])
                pt4 = (x2, y2, image[x2, y2])
                unknown = (x, y, 0)

                if pt1[0] == pt3[0] and pt1[2] == pt2[2]:
                    newImg[i, j] = image[int(x), int(y)]
                else:
                    newImg[i, j] = bi.bilinear_interpolation(pt1, pt2, pt3, pt4, unknown)

        image = newImg
        return image

