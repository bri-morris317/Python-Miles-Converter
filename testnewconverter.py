#Create a program that can convert miles to kilometers

print("How many miles did you run today?")
miles = input()
kms = float(miles)*0.60371
kms = round(kms, 3)
print(f"Your run {miles} mi is equal to {kms} km")