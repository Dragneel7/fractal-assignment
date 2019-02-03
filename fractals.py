import pygame, math, sys, time

iterations = int(sys.argv[1])  # No. of iterations to run the fractal generating algorithm.

pygame.init()
  
# Create a new surface and window to display the fractal tree pattern. 
surface_height, surface_width = 1200, 1000 
main_surface = pygame.display.set_mode((surface_height,surface_width)) 
pygame.display.set_caption("My Fractal Tree Pattern") 
  
def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0): 
    """ Function to draw the fractal tree pattern.
    :param order: integer, No. pf divisions from the tree
    :param theta: float, Angle by which to rotate the next fractal pattern
    :param sz: integer, Size of new fractal pattern
    :param posn: float, Position for the new pattern
    :param heading: float, width of the pattern
    :param color: integer, color of the new patter
    :param depth: integer, depth of the fractal
    """
    trunk_ratio = 0.3  # The relative ratio of the trunk to the whole tree.     

    # Length of the trunk   
    trunk = sz * trunk_ratio 
    delta_x = trunk * math.cos(heading) 
    delta_y = trunk * math.sin(heading) 
    (u, v) = posn 
    newpos = (u + delta_x, v + delta_y) 
    pygame.draw.line(main_surface, color, posn, newpos) 

    if order > 0: 
        """ Make 2 halfs for the fractal tree symmetrical around the trunk.
        """
        if depth == 0: 
            color1 = (255, 0, 0) 
            color2 = (0, 0, 255) 
        else: 
            color1 = color 
            color2 = color 

        # make the recursive calls, which can be considered as zooming into the fractal pattern. 
        newsz = sz*(1 - trunk_ratio) 
        draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1) 
        draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1) 
  
  
def main(): 
    theta = 0
    for _ in range(iterations): 
        theta += 0.01  # Update the angle
        main_surface.fill((255, 255, 0)) 
        draw_tree(9, theta, surface_height*0.9, (surface_width//2, surface_width-50), -math.pi/2) 
        pygame.display.flip()
    time.sleep(20)  # Makes the fractal tree visible for 20 sec. 
  
main()  # Calling the main function 
