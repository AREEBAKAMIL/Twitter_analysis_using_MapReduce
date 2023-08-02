"""Lab 3. Basic wordcount
"""
from mrjob.job import MRJob
import re
import time

#Get number of tweets per day
class Lab3(MRJob):


    def mapper(self, _, line):
        fields = line.split(";")
        try:
            if (len(fields)==4):
                time_epoch = int(fields[0])/1000
                date = time.strftime("%d/%m/%y",time.gmtime(time_epoch)) #returns date of the month
                yield(date, 1)
            else:
                yield("malformed_lines", 1)

        except:
            pass

    def reducer(self, date, counts):
        yield(date, sum(counts))


if __name__ == '__main__':
    Lab3.run()
