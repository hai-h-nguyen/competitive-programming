

def checkStop(numInt):
	while (numInt % 2 == 0):
		numInt /= 2

	if (numInt == 1):
		return 'TAK'
	else:
		return 'NIE'

def main():

	while(True):
		(num_Attacker, num_Defender) = input().split(' ')

		num_Attacker = int(num_Attacker)
		num_Defender = int(num_Defender)

		if (num_Defender == 0) and (num_Attacker == 0):
			break

		attacker_Distance = input().split(' ')
		defender_Distance = input().split(' ')

		attacker_min = min(attacker_Distance)

		count = 0

		for defender_dist in defender_Distance:
			if (int(attacker_min) >= int(defender_dist)):
				count += 1

		if (count >= 2):
			print('N')
		else:
			print('Y')

if __name__ == "__main__":
    main()