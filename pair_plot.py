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
courses_names = ["arithmancy", "astronomy", "herbology", "dark_arts", "divination", "muggle", "runes", "history", "transfiguration", "potions", "creatures", "charms", "flying"]

plt.tick_params(axis = 'x', length = 0)
plt.tick_params(axis = 'y', length = 0)
plt.subplots_adjust(left=0.05, right=1, top=1, bottom=0.05)
for index, course in enumerate(courses):
    for i in range(13):
        plt.subplot(13, 13, index * 13 + i + 1)
        plt.xticks([])
        plt.yticks([])
        if i == index:
            plt.hist(course['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
            plt.hist(course['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
            plt.hist(course['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
            plt.hist(course['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
        else:
            plt.scatter(course['Gryffindor'], courses[i]['Gryffindor'], label='Gryffindor', color="red", s=2, alpha = 0.7)
            plt.scatter(course['Slytherin'], courses[i]['Slytherin'], label='Slytherin', color="green", s=2, alpha = 0.7)
            plt.scatter(course['Hufflepuff'], courses[i]['Hufflepuff'], label='Hufflepuff', color="yellow", s=2, alpha = 0.7)
            plt.scatter(course['Ravenclaw'], courses[i]['Ravenclaw'], label='Ravenclaw', color="blue", s=2, alpha = 0.7)
        # if index == 12:
        plt.xlabel(courses_names[index], fontsize = 'x-small')
        plt.ylabel(courses_names[i], fontsize = 'x-small')


plt.show()