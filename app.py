import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

CAL_GOAL = 2600 #kcal
PROTEIN_GOAL = 140 #grams 
FAT_GOAL = 80 #grams
CARBS_GOAL = 300 #grams

today= []
@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False
while not done:
    print("""
    (1) Add new item
    (2) Visualize progress
    (q) Quit
     """)
    choice=input("Choose an option: ")
    if choice== "1":
        print("Adding new item...")
        name= input("Name: ")
        calories= int(input("Calories: "))
        protein= int(input("Protein: "))
        fat= int(input("Fat: "))
        carbs= int(input("Carbs: "))
        food = Food(name,calories,protein,fat,carbs)
        today.append(food)
        print("The item was successfully added!!")
    elif choice=="2":
        calories_sum = sum(food.calories for food in today)
        proteins_sum = sum(food.protein for food in today)
        fats_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)


        fig , axis = plt.subplots(2,2) 
        axis[0, 0].pie([proteins_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%", explode=(0, 0, 0))

        axis[0,0].set_title("Macro Nutrients Distribution")
        axis[0,1].bar([0,1,2],[proteins_sum,fats_sum,carbs_sum], width=0.4)
        axis[0,1].bar([0.5,1.5,2.5],[PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
        axis[0,0].set_title("Macro Nutrients Progress")
        axis[1,0].pie([calories_sum, CAL_GOAL - calories_sum], labels=["Calories","Remaining"], autopct= "%1.1f%%")
        axis[1,0].set_title("Calorie Goal Progress")
        axis[1,1].plot(list(range(len(today))), np.cumsum ([food.calories for food in today]),label="Calories Eaten")
        axis[1,1].plot(list(range(len(today))), [CAL_GOAL]*len(today), label="Calorie Goal")
        axis[1,1].legend()
        axis[1,1].set_title("Calories Goal Over time")
        fig.tight_layout()
        plt.show()
    elif choice=="q":
        done=True
    else:
        print("Invalid Choice")

