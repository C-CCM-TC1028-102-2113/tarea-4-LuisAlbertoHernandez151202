def main():
    #escribe tu código abajo de esta líne
    n=int(input("Dame los números a promediar que no sean negativos:"))
sum=0
num=0
for i in range(n):
 num=float(input("números:"))
sum=sum+num
promedio=sum/n
print("El promedio es:", promedio)

    pass
if __name__=='__main__':
    main()
