import requests
import keyboard
import mouse
import time
import json
import random

class Bot:

	def __init__(self):
		self.inGame = False
		self.currentLevel = 0
		self.findNewGame = False
		self.userResolution = "1366 x 768"
		print("")
		print(" ***************************        BOT STARTED           ***************************")
		print(" (Ctrl + C to exit) ")
		print("")

	def startClient(self, forCoop):
		if forCoop:
			if self.userResolution == "1366 x 768":
				mouse.move(160, 62) # Play button
				mouse.click()
				time.sleep(2.5)
				mouse.move(176, 119) # Bot coop tab
				mouse.click()
				time.sleep(2.5)
				mouse.move(574, 704) # Confirm bot coop 
				mouse.click()
				time.sleep(2)
				mouse.click()
				mouse.move(680, 574) # Accept queue or try to accept

				QueueClick = 25 # Click accept queue for 50 seconds (If you enter a match it will still be clicking but there's enough time to pick a champ)

				for sec in range(QueueClick):
					mouse.click()
					time.sleep(2)

				mouse.move(426, 288) # Select champ
				mouse.click()
				time.sleep(2.5)
				mouse.move(685, 627) # Confirm champ
				mouse.click()
				time.sleep(2.5)
			elif self.userResolution == "1920 x 1080":
				mouse.move(245, 111) # Play button
				mouse.click()
				time.sleep(2.5)
				mouse.move(274, 171) # Bot coop tab
				mouse.click()
				time.sleep(2.5)
				mouse.move(660, 758) # Confirm bot coop 
				mouse.click()
				time.sleep(2)
				mouse.click()
				mouse.move(770, 628) # Accept queue or try to accept

				QueueClick = 25 # Click accept queue for 50 seconds (If you enter a match it will still be clicking but there's enough time to pick a champ)

				for sec in range(QueueClick):
					mouse.click()
					time.sleep(2)

				mouse.move(506, 336) # Select champ
				mouse.click()
				time.sleep(2.5)
				mouse.move(766, 680) # Confirm champ
				mouse.click()
				time.sleep(2.5)
		else:
			if self.userResolution == "1366 x 768":
				mouse.move(160, 62) # Play button
				mouse.click()
				time.sleep(2.5)
				mouse.move(309, 121) # Training Tool Tab
				mouse.click()
				time.sleep(2.5)
				mouse.move(669, 239) # Training Tool Option
				mouse.click()
				time.sleep(2.5)
				mouse.move(581, 706) # Traning Tool Accept
				mouse.click()
				time.sleep(2.5)
				mouse.click()
				time.sleep(2.5)
				mouse.move(425, 189) # Random champ
				mouse.click()
				time.sleep(2.5)
				mouse.move(682, 629) # Select random champ
				mouse.click()
				time.sleep(2.5)
			elif self.userResolution == "1920 x 1080":
				mouse.move(245, 111) # Play button
				mouse.click()
				time.sleep(2.5)
				mouse.move(378, 170) # Training Tool Tab
				mouse.click()
				time.sleep(2.5)
				mouse.move(725, 287) # Training Tool Option
				mouse.click()
				time.sleep(2.5)
				mouse.move(662, 760) # Traning Tool Accept
				mouse.click()
				time.sleep(2.5)
				mouse.click()
				time.sleep(2.5)
				mouse.move(511, 241) # Random champ
				mouse.click()
				time.sleep(2.5)
				mouse.move(769, 685) # Select random champ
				mouse.click()
				time.sleep(2.5)

	def continueQueue(self):
		if self.userResolution == "1366 x 768":
			mouse.move(574, 704) # Confirm bot coop 
			mouse.click()
			time.sleep(2)
			mouse.move(680, 574) # Accept queue or try to accept

			QueueClick = 25 # Click accept queue for 50 seconds (If you enter a match it will still be clicking, but there's enough time to pick a champ)

			for sec in range(QueueClick):
				mouse.click()
				time.sleep(2)

			mouse.move(426, 288) # Select champ
			mouse.click()
			time.sleep(2.5)
			mouse.move(685, 627) # Confirm champ
			mouse.click()
			time.sleep(2.5)
		elif self.userResolution == "1920 x 1080":
			mouse.move(660, 758)
			mouse.click()
			time.sleep(2)
			mouse.move(770, 628) # Accept queue or try to accept

			QueueClick = 25 # Click accept queue for 50 seconds (If you enter a match it will still be clicking but there's enough time to pick a champ)

			for sec in range(QueueClick):
				mouse.click()
				time.sleep(2)

			mouse.move(506, 336) # Select champ
			mouse.click()
			time.sleep(2.5)
			mouse.move(766, 680) # Confirm champ
			mouse.click()
			time.sleep(2.5)

	def checkInGame(self):
		try:
			r = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
			if r.status_code != 200:
				self.inGame = False
				self.currentLevel = 0
				return False
		except:
			self.inGame = False
			self.currentLevel = 0
			return False
		self.inGame = True
		return True

	def moveChamp(self):
		firstTower = False
		secondTower = False
		thirdTower = False
		inhibiBot = False
		NexusTowerOne = False
		NexusTowerTwo = False

		r = requests.get("https://127.0.0.1:2999/liveclientdata/eventdata", verify=False)
		response = r.json()

		for event in response['Events']:
			if event['EventName'] == 'TurretKilled' and event['TurretKilled'] == 'Turret_T2_R_03_A':
				firstTower = True
			elif event['EventName'] == 'TurretKilled' and event['TurretKilled'] == 'Turret_T2_R_02_A':
				secondTower = True
			elif event['EventName'] == 'TurretKilled' and event['TurretKilled'] == 'Turret_T2_R_01_A':
				thirdTower = True
			elif event['EventName'] == 'InhibKilled' and event['InhibKilled'] == 'Barracks_T2_R1':
				inhibiBot = True
			elif event['EventName'] == 'TurretKilled' and event['TurretKilled'] == 'Turret_T2_C_01_A':
				NexusTowerOne = True
			elif event['EventName'] == 'TurretKilled' and event['TurretKilled'] == 'Turret_T2_C_02_A':
				NexusTowerTwo = True
			elif event['EventName'] == "GameEnd":
				self.findNewGame = True
				print("")
				print(" ***************************    GAME FINISHED!    *************************** ")
				print("")

		

		if self.userResolution == "1366 x 768":
			if not firstTower:
				moveList = [(1160, 727), (1164, 719), (1170, 724), (1166, 734), (1171, 721)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not secondTower:
				moveList = [(1174, 686), (1169, 673), (1177, 674), (1171, 685), (1175, 672)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not thirdTower:
				moveList = [(1180, 656), (1179, 660), (1174, 650), (1173, 659), (1180, 647)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not inhibiBot:
				moveList = [(1175, 636), (1169, 640), (1170, 636), (1171, 627), (1170, 629)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not NexusTowerOne:
				moveList = [(1166, 624), (685, 412), (1170, 624), (1167, 621), (1163, 626)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not NexusTowerTwo:
				moveList = [(1163, 626), (1161, 620), (1168, 617), (1164, 620), (1160, 617)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
		elif self.userResolution == "1920 x 1080":
			if not firstTower:
				moveList = [(1256, 787), (1252, 782), (1245, 796), (1243, 781), (1250, 784)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not secondTower:
				moveList = [(1257, 752), (1262, 746), (1256, 742), (1264, 737), (1240, 728)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not thirdTower:
				moveList = [(1261, 712), (1250, 707), (1261, 702), (1252, 702), (1258, 709)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not inhibiBot:
				moveList = [(1254, 690), (1257, 687), (1265, 685), (1258, 692), (1254, 685)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not NexusTowerOne:
				moveList = [(1251, 675), (1258, 674), (1252, 674), (1248, 671), (1244, 673)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()
			elif not NexusTowerTwo:
				moveList = [(1242, 667), (1244, 668), (1252, 662), (1240, 669), (1244, 666)]
				actualMove = random.choice(moveList)
				mouse.move(actualMove[0], actualMove[1])
				keyboard.press_and_release('A')
				mouse.click()

	def playAgain(self):
		if self.userResolution == "1366 x 768":
			mouse.move(580, 706)
			mouse.click()
			time.sleep(2)
		elif self.userResolution == "1920 x 1080":
			mouse.move(664, 752)
			mouse.click()
			time.sleep(2)

	def pickRewards(self):
		self.findNewGame = False
		time.sleep(15) # Wait for client

		if self.userResolution == "1366 x 768":
			# Clash notice possible appearance (generally when clash event is active)
			mouse.move(681, 688)
			mouse.click()
			time.sleep(1.5)

			mouse.move(619, 453) # Honor
			mouse.click()
			time.sleep(5)

			mouse.move(685, 697) # Confirm possible level up
			confirmClick = 3
			for sec in range(confirmClick):
				mouse.click()
				time.sleep(2)

			mouse.move(678, 412) # This is in case bot is offered a new champ
			selectOfferedChamp = 3
			for sec in range(selectOfferedChamp):
				mouse.click()
				time.sleep(2)

			mouse.move(685, 697) # confirm		
			confirmOfferedChamp = 3
			for sec in range(confirmOfferedChamp):
				mouse.click()
				time.sleep(2)

			mouse.move(685, 697) # confirm any kind of mission or rewards given
			confirmAnything = 6
			for sec in range(confirmAnything):
				mouse.click()
				time.sleep(2)
		elif self.userResolution == "1920 x 1080":
			# Clash notice possible appearance (generally when clash event is active)
			mouse.move(764, 735)
			mouse.click()
			time.sleep(1.5)

			mouse.move(907, 436) # Honor
			mouse.click()
			time.sleep(5)

			mouse.move(769, 749) # Confirm possible level up
			confirmClick = 3
			for sec in range(confirmClick):
				mouse.click()
				time.sleep(2)

			mouse.move(763, 458) # This is in case bot is offered a new champ
			selectOfferedChamp = 3
			for sec in range(selectOfferedChamp):
				mouse.click()
				time.sleep(2)

			mouse.move(769, 749) # confirm		
			confirmOfferedChamp = 3
			for sec in range(confirmOfferedChamp):
				mouse.click()
				time.sleep(2)

			mouse.move(769, 749) # confirm any kind of mission or rewards given
			confirmAnything = 6
			for sec in range(confirmAnything):
				mouse.click()
				time.sleep(2)


	def checkLevel(self):
		if self.inGame:
			r = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
			info = r.json()
			return int(info["activePlayer"]["level"])

print("")
print(" ***************************                       ***************************")
print(" ***************************                       ***************************")
print(" *************************** LEAGUE OF LEGENDS BOT ***************************")
print(" ***************************                       ***************************")
print(" ***************************                       ***************************")
print(" ***************************        MENU           ***************************")
print(" ***************************                       ***************************")
print(" 1) Start Coop Bot (Make sure you didn't move the client from its initial position)")
print(" 2) Practice Tool Bot")
print(" 3) Exit")

ignoreAll = False
coopBot = False
practiceBot = False

while(True):
	try:
		option = int(input("Option (1 | 2 | 3): "))
		if option == 3:
			ignoreAll = True
			break
		elif option == 1:
			coopBot = True
			break
		elif option == 2:
			practiceBot = True
			break
		else:
			print("Invalid option.")
			continue
	except:
		print("Invalid option.")

if not ignoreAll and coopBot:
	gameBot = Bot()

	print("")
	print("Please select your screen resolution: ")
	print("")
	print("1. 1920 x 1080")
	print("2. 1366 x 768 (default)")
	print("")

	while True:
		try:
			resolution = int(input("Option 1 | 2: "))

			if resolution == 1:
				gameBot.userResolution = "1920 x 1080"
				break
			elif resolution == 2:
				gameBot.userResolution = "1366 x 768"
				break
			else:
				print("Invalid option.")
				continue
		except:
			print("Invalid option.")
			continue



	gameBot.startClient(forCoop = True)
	dodgeCounter = 0

	while True:
		if (gameBot.checkInGame()):
			dodgeCounter = 0
			print("")
			print("STATUS: Summoner in game.")
			print("")

			if gameBot.checkLevel != gameBot.currentLevel:
				keyboard.press_and_release('left Ctrl + R')
				keyboard.press_and_release('left Ctrl + Q')
				keyboard.press_and_release('left Ctrl + E')
				keyboard.press_and_release('left Ctrl + W')
				gameBot.currentLevel += 1
				gameBot.moveChamp()

			time.sleep(4.5)
		else:
			print(dodgeCounter)
			if dodgeCounter >= 40: # If someone dodged champ select and bot is not click accept match button anymore, then this will wait 3 minutes and start looking for another game.
				print("Trying to find a new game...")
				gameBot.continueQueue()

			print("")
			print("STATUS: Summoner NOT in game")
			print("")

			if gameBot.findNewGame:
				gameBot.pickRewards()
				gameBot.playAgain()
				gameBot.continueQueue()
				dodgeCounter = 0

			time.sleep(5)
			dodgeCounter += 1

if not ignoreAll and practiceBot:
	gameBot = Bot()

	print("")
	print("Please select your screen resolution: ")
	print("")
	print("1. 1920 x 1080")
	print("2. 1366 x 768 (default)")
	print("")

	while True:
		try:
			resolution = int(input("Option 1 | 2: "))

			if resolution == 1:
				gameBot.userResolution = "1920 x 1080"
				break
			elif resolution == 2:
				gameBot.userResolution = "1366 x 768"
				break
			else:
				print("Invalid option.")
				continue
		except:
			print("Invalid option.")
			continue

	gameBot.startClient(forCoop = False)

	while True:
		if (gameBot.checkInGame()):
			print("")
			print("STATUS: Summoner in game.")
			print("")

			if gameBot.checkLevel != gameBot.currentLevel:
				keyboard.press_and_release('left Ctrl + R')
				keyboard.press_and_release('left Ctrl + Q')
				keyboard.press_and_release('left Ctrl + E')
				keyboard.press_and_release('left Ctrl + W')
				gameBot.currentLevel += 1
				gameBot.moveChamp()

			time.sleep(4.5)
		else:
			print("")
			print("STATUS: Summoner NOT in game")
			print("")

			if gameBot.findNewGame:
				gameBot.pickRewards()
				gameBot.playAgain()
				gameBot.continueQueue()

			time.sleep(5)
else:
	print("")
	print("Thanks for using this bot!")
	print("Bot developed using Python.")
	input("...")
