import pygame
from pygame.locals import *
import modulos.constantes as cos

pygame.init()

class Alma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
        pygame.image.load('PCS/assets/sprites/alma.png'),
        pygame.image.load('PCS/assets/sprites/almaazul.png'),
        pygame.image.load('PCS/assets/sprites/almaverde.png'),    
        ]
        self.game_over = pygame.image.load('PCS/assets/sprites/almaquebrada.png')
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = cos.x, cos.y
        self.acertavel = True
        self.tempo_inicial = None
        self.tempo_atual = None
        #self.gnomo = True

    def update(self):
        self.rect.center = cos.x, cos.y
        if self.acertavel == False:
            self.image = pygame.image.load('PCS/assets/sprites/almavazia.png')
        else:
            self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))

    def iframe(self):
        global fimInv, tempoInv
        '''if self.gnomo:
            self.tempo_inicial = pygame.time.get_ticks()
            self.gnomo = False
            
        self.tempo_atual = pygame.time.get_ticks()
        print(f'Tempo Atual: {self.tempo_atual}')
        print(f'Tempo Inicial: {self.tempo_inicial}')
        if self.tempo_inicial - self.tempo_atual <= cos.tempoInv:'''
        self.acertavel = False
        pygame.time.set_timer(cos.fimInv, cos.tempoInv, 1)

    def trocaestado(self, novoestado=0):#auto explicativo
        if novoestado == '+':
            self.estado += 1
        else:
            self.estado = int(novoestado)

alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)

class Wilson(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('PCS/assets/sprites/Wilsoniddle.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = 300, 87

wilson_sprite = Wilson()
artes.add(wilson_sprite)

class AnimacaoAtaque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_ataque = []
        for i in range(6):
            img = cos.sprite_sheet.subsurface((0, i * 12), (12,12))
            img = pygame.transform.scale(img, (12 * 2, 12*5))
            self.imagens_ataque.append(img)

        self.indexLista = 0
        self.image = self.imagens_ataque[self.indexLista]
        self.rect = self.image.get_rect()
        self.rect.center = (300, 220)
        
    def update(self):
        if self.indexLista > 5:
            self.indexLista = 0
        self.indexLista += 0.25
        self.image = self.imagens_ataque[int(self.indexLista)]
    
    
ataques_sprite = AnimacaoAtaque()
artes.add(ataques_sprite)
print('alma carregando...')
