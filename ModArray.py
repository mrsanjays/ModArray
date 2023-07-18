def ModArray(A,B):
    num=0
    unitdigit=1
    for i in range(len(A)-1,-1,-1):
        num+=((A[i]*unitdigit)%B)
        unitdigit=(unitdigit*10)%B
    return num%B

if __name__ == '__main__':
    A=list(map(int,input().split()))
    B=int(input())
    print(ModArray(A,B))
"""
Mod Array
You are given a large number in the form of a array A of size N where each element denotes a digit of the number.
You are also given a number B. You have to find out the value of A % B and return it.

Example Input

Input 1:
A = [1, 4, 3] B = 2
Input 2:

A = [4, 3, 5, 3, 5, 3, 2, 1] B = 47


Example Output

Output 1:
1
Output 2:

20
"""
