#!/usr/bin/python3
#author=arif_fadillah
A = int(input("Masukan jumah baris: "))
B = 1
for x in range(A):
    for y in range(B):
        print("*", end = " ")
    print("")
    B += 1
