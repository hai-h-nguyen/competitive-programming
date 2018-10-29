"""Input
 Julka surprised her teacher at preschool by solving the following riddle:
Klaudia and Natalia have 10 apples together, but Klaudia has two apples more than Natalia. How many apples does each of he girls have
Julka said without thinking: Klaudia has 6 apples and Natalia 4 apples. The teacher tried to check if Julka's answer wasn't accidental 
and repeated the riddle every time increasing the numbers. Every time Julka answered correctly. The surprised teacher wanted to continue 
questioning Julka, but with big numbers she could't solve the riddle fast enough herself. Help the teacher and write a program which will give her the right answers. 
"""
def main():
	for test in range(0, 10):	
		Sum =int(input())
		More = int(input())
		print((Sum + More) // 2)
		print((Sum - More) // 2)

if __name__ == "__main__":
    main()