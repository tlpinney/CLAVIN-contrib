# JIFX Experiment 2013-Aug-05



## Data Pre-Prep 

Get access to twitter data

Conversion to TSV 
   
Use LibreOffice and export as CSV using tab as a delimeter, and no formatting for text.

Generate unique ids for datasets

    python make_geo_ids.py > GeocodedTweets_id.tsv
	python make_tweet_ids.py > JIFX_tweets_id.tsv

Create a combined dataset

	make_combined.py
	

## Analysis

Install R-Studio
Install ggplot2 package 

Load data 

    tweets <- read.delim("JIFX_tweets_id.tsv")


Create bar chart of language counts 

    ggplot(data=tweets, aes(x=Language)) + geom_bar(stat="bin") + ggtitle("JIFX - Twitter Language Counts")


Generated Plot 

https://raw.github.com/Berico-Technologies/CLAVIN-contrib/master/jifx/jifx_twitter_language_counts.png













