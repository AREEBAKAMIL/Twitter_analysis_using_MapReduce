# Twitter_analysis_using_MapReduce
In this repository, I analyzed the real twitter dataset using MapReduce to extract:
1. number of tweets made per day
2. number of times each hashtag was used

# About the dataset
The dataset consists of a line in each row, where each line contains 4 fields as follows:
  0 epoch_time
  1 tweetId
  2 tweet(including #hashtags)
  3 device

# About the files
As the name suggests, the 'tweets_per_day.py' contains code for extracting the number of tweets made per day.
the 'no_of_hashtags_used.py' contains code for extracting the number of times each hashtag was used.

The results obtained from the .py file are in the following files:
- tweets_per_day.py -> tweets_per_day.txt
- no_of_hashtags_used.py -> hashtag_count.txt

# How to run
1. Ensure you have Python installed
2. Download the .py files
3. Navigate to the directory where the .py files are downloaded
4. To run the python file, type the command 'python python_file.py olympictweets2016rio.csv > output_file_name.txt'. Replace 'python_file' with the relevant python file you wish to run and 'output_file_name' with your chosen file name to output the results.
   
