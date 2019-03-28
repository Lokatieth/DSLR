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
        if row['Transfiguration']:
            transfiguration[row['Hogwarts House']].append(round(float(row['Transfiguration'])))
        if row['Arithmancy']:
            arithmancy[row['Hogwarts House']].append(round(float(row['Arithmancy'])))
        if row['Divination']:
            divination[row['Hogwarts House']].append(round(float(row['Divination']), 2))
        if row['Astronomy']:
            astronomy[row['Hogwarts House']].append(round(float(row['Astronomy'])))
        if row['Herbology']:
            herbology[row['Hogwarts House']].append(round(float(row['Herbology']), 2))
        if row['Defense Against the Dark Arts']:
           dark_arts[row['Hogwarts House']].append(round(float(row['Defense Against the Dark Arts']), 2))
        if row['Charms']:
            charms[row['Hogwarts House']].append(round(float(row['Charms'])))
        if row['Care of Magical Creatures']:
            creatures[row['Hogwarts House']].append(round(float(row['Care of Magical Creatures']), 2))
        if row['History of Magic']:
            history[row['Hogwarts House']].append(round(float(row['History of Magic']), 2))
        if row['Potions']:
            potions[row['Hogwarts House']].append(round(float(row['Potions']), 2))
        if row['Muggle Studies']:
            muggle[row['Hogwarts House']].append(round(float(row['Muggle Studies'])))
        if row['Flying']:
            flying[row['Hogwarts House']].append(round(float(row['Flying'])))
        if row['Ancient Runes']:
            runes[row['Hogwarts House']].append(round(float(row['Ancient Runes'])))
    # print (runes)

plt.subplot(441)
plt.suptitle('Grade repartition from house to house.')
plt.hist(arithmancy['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(arithmancy['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(arithmancy['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(arithmancy['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Arithmancy')

plt.subplot(442)
plt.hist(astronomy['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(astronomy['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(astronomy['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(astronomy['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Astronomy')

plt.subplot(443)
plt.hist(herbology['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(herbology['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(herbology['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(herbology['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Herbology')

plt.subplot(444)
plt.hist(dark_arts['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(dark_arts['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(dark_arts['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(dark_arts['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Defense Against the Dark Arts')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.subplot(445)
plt.hist(divination['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(divination['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(divination['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(divination['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Divination')

plt.subplot(446)
plt.hist(muggle['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(muggle['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(muggle['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(muggle['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Muggle Studies')

plt.subplot(447)
plt.hist(runes['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(runes['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(runes['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(runes['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Ancient Runes')

plt.subplot(448)
plt.hist(history['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(history['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(history['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(history['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('History of Magic')

plt.subplot(449)
plt.hist(transfiguration['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(transfiguration['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(transfiguration['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(transfiguration['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Transfiguration')

plt.subplot(4, 4, 10)
plt.hist(potions['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(potions['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(potions['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(potions['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Potions')

plt.subplot(4, 4,11)
plt.hist(creatures['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(creatures['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(creatures['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(creatures['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Care of Magical Creatures')

plt.subplot(4, 4, 12)
plt.hist(charms['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(charms['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(charms['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(charms['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Charms')

plt.subplot(4, 4, 13)
plt.hist(flying['Gryffindor'], bins = 25 , alpha=0.6, label='Gryffindor', color="red")
plt.hist(flying['Slytherin'], bins = 25 , alpha=0.6, label='Slytherin', color="green")
plt.hist(flying['Hufflepuff'], bins = 25 , alpha=0.6, label='Hufflepuff', color="yellow")
plt.hist(flying['Ravenclaw'], bins = 25 , alpha=0.6, label='Ravenclaw', color="blue")
plt.title('Flying')

plt.show()
