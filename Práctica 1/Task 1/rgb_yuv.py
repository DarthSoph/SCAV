# We ask for 3 integer numbers in the command screen and we check they are between 0 and 255 to give values to R, G & B
R = -1
while R < 0 or R > 255:
    R = int(input("Introduce a value for R (between 0 and 255): "))

G = -1
while G < 0 or G > 255:
    G = int(input("Introduce a value for G (between 0 and 255): "))

B = -1
while B < 0 or B > 255:
    B = int(input("Introduce a value for B (between 0 and 255): "))

# Conversion from RGB to YUV
Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
U = -0.148 * R - 0.291 * G + 0.439 * B + 128
V = 0.439 * R - 0.368 * G - 0.071 * B + 128

# We print the values Y, U and V previously computed
print("The Y value is", Y)
print("The U value is", U)
print("The V value is", V)

# We ask the user if they want to go back to the RGB values computed from the YUV values
ans = "R"
while ans != "Y" and ans != "N":
    ans = input("¿Do you want to convert the previous values to RGB again? (Y/N): ")

# If the answer is yes, we do the corresponding computations to obtain the values R, G and B
if ans == "Y":
    r = 1.164 * (Y - 16) + 1.596 * (V - 128)
    g = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128)
    b = 1.164 * (Y - 16) + 2.018 * (U - 128)
    print("The R value is", r)
    print("The G value is", g)
    print("The B  value is", b)

# If the answer is no, we say goodbye to the user
else:
    print("See you soon!")
