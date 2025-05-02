slovo = input("daj slovo:")
for i in range(0, len(slovo)):
    if slovo[i] != slovo[-(i + 1)]:
        print("Nie je palindróm")
        break
else:
    print("Palindróm")
