
# Vstup od uživatele
vaha = float(input("Zadej svoji váhu (v kg): "))
vyska = float(input("Zadej svoji výšku (v metrech): "))

bmi = vaha / (vyska ** 2)

print(f"\nTvoje BMI je: {bmi:.2f}")

if bmi < 18.5:
    print("➡️ Podváha")
elif 18.5 <= bmi < 25:
    print("✅ Normální váha")
elif 25 <= bmi < 30:
    print("⚠️ Nadváha")
else:
    print("🚨 Obezita")
