from Personnage import Characters
from Personnage import CharactersManager
from treasures import TreasureManager
import MapManager
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

WIDTH = 50
HEIGHT = 50
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
TIMEOUT = 100

def renderMap(window, map):
	i = 0

	while i < len(map):
		j = 0
		while j < len(map[i]):
			if map[i][j] == 3:
				window.addstr(i + 1, j + 1, '#')
			elif map[i][j] == 2:
				window.addstr(i + 1, j + 1, '+')
			elif map[i][j] == 1:
				window.addstr(i + 1, j + 1, '.')
			j = j + 1
		i = i + 1

if __name__ == '__main__':
	curses.initscr()
	curses.beep()
	curses.beep()
	window = curses.newwin(HEIGHT, WIDTH, 0, 0)
	window.timeout(TIMEOUT)
	window.keypad(1)
	curses.noecho()
	curses.curs_set(0)
	window.border(0)

	characterManager = CharactersManager()
	treasureManager = TreasureManager()
	myMap = MapManager.Map()
	myMap.creer_niveau()
	coord = myMap.listeSalles[1][1].pos
	character = Characters("me", (coord[0] + 2, coord[1] + 2), 100, 10, 0.8, 10)

	while True:
		window.clear()
		window.border(0)

		renderMap(window, myMap.carte)
		window.addstr(character.position[0] + 1, character.position[1] + 1, '*')

		for monster in characterManager.instance.charactersList:
			window.addstr(monster.position[0] + 1, monster.position[1] + 1, 'M')
		
		for treasure in treasureManager.instance.treasures:
			window.addstr(treasure.pos[0] + 1, treasure.pos[1] + 1, 'T')

		event = window.getch()

		if event == 27:
			break

		if event == KEY_UP:
			character.move(characterManager, myMap, "nord")
		elif event == KEY_DOWN:
			character.move(characterManager, myMap, "sud")
		elif event == KEY_LEFT:
			character.move(characterManager, myMap, "ouest")
		elif event ==KEY_RIGHT:
			character.move(characterManager, myMap, "est")

		# if snake.head.x == food.x and snake.head.y == food.y:
		# 	snake.eat_food(food)

		if event == 32:
			key = -1
			while key != 32:
				key = window.getch()

	curses.endwin()