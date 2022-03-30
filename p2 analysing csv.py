import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     language_counter = Counter()
#
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))
#
#     # row = next(csv_reader)
#     # print(row['LanguagesWorkedWith'].split(';'))

data = pd.read_csv('data.csv')
print(data)
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

print(lang_responses)
language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# print(language_counter.most_common(15)

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)  # barh for horizontal bar chart

plt.title("Most popular languages")
# plt.ylabel("Programming languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

plt.show()
