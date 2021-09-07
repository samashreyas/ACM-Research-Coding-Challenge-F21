# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Question One Solution Explanation:

This score, determined by a implementation of the NLTK Library in Python called VADER, is broken down into multiple parts. VADER is a model used for a pretrained text sentiment analysis that takes a chain of words and finds the polarity and magnitude of the emotion conveyed by each of the words. The first three scores sum to one and they represent approximately the proportion of the text that is 'neg'(negative), 'neu'(neutral), and 'pos'(positive). The fourth score 'compound' is a compounded score that is between -1 and 1 that roughly approximates the overall sentiment of the body of text as a whole. This compounded score counts as the sentiment score that is being sought after. I chose to use VADER because it is capable of recognizing some negatives and inversions in grammar and takes them into account when calculating sentiment score. VADER has already been trained through large datasets and gives Sentiment ratings to different words and gives neutral ratings to words like nouns that don't have sentiments and words it has not encountered before. I expected the score to be relatively high for that body of text given in the input text file as it is a person describing their friend who is very respected and appreciated in the community and though he has his flaw of being unemployed, he is a very great member of society. The first paragraph described a humorous interaction between the narrator and the friend, and the second paragraph goes into how great and well reputable said friend is and his experiences and strengths. The output sentiment score for that body of text is 0.9979 which is actually quite close to what I was expecting it to be, which was around 0.9-0.95. The reason why it is so high even though only 18.8% of the text was found to be of positive polarity is because of the deep connection and meaningful descriptions the narrator puts up. Compared to the blabber and thoughtless statements most people type on a day to day basis in social media, the narrators words convey deep connection to the friend described and shows how much the narrators knows about said friend. I am sadly not exactly good enough to pull off a self-trained sentiment analysis algorithm in the timeframe given so I had to use a pretrained one and one of the main reasons I used VADER compared to other ones was because of its ability to recognize minor details and the large datasets it was already trained with. Though it was intended to be used in rather small tokens of information, it works rather well with this certain data set, coincidently, because it is not exactly large enough to start running into some of the more major problems plus the fact that the body of text had a lot of vivid and colorful words that the sentiment analysis algorithm loved to gobble up.
