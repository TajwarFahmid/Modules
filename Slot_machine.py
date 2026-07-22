import random, math

def play():
    Q = input(
        "Do you want to play? Press 1 to play, press 0 to opt out of playing: "
    )

    while Q == "1":
        slot_choices = ["🍒", "🍇", "🍉", "7️⃣"]
        results = random.choices(slot_choices, k=3)

        output = " | ".join(results)
        print(output)

        if output == "7️⃣ | 7️⃣ | 7️⃣":
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")

        Q = input("\nPlay again? Press 1 to play, press 0 to exit: ")


play()

