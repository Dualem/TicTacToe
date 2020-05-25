

class Main:

	arr = [
		[' ',' ',' '],
		[' ',' ',' '],
		[' ',' ',' ']
		]

	allowed = ['00','01','02','10','11','12','20','21','22',]
	def loadboard(self):
		print("  _0__1__2_")
		for x in range(0,3, 1):
			print(f"{x}|", end="")
			for y in range(0, 3, 1):

				print(f" {self.arr[x][y]}", end=" ")
			print("|")

	def askX(self):
		while True:
			x = input("X input?(x axis, y axis)")
			if x in self.allowed:
				s = list(str(x))
				s1 = int(s[0])
				s2 = int(s[1])
				if('X' == self.arr[s1][s2] or 'O' == self.arr[s1][s2]):
					print("Already a value in this place, try again...")
				else:
					return x
					break
			else:
				print("Wrong format, try something like '00', '01' ")
		
	
	def askY(self):
		while True:
			y = input("O input?(x axis, y axis)")
			if y in self.allowed:
				#code is duplicate
				s = list(str(y))
				s1 = int(s[0])
				s2 = int(s[1])
				if('X' == self.arr[s1][s2] or 'O' == self.arr[s1][s2]):
					print("Already a value in this place, try again...")
				else:
					return y
					break
			else:
				print("Wrong format, try something like '00', '01' ")
			

	def play(self):
		win = True
		winnerX = 'X'
		winnerO = 'O'
		self.loadboard()
		while win:
			
			x = self.askX()
			self.makemoveX(x)
			#checkwin
			win = self.win()
			if(win != True):
				self.loadboard()

				return winnerX
			self.loadboard()
			y = self.askY()
			self.makemoveY(y)
			win = self.win()
			if(win != True):
				self.loadboard()

				return winnerO
			self.loadboard()

	def makemoveX(self, var):
		#pass var to the array, var will be ex.1 1 a string
		s = list(str(var))
		s1 = int(s[0])
		s2 = int(s[1])
		
		self.arr[s1][s2] = 'X'
		
			
		
				
				

	
	def makemoveY(self, var):
		s = list(str(var))
		s1 = int(s[0])
		s2 = int(s[1])
		
		self.arr[s1][s2] = 'O'

	def win(self):
		#check array for right combination to win
		#if in straight line or diagnal
		bol = True
		arr = self.arr
		for x in range(0,3,1):
			#in x axis line 3 times
			if(arr[x][0] == arr[x][1] and arr[x][0] == arr[x][2] and arr[x][1] !=' '):
				bol=False
				return bol
			elif(arr[0][x] == arr[1][x] and arr[0][x] == arr[2][x] and arr[1][x] !=' '):
				bol=False
				return bol
			elif(arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2] and arr[1][1] !=' '):
				bol = False
				return bol
			elif(arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0] and arr[1][1] !=' '):
				bol = False
				return bol

		return bol


make = Main()
winner = make.play()
print("The winner is: ", winner)
