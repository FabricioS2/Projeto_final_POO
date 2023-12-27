import pygame
import abc
from os.path import join
from abc import abstractmethod


class MixIn_Son(abc.ABC):

    @abstractmethod
    def gerar_som():
        pass

