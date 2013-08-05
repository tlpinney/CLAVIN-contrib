# JIFX Experiment 2013-Aug-05



## Data Pre-Prep 

Get access to twitter data

Conversion to TSV 

Get python script at https://gist.github.com/brendano/22764

    python xlsx2tsv.py JIFX_tweets.xlsx > JIFX_tweets.tsv
   
Other option is to use LibreOffice and export as CSV using tab as a delimeter


## R-Studio 

Install ggplot2 package 

Load data 

    tweets <- read.delim("~/Downloads/JIFX_tweets.tsv")

Fix up misspelled column

    names(tweets)[names(tweets)=="Langauge"] <- "Language"


Create bar chart of language counts 

    ggplot(data=tweets, aes(x=Language)) + geom_bar(stat="bin") + ggtitle("JIFX - Twitter Language Counts")











