import pygame
import config
import sys
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def gen_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pipes_spawn_time = 10

    while True:
        quit_game()
        config.window.fill((0, 0, 0))
        config.ground.draw(config.window)

        if pipes_spawn_time <= 0:
            gen_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)

        if not population.extinct():
            population.update_live_players()
        else :
            config.pipes.clear()
            population.enhance_update()

        
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':

    main()
