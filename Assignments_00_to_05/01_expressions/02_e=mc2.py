c =  299792458
def main():
    mass = int(input("Enter the mass in kilogram : "))
    energy = mass  * (c ** 2)
    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(c) + " m/s")
    
    print(str(energy) + " joules of energy!")

if __name__ == '__main__':
    main()
