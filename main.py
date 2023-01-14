import matplotlib.pyplot as plt

def read_data(file_path):
  temps = []
  with open(file_path) as file:
    for line in file:
      temps.append(float(line.strip()))
  return temps

def run():
  data = read_data('visual/subplots/temps.txt')
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  plt.show()

run()

import matplotlib.pyplot as plt
import csv

def read_data():
  with open('visual/subplots/temps.csv') as file:
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)
    data = {'week1':[], 'week2':[]}

    for line in csv_reader:
      data['week1'].append(float(line[0].strip()))
      data['week2'].append(float(line[1].strip()))
  
  return data

def run():
  data = read_data()
  
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data['week1'])), data['week1'])
  ax2.plot(range(len(data['week2'])), data['week2'])
  plt.show()

run()

import matplotlib.pyplot as plt
import csv

def read_data():
  with open('visual/subplots/temps.csv') as file:
    csv_reader = csv.reader(file)

    # extract headers
    line = next(csv_reader)
    weeks = [week.strip() for week in line]

    # extract temperature data
    data = {weeks[0]:[], weeks[1]:[]}

    for line in csv_reader:
      data[weeks[0]].append(float(line[0].strip()))
      data[weeks[1]].append(float(line[1].strip()))
  
  return data

def run():
  data = read_data()
  weeks = list(data.keys())
  
  fig, axs = plt.subplots(2, 1)
  
  ax_index = 0
  for week in weeks:
    axs[ax_index].plot(range(len(data[week])), data[week])
    ax_index += 1

  plt.tight_layout()
  plt.show()

run()

