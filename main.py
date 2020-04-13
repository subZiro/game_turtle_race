#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import turtle
from random import randint


window_h = 500
window_w = 500


class TurtleRacer(object):
	"""docstring for TurtleRacer"""
	def __init__(self, position, color):
		self.position = position
		self.color = color

		self.racer = turtle.Turtle()
		self.racer.shape('turtle')  # фигура черепашки
		self.racer.color(color)  # цвет черепашки
		self.racer.penup()  # поднять перо
		self.racer.setpos(position)  # пересестить черепашку на position
		self.racer.setheading(90)  # поворот на 90 градусов


	def restart(self):
		"""рестарт позиций гонщиков"""
		self.racer.penup()  # поднять перо
		self.setpos(self.position)


	def move(self, a=1, b=10):
		"""задание скорости каждому гонщику"""
		speed = randint(a, b)
		self.position = (self.position[0], self.position[1]+speed)
		self.racer.pendown()  # опустить перо
		self.racer.forward(speed)


def racer_to_start(turtles_count=5):
	"""отрисовка гонщиков на стартовой позиции"""
	turtle.clearscreen()
	turtle.hideturtle()

	racers_list = []
	color = ["red", "green", "blue", 'pink', 'orange', 'purple', 'black', 'grey', 'orange']
	start = -(window_w/2) + 20

	for t in range(turtles_count): 
		x = start + t*(window_h)//turtles_count
		racers_list.append(TurtleRacer(color=color[t], position=(x, -200)))
		racers_list[t].racer.showturtle()

	return racers_list

	
def racer_move(racers):
	"""перемещение черепашек к финишу"""
	run = True
	while run:
		for racer in racers:  # перемещение черепашек
			racer.move()

		win_color = []
		maxDis = 0
		for racer in racers:
			if racer.position[1] > 200 and racer.position[1] > maxDis:
				maxDis = racer.position[1]
				win_color = []
				win_color.append(racer.color)
			elif racer.position[1] > 200 and racer.position[1] == maxDis:
				maxDis = racer.position[1]
				win_color.append(racer.color)

		if win_color:  # если есть черепашка достигнувшая финиша отстанавливаем гонку выводим увет победителя
			run = False
			return win_color

			
def output_winner(winners):
	"""вывод информации о победителе"""
	s = 'The Champion of race: '
	for winner in winners:
		s += winner + ', '

	turtle.write(s[:-2], align = 'center', font = ('Arial', 28, 'normal'))


def main():
	"""главная программа"""
	turtle.screensize(window_w, window_h)  # 
	racers = racer_to_start(8)  # отприсовка стартовых позиций
	winners = racer_move(racers)  # отрисовка гонки
	output_winner(winners)  # вывод победителя/лей

	
if __name__ == '__main__':
	main()
