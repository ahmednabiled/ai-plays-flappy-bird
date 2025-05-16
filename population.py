import config
import player
import pygame
import math
import operator
import categories


class Population:
    def __init__(self,size):
        self.players : list[player.Player] = []
        self.size = size
        self.categories : list[categories.categories] = []

        for i in range(size):
            self.players.append(player.Player())
        
        self.generation = 0

    def update_live_players(self):
        for p in self.players:
            if p.alive :
                # self.player.pressed()
                p.calc_vision()
                p.think()
                p.draw(config.window)
                p.update(config.ground)


    def enhance_update(self):
        self.categorize()
        self.calculate_fitness()
        self.sort_categories_by_fitness()
        self.next_gen()

    def categorize(self):
        for c in self.categories:
            c.players = []

        for p in self.players:
            add_to_categories = False
            for c in self.categories:
                if c.similar_to(p.perceptron):
                    c.add_to_categories(p)
                    add_to_categories = True
                    break
            if not add_to_categories:
                self.categories.append(categories.categories(p))

    def calculate_fitness(self):
        for p in self.players:
            p.calculate_fitness()

        for c in self.categories:
            c.calculate_average_fitness()
        
    def sort_categories_by_fitness(self):
        for c in self.categories:
            c.sort_players_by_fitness()
        self.categories.sort(key=operator.attrgetter('benchmark_fitness'),reverse=True)

    def next_gen(self):
        children = []

        for s in self.categories:
            children.append(s.champion.clone())

        children_per_categories = math.floor((self.size - len(self.categories)) / len(self.categories))
        for s in self.categories:
            for i in range(0, children_per_categories):
                children.append(s.offspring())

        while len(children) < self.size:
            children.append(self.categories[0].offspring())

        self.players = []
        for child in children:
            self.players.append(child)
        self.generation += 1


    def extinct(self):
        extinct = True
        for p in self.players:
            if p.alive :
                extinct = False
                
        return extinct