# ACM Research Coding Challenge (Fall 2021)
## What I used
This score, determined by a implementation of the NLTK Library in Python called VADER, is broken down into multiple parts. VADER is a model used for a pre-trained text sentiment analysis that takes a chain of words and finds the polarity and magnitude of the emotion conveyed by each of the words. The first three scores sum to one and they represent approximately the proportion of the text that is 'neg'(negative), 'neu'(neutral), and 'pos'(positive). The fourth score 'compound' is a compounded score that is between -1 and 1 that roughly approximates the overall sentiment of the body of text as a whole. This compounded score counts as the sentiment score that is being sought after. 
## Why I chose this
I chose to use VADER because it is capable of recognizing some negatives and inversions in grammar and takes them into account when calculating sentiment score. VADER has already been trained through large datasets and gives Sentiment ratings to different words and gives neutral ratings to words like nouns that don't have sentiments and words it has not encountered before. 
## Contrasting expectations and Results
I expected the score to be relatively high for that body of text given in the input text file as it is a person describing their friend who is very respected and appreciated in the community and though he has his flaw of being unemployed, he is a very great member of society. The first paragraph described a humorous interaction between the narrator and the friend, and the second paragraph goes into how great and well reputable said friend is and his experiences and strengths. The output sentiment score for that body of text is 0.9979 which is actually quite close to what I was expecting it to be, which was around 0.9-0.95. The reason why it is so high even though only 18.8% of the text was found to be of positive polarity is because of the deep connection and meaningful descriptions the narrator puts up. Compared to the blabber and thoughtless statements most people type on a day to day basis in social media, the narrator's words convey deep connection to the friend described and shows how much the narrator knows about said friend. 
## Limitations and Concerns
I sadly do not know enough to pull off a self-trained sentiment analysis algorithm in the timeframe given so I had to use a pre-trained one and one of the main reasons I used VADER compared to other ones was because of its ability to recognize minor details and the large datasets it was already trained with. Though it was intended to be used in rather small tokens of information, it works rather well with this certain data set, coincidently, because it is not exactly large enough to start running into some of the more major problems plus the fact that the body of text had a lot of vivid and colorful words that the sentiment analysis algorithm loves to gobble up. The compound score is found by finding the sum of the valence scores already assigned in the VADER lexicon, which are each between -4 and 4, and then normalizing it using an equation in the form x/sqrt(x^2+a). When x reaches really high or really low values, this score approaches 1 or -1 respectively. But it behaves in a less stable manner for lower values of x. This wouldn't exactly work well for extremely large sets of data as the sum of the valence scores would reach such a large magnitude that even if the overall sentiment of the text is fairly neutral, the a wouldn't be able to handle the immense value for x and would show a value that approaches -1 or 1 depending on the skew of the data set. This wouldn't really apply to this specific data set as it isn't exactly that massive plus it was already incredibly skewed to one side to begin with.
## What I would have changed
An interesting addition to the program I would have added if I had more experience in Python is removing quotes within quotes. For example if someone is citing or quoting another person within their speech then the quote they are citing doesn’t technically contribute to the sentiment at all and only their reaction or reflection on the matter will contribute towards the sentiment of the overall text in most cases. This is shown as though the overall text has a very high sentiment compound value, there is about 7.6% of it that has a negative sentiment because they are quoting other people in their humorous encounter and the quotes that were referenced had a rather negative sentiment though the conversation itself was a very positive sentiment oriented one. 
