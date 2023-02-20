
# def printSpaces(num_of_spaces):
# 	print(" " * num_of_spaces, end = "")
#
# def printUP(diamond_base):
# 	for row in range(5, 0, -1):
# 		printSpaces(diamond_base-row)
# 		for i in range(1, row+1):
# 			print(i, end = " ")
# 		print()
#
# # def printDown(diamond_base):
# #     for row in range(2, 6):
# #         printSpaces(diamond_base-row)
# #         for i in range(row, 0, -1):
# # 			print(i, end = " ")
# # 			print()
#
# printUP(5)
# # printDown(5)

for i in range(5, 0, -1):
	for k in range(6-i, 0, -1):
		print(" ", end="")
	for j in range(1, i+1):
		print(j, end=" ")
	print()

for i in range(2, 6):
	for k in range(6-i, 0, -1):
		print(" ", end="")
	for j in range(i, 0, -1):
		print(j, end=" ")
	print()
