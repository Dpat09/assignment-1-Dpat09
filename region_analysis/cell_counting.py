class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        import numpy as np
        regions = dict()
        R = np.zeros((image.shape[0], image.shape[1]), np.uint32)
        k = 1

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if (image[i,j] == 1 and image[i,j-1] == 0 and image[i-1,j] == 0):
                    R[(i, j)] = k
                    regions[k] = {(i, j)}
                    k += 1

                elif (image[i,j] == 1 and image[i,j-1] == 0 and image[i-1,j] == 1):
                    R[(i, j)] = R[(i-1, j)]
                    regions[R[i, j]].add((i, j))

                elif (image[i,j] == 1 and image[i,j-1] == 1 and image[i-1,j] == 0):
                    R[(i, j)] = R[(i, j-1)]
                    regions[R[i, j]].add((i, j))
                elif (image[i,j] == 1 and image[i,j-1] == 1 and image[i-1,j] == 1):
                    R[(i, j)] = R[(i-1,j)]

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        


        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""



        return image

