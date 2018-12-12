# News Insight from Trade War
![](https://github.com/leo2506/metis-work/blob/master/Project%204/caption.png)
## Overview
US and China trade war has caught eyes of general public since the beginning of 2018. As it heats up with tariffs increasingly imposed against each other, a variety of industries have been influenced immensely. Meanwhile, some countries have switched their attitudes towards US and China.  Once people wish to make an investment decision based on ongoing status of trade war, they will first look at recent news based on the opinions from domain experts. It is easy to gain provoking insights upon reading through articles. However, figuring out trends, patterns, and correlations of different aspects of the trade war are complicated and time-consuming. 

Machine learning and Nature Language Processing techniques can be very useful in mining insights from tons of news articles. Therefore, my goals of building a model could help investors to make wise decisions and assist governments to generate strategic diplomatic policies with efficiency.
## Notebook Description
* [Presentation](https://github.com/leo2506/metis-work/blob/master/Project%204/Slides/Trade%20War%20Insights%20from%20News.pdf)
* [Summary](https://liuriguang.wixsite.com/leo2506-1/blog/trade-war-insights-from-news)
* [Data_collection.ipynb](Data_collection.ipynb) - collects metadata of 6,000 articles by news API.
* [News_full_content_scarpping.ipynb](Data_cleaning.ipynb) - scraps full content of the 6,000 articles.
* [Preprocessing_Tokenization_Vectorization.ipynb](Preprocessing_Tokenization_Vectorization.ipynb) - cleans up metadata and full content, removes digits, punctuations, stopwords, high frequency terms, lowercases all words, and then fits into countervectorizer and tfidfvectorizer.
* [LDA_Topic_Modeling.ipynb](LDA_Topic_Modeling.ipynb) - builds a LDA topic model.
* [Sentiment_Analysis.ipynb](Sentiment_Analysis.ipynb) - analyzes sentiment over all topics and visualizes in heatmap.
* [Similarity_Analysis.ipynb](Similarity_Analysis.ipynb) - analyzes pairwise cosine similarity between documents and plots time plot of similarity scores.

## Tools
- Data collection: NewsAPI, BeautifulSoup, Selenium.
- Data cleaning and analysis: Pandas, Numpy, Sklearn, nltk, Textblob.
- Visualization: Tableau, matplotlib, seaborn.
