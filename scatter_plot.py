import sys;
import csv;
import math;
import numpy as np
import matplotlib.pyplot as plt;

with open('resources/dataset_train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

    transfiguration = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    arithmancy = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    divination = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    astronomy = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    herbology = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    dark_arts = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    creatures = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    history = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    potions = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    muggle = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    charms = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    flying = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}
    runes = {'Gryffindor':[], 'Ravenclaw':[], 'Hufflepuff':[], 'Slytherin':[]}

    for row in rows:
        if row['Transfiguration'] and row['Arithmancy'] and row['Divination'] and row['Astronomy'] and row['Herbology'] and row['Defense Against the Dark Arts'] and row['Charms'] and row['Care of Magical Creatures'] and row['History of Magic'] and row['Potions'] and row['Muggle Studies'] and row['Flying'] and row['Ancient Runes']:
            transfiguration[row['Hogwarts House']].append(round(float(row['Transfiguration'])))
            arithmancy[row['Hogwarts House']].append(round(float(row['Arithmancy'])))
            divination[row['Hogwarts House']].append(round(float(row['Divination']), 2))
            astronomy[row['Hogwarts House']].append(round(float(row['Astronomy'])))
            herbology[row['Hogwarts House']].append(round(float(row['Herbology']), 2))
            dark_arts[row['Hogwarts House']].append(round(float(row['Defense Against the Dark Arts']), 2))
            charms[row['Hogwarts House']].append(round(float(row['Charms'])))
            creatures[row['Hogwarts House']].append(round(float(row['Care of Magical Creatures']), 2))
            history[row['Hogwarts House']].append(round(float(row['History of Magic']), 2))
            potions[row['Hogwarts House']].append(round(float(row['Potions']), 2))
            muggle[row['Hogwarts House']].append(round(float(row['Muggle Studies'])))
            flying[row['Hogwarts House']].append(round(float(row['Flying'])))
            runes[row['Hogwarts House']].append(round(float(row['Ancient Runes'])))

courses = [arithmancy, astronomy, herbology, dark_arts, divination, muggle, runes, history, transfiguration, potions, creatures, charms, flying]
courses_names = ["Arithmancy", "Astronomy", "Herbology", "Dark arts", "Divination", "muggle", "runes", "history", "transfiguration", "potions", "creatures", "charms", "flying"]

plt.scatter(astronomy['Gryffindor'], dark_arts['Gryffindor'], label='Gryffindor', color="red")
plt.scatter(astronomy['Slytherin'], dark_arts['Slytherin'], label='Slytherin', color="green")
plt.scatter(astronomy['Hufflepuff'], dark_arts['Hufflepuff'], label='Hufflepuff', color="yellow")
plt.scatter(astronomy['Ravenclaw'], dark_arts['Ravenclaw'], label='Ravenclaw', color="blue")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()