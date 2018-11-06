def main():

	while(True):
		(num_Attacker, num_Defender) = input().split(' ')

		if (num_Defender == '0') and (num_Attacker == '0'):
			break

		attacker_Distance = list(map(int, input().split(' ')))
		defender_Distance = list(map(int, input().split(' ')))

		attacker_min = min(attacker_Distance)

		count = 0

		for defender_dist in defender_Distance:
			if (attacker_min >= defender_dist):
				count += 1

		if (count >= 2):
			print('N')
		else:
			print('Y')

if __name__ == "__main__":
    main()