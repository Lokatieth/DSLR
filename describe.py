import sys;
import csv;
import math;
import numpy as np
import matplotlib.pyplot as plt;
from datetime import datetime;

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print ("You need to specify the csv file !")
    exit()


def calculate_standard_deviation(course, mean, count):
    squared_sum = sum([(x - mean) * (x - mean) for x in course])
    return (math.sqrt(squared_sum / count))

with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

    transfiguration = []
    arithmancy = []
    divination = []
    astronomy = []
    herbology = []
    dark_arts = []
    creatures = []
    history = []
    potions = []
    muggle = []
    charms = []
    flying = []
    runes = []

    for row in rows:
        dark_arts.append(row['Defense Against the Dark Arts'])
        creatures.append(row['Care of Magical Creatures'])
        transfiguration.append(row['Transfiguration'])
        history.append(row['History of Magic'])
        divination.append(row['Divination'])
        muggle.append(row['Muggle Studies'])
        arithmancy.append(row['Arithmancy'])
        astronomy.append(row['Astronomy'])
        herbology.append(row['Herbology'])
        runes.append(row['Ancient Runes'])
        potions.append(row['Potions'])
        charms.append(row['Charms'])
        flying.append(row['Flying'])
        
    courses = [arithmancy,
        astronomy, herbology, dark_arts, divination, muggle, runes, history, transfiguration, potions, creatures, charms, flying]

    counts = ['Count  |']
    means = ['Mean  |']
    stds = ['Std  |']
    mins = ['Min  |']
    perc_25 = ['25%  |']
    perc_50 = ['50%  |']
    perc_75 = ['75%  |']
    maxs = ['Max  |']
    for course in courses:
        course = [float(x) for x in course if x]
        course.sort()
        grade_count = 0.0
        grade_sum = 0.0
        for grade in course:
            if grade:
                grade_count += 1
                grade_sum += grade
        counts.append(str(grade_count))
        grade_mean = grade_sum / grade_count
        means.append(str(grade_sum / grade_count))
        stds.append(str(calculate_standard_deviation(course, grade_mean, grade_count)))
        mins.append(str(course[0]))
        perc_25.append(str(course[int(0.25 * grade_count)]))
        perc_50.append(str(course[int(0.5 * grade_count)]))
        perc_75.append(str(course[int(0.75 * grade_count)]))
        maxs.append(str(course[int(grade_count - 1)]))

    firstline = ['', 'Arithmancy', 'Astronomy', 'Herbology', 'Dark Arts', 'Divination', 'Muggle St.', 'Runes', 'History', 'Transfig.', 'Potions', 'Creatures', 'Charms', 'Flying']
    print(' '.join('{:>16.10}'.format(headline) for headline in firstline))
    print("\t\t------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(' '.join('{:>16.10}'.format(number) for number in counts))
    print(' '.join('{:>16.10}'.format(number) for number in means))
    print(' '.join('{:>16.10}'.format(number) for number in stds))
    print(' '.join('{:>16.10}'.format(number) for number in mins))
    print(' '.join('{:>16.10}'.format(number) for number in perc_25))
    print(' '.join('{:>16.10}'.format(number) for number in perc_50))
    print(' '.join('{:>16.10}'.format(number) for number in perc_75))
    print(' '.join('{:>16.10}'.format(number) for number in maxs))
        


    plt.locator_params(axis='y', nbins=6)
    # plt.scatter(Age, Arithmancy)
    # plt.xlabel("Age")
    # plt.ylabel("Arithmancy")
    # plt.show()


