import pygame


running = True
pygame.init()
pygame.display.set_caption('game in life')
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 60
clock = pygame.time.Clock()

circle_center_x = screen_width//2
circle_center_y = screen_height//2
circle_radius_x = 100
circle_radius_y = 27
naprav = 1
coube_height = 100
help_value = (circle_radius_x**2)*(circle_radius_y**2)
def field_maker(y):

    points = []
    for i in range(circle_center_y-circle_radius_y,circle_center_y+circle_radius_y+1):
        if i == circle_center_y - y or i == circle_center_y + y:
            for j in range(circle_center_x - circle_radius_x,circle_center_x + circle_radius_x+1):
                a = int(((help_value-(((j-screen_width/2)**2)*circle_radius_y**2))//circle_radius_x**2)**0.5)
                if int(y) == int(((help_value-(((j-screen_width/2)**2)*circle_radius_y**2))//circle_radius_x**2)**0.5):


                    if i == circle_center_y - y:
                        points.append([j,i,naprav])
                    else:
                        points.append([j, i, naprav-1])

    points = [points[0],points[len(points)//2-1],points[-1],points[len(points)//2]]
    return(points)
speed = 20
points = field_maker((circle_radius_y-speed)//2)
mode = 0

circle_radius_y_original = circle_radius_y
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                points = []
                circle_radius_y +=speed
                help_value = (circle_radius_x ** 2) * (circle_radius_y ** 2)
                points = field_maker(circle_radius_y//2)
                print(circle_radius_y)

    screen.fill((0, 0, 0))
    #way 1
    # for y in range(circle_center_y-circle_radius_y,circle_center_y+circle_radius_y+1):
    #
    #     for x in range(circle_center_x - circle_radius_x,circle_center_x + circle_radius_x+1):
    #
    #
    #         if ((x-screen_width/2)**2)/(circle_radius_x**2)+ ((y-screen_height/2)**2)/(circle_radius_y**2) == 1:
    #
    #             pygame.draw.line(screen,(0,255,0),(x,y),(x,y-1),5)

    #way 2
    # for x in range(circle_center_x - circle_radius_x,circle_center_x + circle_radius_x+1):
    #
    #     y = ((help_value-(((x-screen_width/2)**2)*circle_radius_y**2))//circle_radius_x**2)**0.5
    #
    #
    #     pygame.draw.line(screen, (0, 255, 0), (x, (y+screen_height/2)), (x, (y+screen_height/2)-1), 1)
    #
    #     pygame.draw.line(screen, (0, 255, 0), (x, (y+screen_height/2)- 2*y), (x, (y+screen_height/2)- 2*y-1), 1)
    for i in range(len(points)):

        y = ((help_value - (((points[i][0] - screen_width / 2) ** 2) * circle_radius_y ** 2)) // circle_radius_x ** 2) ** 0.5


        if points[i][2]==1 :

            points[i][1] = screen_height//2 -y
        else:
            points[i][1] = screen_height//2+y


        if points[i][2] == 1:
            points[i][0] += 1
        else:
            points[i][0] -= 1

        if points[i][0] >= circle_center_x+circle_radius_x:
            points[i][2] = 0

        elif points[i][0] <= circle_center_x - circle_radius_x:
            points[i][2] = 1

    # if mode == 0:
    #     if circle_radius_y>0:
    #         circle_radius_y -=speed
    #     else:
    #         mode = 1
    # else:
    #     if circle_radius_y<circle_radius_y_original:
    #         circle_radius_y -=speed
    #     else:
    #         mode = 0

    for i in range(len(points)):

        pygame.draw.line(screen,(0,255,0), (points[i][0],points[i][1]),(points[i-1][0],points[i-1][1]),1)

        pygame.draw.line(screen, (0, 255, 0), (points[i][0], points[i][1]+coube_height), (points[i - 1][0], points[i - 1][1]+coube_height))
        pygame.draw.line(screen, (0, 255, 0), (points[i][0], points[i][1]), (points[i][0], points[i][1]+coube_height))

    clock.tick(fps)
    pygame.display.flip()
