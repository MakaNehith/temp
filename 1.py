
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd




def simulate_bertrands_paradox( threshold_length , number_of_iterations):
    count_blue_endpoints = 0  # count the number of chords with length greater than threshold length in the random endpoints method
    count_red_endpoints = 0

    count_blue_midpoint = 0  # count the number of chords with length greater than threshold length in the random midpoint method
    count_red_midpoint = 0

    for index_of_iteration in range(number_of_iterations):

        # Generating the plot containing two 3d subplots, each with a sphere of radius 1 unit 
        figure , plots = plt.subplots(1 , 2 , dpi = 120, figsize = (12,6) , subplot_kw= { 'projection' : '3d'} )
        plots[0].view_init( elev = 30 , azim = 45) # for viewing the 3D plot in a particular way
        plots[1].view_init( elev = 30 , azim = 45) 

        # crearting a sphere using the polar form which is radius , theta  and phi.
        # x = rsin(theta)cos(phi)   0 <= theta <= pi
        # y = rsin(theta)sin(phi)   0 <= phi   <= 2*pi
        # z = rcos(theta)
        radius = 1
        theta = np.linspace( 0 , np.pi , 25 ) # creating an array of 25 values between 0 and pi which are equally placed
        phi = np.linspace( 0 , 2 * np.pi , 25) # creating an array of 25 values between 0 and 2*pi which are equally placed

        # creating a meshgrid, that is, (x[i] , y [i] , z [i] ) is a point on the surface of sphere of unit radius
        x = radius * np.outer(np.sin(theta) , np.cos(phi))  # np.outer() gives an array with product such each element being the product of one element in first array and one elment in the second array
        y = radius * np.outer(np.sin(theta) , np.sin(phi))
        z = radius * np.outer(  np.cos(theta) , np.ones(len(phi)))

        plots[0].plot_wireframe(x,y,z, edgecolor = 'black' , linewidth = 0.6) # creating the sphere in the first 3D plot
        plots[1].plot_wireframe(x,y,z, edgecolor = 'black' , linewidth = 0.6) # creating the sphere in the second 3D plot
        
        # Limiting the values of x, y and z from -1 to 1
        plots[0].set_xlim(-1,1)
        plots[0].set_ylim(-1,1)
        plots[0].set_zlim(-1,1)
        plots[1].set_xlim(-1,1)
        plots[1].set_ylim(-1,1)
        plots[1].set_zlim(-1,1)

        # Giving the labels on x, y and z axes
        plots[0].set_xlabel('x' , fontweight = 'bold' )
        plots[0].set_ylabel('y' , fontweight = 'bold')
        plots[0].set_zlabel('z' ,  fontweight = 'bold')
        plots[1].set_xlabel('x' , fontweight = 'bold')
        plots[1].set_ylabel('y' , fontweight = 'bold')
        plots[1].set_zlabel('z' , fontweight = 'bold')


        list_color = ['r-' , 'b-'] # for giving colors to lines in two plots basing on their chord lengths

        # Generate two random endpoints



        r1 = 1
        
        # first point
        Theta1 = rd.uniform(0 , (np.pi) , 1)  # uniformly generates a number from 0 to pi
        Phi1 = rd.uniform(0, 2*(np.pi) , 1)   # uniformly generates a number from 0 to 2* pi
        x1 = r1 * np.sin(Theta1) * np.cos(Phi1)
        y1 = r1 * np.sin(Theta1) * np.sin(Phi1)
        z1 = r1 * np.cos(Theta1)

        # Second point
        Theta2 = rd.uniform(0 , (np.pi) , 1)
        Phi2 = rd.uniform(0, 2*(np.pi) , 1)
        x2 = r1 * np.sin(Theta2) * np.cos(Phi2)
        y2 = r1 * np.sin(Theta2) * np.sin(Phi2)
        z2 = r1 * np.cos(Theta2)

        # calculating the length of the chord using distance formula
        length_of_chord_endpoints = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1-z2)**2 )
        if_length_of_chord_endpoints_is_greater = 0 # counter variable for checking whether the length of the chord is greater than the threshld length or not
        if length_of_chord_endpoints > threshold_length :
            if_length_of_chord_endpoints_is_greater = 1
            count_blue_endpoints += 1
        count_red_endpoints = index_of_iteration + 1 - count_blue_endpoints

        # updating the count of the blue color and red color chords and calculating the probability that a chord is blue, that is , length of the chord is greater than the threshold value
        # Displaying the count of blue and red chords, and probability of getting a blue chord
        # Red color : length of chord is less than or equal to the threshold value
        # Blue color : length of the chord is greater than the threshold value
        plots[1].set_title(f"Random Endpoints\nRed: {count_red_endpoints}  Blue: {count_blue_endpoints}  P(Blue): {round(count_blue_endpoints / (index_of_iteration + 1) , 3)} " , fontweight = 'bold')

        # plotting the line in the 3D plot for Random endpoints
        plots[1].plot([x1,x2] , [y1,y2] , [z1 , z2] ,list_color[if_length_of_chord_endpoints_is_greater] )







        # Generate a random midpoint(x_midpoint , y_midpoint , z_midpoint)

        z = rd.uniform(0,1,1) # choosing a value for z from 0 to 1

        # for choosing x and y , x^2 + y^2 = 1 - z^2
        # choosing y from 0 to sqrt(1 - z**2)

        y = rd.uniform(0, np.sqrt(1 - z**2) , 1)

        # for given z and y, choosing x from 0 to sqrt(1 - y**2 - z**2)
        x = rd.uniform(0, np.sqrt(1 - y**2 - z**2) ,1)

        # for a given value of x or y or z , it can either be positve or negative
        # As we are only choosing positive value of x, y  and z above, we will randomly choose whether the number is positive or negative
        x_negative = (-1)*x
        y_negative = (-1)*y
        z_negative = (-1)*z
        
        #print(x[0] , x)
        x_midpoint = np.array([rd.choice([x_negative[0] , x[0]])])
        y_midpoint = np.array([rd.choice([y_negative[0] , y[0]])])
        z_midpoint = np.array([rd.choice([z_negative[0] , z[0]])])

        
        # Calculating the distance of midpoint from origin
        r2 = np.sqrt( x_midpoint**2 + y_midpoint**2 + z_midpoint**2)

        # Calculating the length of the chord using the formula 2 * sqrt(1 - (r**2))
        length_of_chord_midpoint = 2 * (np.sqrt(1 - (r2 ** 2)))

        # Checking whether the length of the chord is greater than the threshold length and changing its color in the plot
        if_length_of_chord_midpoint_is_greater = 0 # counter variable to know whether the length of the chord ig greater than the threshold length or not
        if length_of_chord_midpoint > threshold_length :
            if_length_of_chord_midpoint_is_greater = 1
            count_blue_midpoint += 1
        count_red_midpoint = (index_of_iteration + 1) - count_blue_midpoint


        # Choosing a random vector onto the sphere in terms of polar coordinates

        vector_theta = rd.uniform(0 , np.pi , 1)
        vector_phi = rd.uniform(0 , 2 * np.pi , 1)

        vector = np.array([1 * np.sin(vector_theta) * np.cos(vector_phi) , 1 * np.sin(vector_theta) * np.sin(vector_phi) , 1 * np.cos(vector_theta)])

        # To find the vector which is perpendicular to the vector formed by joining centre and the mid point , we can subtract the component of random vector along the vector joining center and midpoint, from the random vector

        midpoint_vector = np.array([x_midpoint , y_midpoint , z_midpoint])  # creating a vector joining the centre and midpoint
        parallel_component =  (((vector[0]  * midpoint_vector[0]) + (vector[1] * midpoint_vector[1]) + (vector[2] * midpoint_vector[2])) / (r2 ** 2)) * midpoint_vector# finding the parallel component of vector along the midpoint 
        required_vector = (vector - parallel_component) # Subtarcting the parallel component from vector to get a random direction perpendicular to midpoint_vector

        # Using the required_vector to get a "RANDOM POINT" on the sphere such that the line joining the midpoint and the " RANDOM POINT " is perpendicular to the midpoint vector
        # Converting the above vector into a unit vector and multiplying it with half the length of chord to get the position vector

        vector_point = (required_vector/(np.sqrt((required_vector[0] ** 2) + (required_vector[1] ** 2) + (required_vector[2] ** 2))))*(length_of_chord_midpoint / 2)

        # adding the midpoint_vector with above vector to get the given point
        point = vector_point + midpoint_vector

        x1_midpoint = point[0] # Obtaining a random point such that line joining midpoint and the random point is perpendicukar to the line joining origin and midpoint
        y1_midpoint = point[1]
        z1_midpoint = point[2]
        x2_midpoint = (2*x_midpoint) - x1_midpoint  # Obtaining the second point using midpoint condition
        y2_midpoint = (2*y_midpoint) - y1_midpoint
        z2_midpoint = (2*z_midpoint) - z1_midpoint

        # Plotting the chord joining the above points in the 3D plot and changing the color based on its length
        plots[0].plot([x1_midpoint , x2_midpoint] , [y1_midpoint , y2_midpoint] , [z1_midpoint , z2_midpoint] , list_color[if_length_of_chord_midpoint_is_greater])


        # updating the count of the blue color and red color chords and calculating the probability that a chord is blue, that is , length of the chord is greater than the threshold value
        # Displaying the count of blue and red chords, and probability of getting a blue chord
        # Red color : length of chord is less than or equal to the threshold value
        # Blue color : length of the chord is greater than the threshold value
        plots[0].set_title(f"Random Midpoint\nRed: {count_red_midpoint}  Blue: {count_blue_midpoint}  P(Blue): {round(count_blue_midpoint / (index_of_iteration + 1) , 3)} " , fontweight = 'bold')
        
        
        plt.pause(0.3)
        #plt.show()


simulate_bertrands_paradox( np.sqrt(3),100)

        

