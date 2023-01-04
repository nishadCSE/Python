n=int(input())
arr=map(int,input().split())    #map used for multiple input spilt to convert strings and int convert int value.For example, if the user inputs the string "1 2 3 4 5", the code will split it into a list of strings ['1', '2', '3', '4', '5'],apply the int() function to each element to convert it to an integer, and return a new iterator with the elements [1, 2, 3, 4, 5].
z=list(set(sorted(arr)))
print(z[-2])
