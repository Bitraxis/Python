#vypocet znamky z poctu bodov
#dolna hranica 1 - 90%, 2 - 75%, 3 - 50%, 4 - 30%
maximum = int(input("Maximálny počet bodov: "))
ziaci = int(input("Koľko žiakov: "))
while ziaci > 0 :
    ziaci -= 1
    bodyZiaka = int(input("Body žiaka: "))
    if maximum * 0.9 <= bodyZiaka :
        print("Má za jedna")
    elif maximum * 0.75 <= bodyZiaka :
        print("Má za dva")
    elif maximum * 0.5 <= bodyZiaka :
        print("Má za tri")
    elif maximum * 0.3 <= bodyZiaka :
        print("Má za štyri")
    else :
        print("Má za päť")
print("Už nie sú žiaci")
