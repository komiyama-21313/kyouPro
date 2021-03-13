Sx, Sy, Gx, Gy = list(map(int, input().split()))

x = Sx + (Gx-Sx)*(Sy/(Sy+Gy))

print(x)