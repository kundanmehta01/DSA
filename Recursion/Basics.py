def countdown(n):
    if n==0:
        return

    print("Before",n)
    countdown(n-1)
    print("After",n)
    

countdown(5)