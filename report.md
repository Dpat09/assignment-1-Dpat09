# Digital Image Processing 
Assignment #1

1. Resampling:
    - nearest_neighbor:
        - It was a pretty straight forward method once I understood the concept better.
        - I utilized the pseudo code in the slides from lecture 4, it helped me get an understanding of what the overall look of what the actual code may look like.
        - Learned a few things about numpy that I did not know as to finding dimensions using the shape function.
        - Created a new array filled with zeros with the new dimensions found by multiplying the scales to their respective axis
        - Used nested for to iterate through the new array, used the ratio of width and height and multiplied them with their respective axis (i,j) to create variables x,y.
        - Created simple conditionals to prevent from going out of bounds if the scaling ratio isn't always square.
        - Used the previously mentioned rounded values to give use the position of where to look in the original image, and then set the new image to the intensity found at the rounded position in the old image.
        - Hence all that gave us the nearest neighbor.
     
    - bilinear
        - Setup just like nearest neighbor and utilized pseudo code from the lecture slides.
        - Used the math functions, floor and ceiling to help determine x1,x2,y1,y2 to use for the pts
        - Added safety nets to not go out of bounds for all previously mentioned coordinates.
        - Created tuples for all the 4 points required to do bilinear interpolation. Utilized the diagrams in the slides to understand which pt would contain which pair of coordinates.
        - Also added a safety net to prevent dividing values by 0. Implemented the conditional to check if the respective x or y was ever the exact same, in which case no interpolation is necessary.
        - Then calling the bilinear_interpolation was where it was a bit tricky, but used the diagram again to get a better perspective on how to solve it.
        - In the bilinear_interpolation, we also add a few checks to see if x1 and x2 were ever the exact same to prevent division by zero. 
          In the mathematical function the division by (x2-x1) could result in (something/0) would cause the whole program to crash.
          Also did the same for the possibility of y being the same. In which either passed in x1 & x2 or y1 & y2 to still do linear interpolation for intensity values.
          Then following the equation, called linear interpolation 2x to get the intensity values that would be utilized in finding the intensity values of P.
        - Lastly doing the function call results in it returning an intensity value, which we would store in the new image at i,j. Then I set image to the new image as the function was defined to return 'image'.
        - I found that modeling the code after the diagram and the mathematical equation made a lot of sense, and being a visual learner;
          I hand drew the diagram to understand how everything would fit in with the formula.
    
2. Region Counting:

    - a.) Binary image
        - compute_histogram:
            - Used numpy nditer that I found searching how to iterate through a numpy array. Found some help in scipy documents online. 
              Not having experience in numpy and python really hindered my performance on this homework.
            - Used the for loop to iterate through the image and incremented the intesity values in the histogram array.
            - Then returned the histogram array.
        
        - find_optimal_threshold:
            - This one was tough, but utilized the pseudo code for Expectation Maximization.
            - Modeling after the pseudo code understood to first set threshold to half the length of the histogram array.
            - Had to create some sort of temporary variables to hold the computed expected values of the halfs of the histogram.
            - created a variable to hold the total number of pixels which will be utilized in finding f(x) for finding the expected value
            - Since it is a do while loop of sorts, the first iteration was done outside the loop to start the process. (also side note learned how to use enumerate() for tuples to make the for loop easier)
            - Then computed the E[X] for all X less than K/2, K being the length of the histogram. Also did the same for being greater than or equal to.
            - Following the pseudo code, set threshold to the sumation of the two resulting expected values divided by two.
            - The loop continues to till there is difference between the temporarily held E[X]s and recently calculated E[X]s.
            - This one was tough in understanding how to get the probablilty for every position in histogram to be able to find the E[X]
        
        -   binarize:
            - This function was fairly straight forward once the threshold was found.
            - Simply use the functions just created to compute the histogram, then use the histogram to compute threshold.
            - Then iterate through the image the same method as the interpolation.
              All you do then is check if the intensity in the image in greater than or equal to the threshold, and if it is: you store 255 as the intensity at the corresponding (i,j) values.
              Else you store 0.
            - That was all for this function.
        
        -   Overall threshold was the toughest part.
        

            