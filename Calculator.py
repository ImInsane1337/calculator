import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def main():
    angles = [
        ##Сюда углы как по примеру ниже.
        10, 135, -60,
    ]

    print("Калькулятор перевода из градусной меры в радианную.")
    
    for degree in angles:
        radians = degrees_to_radians(degree)
        print(f"{degree} градусов = {radians:.6f} радиан")

if __name__ == "__main__":
    main()
