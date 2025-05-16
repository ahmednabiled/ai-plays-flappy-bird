import pygame
import random
import config
import perceptron

class Player:
    def __init__(self):
        
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.speed = 0
        self.flap = False
        self.alive = True
        self.flap_cooldown = 0
        self.lifespan = 0


        self.decision = None
        self.vision = [0.5, 1, 0.5]
        self.inputs = 3
        self.perceptron = perceptron.Perceptron(self.inputs)
        self.perceptron.gen_net()
        self.fitness = 0

    def draw(self, window):
        
        pygame.draw.rect(window, self.color, self.rect)

    def ground_collision(self, ground):
        
        return self.rect.colliderect(ground)

    def sky_collision(self):
        
        return self.rect.y < 30

    def pipe_collision(self):
        
        for p in config.pipes:
            if self.rect.colliderect(p.top_rect) or self.rect.colliderect(p.bottom_rect):
                return True
        return False

    def update(self, ground):
        
        if self.alive and not (self.ground_collision(ground) or self.pipe_collision()):
            self.speed += 0.3  
            self.rect.y += self.speed
            if self.speed > 5:  
                self.speed = 5
        else:
            self.alive = False
            self.flap = False
            self.speed = 0

    def bird_flap(self):
        if self.alive and not self.flap and not self.sky_collision() and self.flap_cooldown <= 0:
            self.flap = True
            self.speed = -5  
            self.lifespan += 1
            # self.flap_cooldown = 20  
        if self.speed >= 2:  
            self.flap = False

    # def pressed(self):
    #     # Handle mouse input for flapping
    #     mouse_buttons = pygame.mouse.get_pressed()
    #     if mouse_buttons[0]:  # Left mouse button (index 0)
    #         print("Left mouse button is being held at", pygame.mouse.get_pos())
    #         self.bird_flap()
    #     if self.flap_cooldown > 0:  # Decrease cooldown
    #         self.flap_cooldown -= 1

    @staticmethod
    def closest_pipe():
        for p in config.pipes:
            if not p.passed:
                return p

    def calc_vision(self):
        if config.pipes:
            self.vision[0] = max(0,self.rect.center[1] - self.closest_pipe().top_rect.bottom)/500
            pygame.draw.line(config.window, self.color, self.rect.center,
                            (config.pipes[0].x + config.pipes[0].width // 2, config.pipes[0].top_rect.bottom))


            self.vision[1] = max(0, self.closest_pipe().x - self.rect.center[0]) / 500

            opening_middle_y = (config.pipes[0].top_rect.bottom + config.pipes[0].bottom_rect.top) // 2

            pygame.draw.line(config.window, self.color, self.rect.center,
                            (config.pipes[0].x + config.pipes[0].width // 2, opening_middle_y))

            self.vision[2] = max(0, self.closest_pipe().bottom_rect.top - self.rect.center[1]) / 500

            pygame.draw.line(config.window, self.color, self.rect.center,
                            (config.pipes[0].x + config.pipes[0].width // 2, config.pipes[0].bottom_rect.top))

    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Player()
        clone.fitness = self.fitness
        clone.perceptron = self.perceptron.clone()
        clone.perceptron.gen_net()
        return clone

    def think(self):
        self.decision = self.perceptron.feed_forward(self.vision)
        if self.decision > 0.73:
            self.bird_flap()
