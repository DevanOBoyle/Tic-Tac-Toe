import sys, pygame

blue = (81, 61, 255)
red = (255, 38, 38)
black = (0, 0, 0)
white = (255, 255, 255)

squares = {
    1: pygame.Rect(105, 35, 90, 90),
    2: pygame.Rect(206, 35, 90, 90),
    3: pygame.Rect(306, 35, 90, 90),
    4: pygame.Rect(105, 136, 90, 90),
    5: pygame.Rect(206, 136, 90, 90),
    6: pygame.Rect(306, 136, 90, 90),
    7: pygame.Rect(105, 236, 90, 90),
    8: pygame.Rect(206, 236, 90, 90),
    9: pygame.Rect(306, 236, 90, 90)
}

win_lines = [
    [(125, 55), (376, 306)],
    [(376, 55), (125, 306)],
    [(125, 80), (376, 80)],
    [(125, 181), (376, 181)],
    [(125, 281), (376, 281)],
    [(150, 55), (150, 306)],
    [(251, 55), (251, 306)],
    [(351, 55), (351, 306)]
]

def draw_x(surface, square):
    pygame.draw.line(
        surface, 
        blue, 
        (squares[square].left + 20, squares[square].top + 20), 
        (squares[square].left + squares[square].width - 20, squares[square].top + squares[square].height - 20), 
        15
    )
    pygame.draw.line(
        surface, 
        blue, 
        (squares[square].left + squares[square].width - 20, squares[square].top + 20), 
        (squares[square].left + 20, squares[square].top + squares[square].height - 20),
        15
    )

def draw_o(surface, square):
    pygame.draw.circle(
        surface,
        red,
        (squares[square].left + squares[square].width/2, squares[square].top + squares[square].height/2),
        30,
        15
    )

def check_win(player):
    points = set(player)
    if set([1,2,3]).issubset(points):
        return True, 2
    elif set([1,4,7]).issubset(points):
        return True, 5
    elif set([1,5,9]).issubset(points):
        return True, 0
    elif set([2,5,8]).issubset(points):
        return True, 6
    elif set([4,5,6]).issubset(points):
        return True, 3
    elif set([3,5,7]).issubset(points):
        return True, 1
    elif set([3,6,9]).issubset(points):
        return True, 7
    elif set([7,8,9]).issubset(points):
        return True, 4
    return False, -1

def main():
    pygame.init()

    x,y = 500, 460

    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("TicTacToe")

    font = pygame.font.Font('freesansbold.ttf', 35)
    text_x = font.render("X Go", True, blue)
    text_o = font.render("O Go", True, red)
    win_x = font.render("X Wins!", True, blue)
    win_o = font.render("O Wins!", True, red)
    text_tie = font.render("Tie", True, white)

    rect_x = text_x.get_rect()
    rect_x.center = (x // 2, y - 60)

    rect_o = text_o.get_rect()
    rect_o.center = (x // 2, y - 60)

    rect_win_x = win_x.get_rect()
    rect_win_x.center = (x // 2, y - 60)

    rect_win_o = win_o.get_rect()
    rect_win_o.center = (x // 2, y - 60)

    rect_tie = text_tie.get_rect()
    rect_tie.center = (x // 2, y - 60)


    player_x, player_o = [], []
    x_turn = True

    win_line = -1

    x_win = False
    o_win = False
    tie = False

    while True:
        screen.fill(black)

        # draws the game board
        pygame.draw.line(screen, white, (200, 35), (200, 325), 11)
        pygame.draw.line(screen, white, (300, 35), (300, 325), 11)
        pygame.draw.line(screen, white, (105, 130), (395, 130), 11)
        pygame.draw.line(screen, white, (105, 230), (395, 230), 11)

        curr_square = 0
        # highlights each square on mouse hover
        for i in squares:
            if squares[i].collidepoint(pygame.mouse.get_pos()):
                rect_light = pygame.Surface(squares[i].size)
                rect_light.set_alpha(210)
                pygame.draw.rect(screen, white, squares[i])
                screen.blit(rect_light, squares[i])
                curr_square = i
        
        for i in player_x:
            draw_x(screen, i)
        for i in player_o:
            draw_o(screen, i)

        if (x_win):
            pygame.draw.line(
                screen,
                blue,
                (win_lines[win_line][0]), 
                (win_lines[win_line][1]), 
                15
            )
            screen.blit(win_x, rect_win_x)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                pygame.display.update()

        elif (o_win):
            pygame.draw.line(
                screen, 
                red,
                (win_lines[win_line][0]), 
                (win_lines[win_line][1]), 
                15
            )
            screen.blit(win_o, rect_win_o)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                pygame.display.update()

        elif (tie):
            screen.blit(text_tie, rect_tie)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if (pygame.mouse.get_pressed()[0] == 1) and curr_square != 0:
                    if x_turn and curr_square not in player_o:
                        draw_x(screen, curr_square)
                        player_x.append(curr_square)
                        x_win, win_line = check_win(player_x)
                        x_turn = not x_turn
                    elif not x_turn and curr_square not in player_x:
                        draw_o(screen, curr_square)
                        player_o.append(curr_square)
                        o_win, win_line = check_win(player_o)
                        x_turn = not x_turn
                    if (len(player_x) + len(player_o) == 9):
                        tie = True
                pygame.display.update()

if __name__ == "__main__":
    main()
