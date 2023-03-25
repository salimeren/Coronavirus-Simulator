
p=0
b=0

import math
import random
from evaluator import *    # get_data() will come from this import
universalstate = get_data()[6:][0]
şuankidata = []
bulaşanlar= []
def new_move():
	global universalstate,şuankidata,p,b
	şuankidata.extend(universalstate)
	M = get_data()[0]
	N = get_data()[1]
	D = get_data()[2]
	K = get_data()[3]
	LAMBDA = get_data()[4]
	mu = get_data()[5]
	p = 0  
	b = 0  

	def bulaştırıcı(a):
		global bulaşanlar
		global universalstate
		global b
		global şuankidata

		x = a[0][0][0]
		y = a[0][0][1]
		for i in range(len(a)):
			if i + 1 == len(a):
				break
			t = a[i + 1][0][0]
			u = a[i + 1][0][1]
			distance = math.sqrt(((x - t) ** 2) + ((y - u) ** 2))

			if a[0][2] == "notmasked" and a[i + 1][2] == "notmasked":
				lambdasabiti = 1
			if a[0][2] == "masked" and a[i + 1][2] == "notmasked":
				lambdasabiti = LAMBDA
			if a[0][2] == "notmasked" and a[i + 1][2] == "masked":
				lambdasabiti = LAMBDA
			if a[0][2] == "masked" and a[i + 1][2] == "masked":
				lambdasabiti = LAMBDA ** 2

			if distance <= D and a[0][3] == "infected" and a[i + 1][3] == "notinfected":
				bulaşmaihtimali = random.choices(["infected", "notinfected"],weights=[min(1, K / distance ** 2) / lambdasabiti,1 -( min(1, K / distance ** 2) / lambdasabiti)], k=1)

				if bulaşmaihtimali == ["infected"]:
					bulaşanlar.extend([b,i+1+b])

			if distance <= D and a[0][3] == "notinfected" and a[i + 1][3] == "infected":
				bulaşmaihtimali = random.choices(["infected", "notinfected"],weights=[min(1, K / distance ** 2) / lambdasabiti,1 -(min(1, K / distance ** 2) / lambdasabiti)], k=1)

				if bulaşmaihtimali == ["infected"]:
					bulaşanlar.extend([ i + 1 + b,b])

		b = b + 1
		if len(a[1:]) == 0:
			universalstate =[]

			universalstate.extend(şuankidata)
			for i in range(len(bulaşanlar)):
				universalstate[bulaşanlar[i]][3] = "infected"

			şuankidata=[]
			p=0
			b=0
			bulaşanlar=[]
			return universalstate
		else:
			return bulaştırıcı(a[1:])
	def ilerletici(a):
		global universalstate,koordinattutucu
		global şuankidata
		öncekidata=[]
		öncekidata.extend(şuankidata[:])
		lastmove=[]
		global p
		if len(a) == 0:
			return []
		x = a[0][0][0]
		y = a[0][0][1]
		if p < len(şuankidata):
			prob = random.choices(["f", "rf", "r", "rb", "b", "lb", "l", "lf"], weights=[mu / 2, mu / 8, (1 - mu - mu ** 2) / 2, (mu ** 2) * (2 / 5), (mu ** 2) / 5,(mu ** 2) * (2 / 5), (1 - mu - mu ** 2) / 2, mu / 8, ], k=1)[0]
		if p < len(şuankidata):
			if a[0][1] == 0:
				if prob == "b":
					y = y - 1
					lastmove = 4
				if prob == "rb":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "lb":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "r":
					x = x - 1
					lastmove = 2
				if prob == "l":
					x = x + 1
					lastmove = 6
				if prob == "rf":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "lf":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "f":
					y = y + 1
					lastmove = 0
				error=[]
				if x == N or x < 0 or y == M or y < 0:
					error="var"
				for k in range(p):
					if (x,y)==şuankidata[k][0]:
						error="var"
				for i in range(len(a)-1):
					if (x,y)==a[i+1][0]:
						error="var"
				if not error=="var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 1:
				if prob == "b":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "rb":
					y = y - 1
					lastmove = 4
				if prob == "lb":
					x = x + 1
					lastmove = 6
				if prob == "r":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "l":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "rf":
					x = x - 1
					lastmove = 2
				if prob == "lf":
					y = y + 1
					lastmove = 0
				if prob == "f":
					x = x - 1
					y = y + 1
					lastmove = 1
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 2:
				if prob == "b":
					x = x + 1
					lastmove = 6
				if prob == "rb":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "lb":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "r":
					y = y - 1
					lastmove = 4
				if prob == "l":
					y = y + 1
					lastmove = 0
				if prob == "rf":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "lf":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "f":
					x = x - 1
					lastmove = 2
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 3:
				if prob == "b":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "rb":
					x = x + 1
					lastmove = 6
				if prob == "lb":
					y = y + 1
					lastmove = 0
				if prob == "r":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "l":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "rf":
					y = y - 1
					lastmove = 4
				if prob == "lf":
					x = x - 1
					lastmove = 2
				if prob == "f":
					x = x - 1
					y = y - 1
					lastmove = 3
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 4:
				if prob == "b":
					y = y + 1
					lastmove = 0
				if prob == "rb":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "lb":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "r":
					x = x + 1
					lastmove = 6
				if prob == "l":
					x = x - 1
					lastmove = 2
				if prob == "rf":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "lf":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "f":
					y = y - 1
					lastmove = 4
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 5:
				if prob == "b":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "rb":
					y = y + 1
					lastmove = 0
				if prob == "lb":
					x = x - 1
					lastmove = 2
				if prob == "r":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "l":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "rf":
					x = x + 1
					lastmove = 6
				if prob == "lf":
					y = y - 1
					lastmove = 4
				if prob == "f":
					x = x + 1
					y = y - 1
					lastmove = 5
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 6:
				if prob == "b":
					x = x - 1
					lastmove = 2
				if prob == "rb":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "lb":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "r":
					y = y + 1
					lastmove = 0
				if prob == "l":
					y = y - 1
					lastmove = 4
				if prob == "rf":
					x = x + 1
					y = y + 1
					lastmove = 7
				if prob == "lf":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "f":
					x = x + 1
					lastmove = 6
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])
		if p < len(şuankidata):
			if a[0][1] == 7:
				if prob == "b":
					x = x - 1
					y = y - 1
					lastmove = 3
				if prob == "rb":
					x = x - 1
					lastmove = 2
				if prob == "lb":
					y = y - 1
					lastmove = 4
				if prob == "r":
					x = x - 1
					y = y + 1
					lastmove = 1
				if prob == "l":
					x = x + 1
					y = y - 1
					lastmove = 5
				if prob == "rf":
					y = y + 1
					lastmove = 0
				if prob == "lf":
					x = x + 1
					lastmove = 6
				if prob == "f":
					x = x + 1
					y = y + 1
					lastmove = 7
				error = []
				if x == N or x < 0 or y == M or y < 0:
					error = "var"
				for k in range(p):
					if (x, y) == şuankidata[k][0]:
						error = "var"
				for i in range(len(a) - 1):
					if (x, y) == a[i + 1][0]:
						error = "var"
				if not error == "var":
					şuankidata[p][0] = (x, y)
					şuankidata[p][1] = lastmove
				p = p + 1
				if p == len(şuankidata):
					return []
				ilerletici(a[1:])

		if len(a) == len(şuankidata):

			p=0
			return bulaştırıcı(universalstate)

	return ilerletici(universalstate)
























