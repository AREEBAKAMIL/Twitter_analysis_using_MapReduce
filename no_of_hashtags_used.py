"""Lab 3. Basic wordcount
"""
from mrjob.job import MRJob
import re
import time

#this is a regular expression that finds all the words inside a String
#WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class Lab1, that extends the MRJob format.
class Lab3(MRJob):

    # Fields contains line as follows.
    #  0            1        2                           3
    # epoch_time ; tweetId ; tweet(including #hashtags) ; device
    # in order to select the tweet, you would choose fields[2].

    def mapper(self, _, line):
        fields = line.split(";")
        try:
            if (len(fields)==4):
                message = fields[2]
                # count_hash = message.count('#')
                hash_set = {tag.strip("#") for tag in message.split() if tag.startswith("#")}
                for hashtag in hash_set:
                    yield(hashtag, 1)
        except:
            pass

    # option 1
    def reducer(self, hashtag, values): #no_of_hash, length_of_message
        yield (hashtag, sum(values))


if __name__ == '__main__':
    Lab3.run()
