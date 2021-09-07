import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
with open("input.txt", "r") as input:
    input = input.readlines()

format1_input = []
for element in input:
    format1_input.append(element.strip())

format2_input = ' '.join(format1_input)
format3_input = format2_input.replace('"', '')
format4_input = format3_input.replace("`", "")
format5_input = format4_input.replace("'", "")
format6_input = format5_input.replace(".", "")
format7_input = format6_input.replace("!", "")
format8_input = format7_input.replace("?", "")
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores(format8_input))
