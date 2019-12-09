# useful to have this code snippet to avoid getting an error in case forgeting 
# to close spark

try:
    spark.stop()
except:
    pass

# Using findspark to find automatically the spark folder
#!pip install --user findspark
import findspark
findspark.init()

# import python libraries

# initialize
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StringType
from pyspark.sql.types import DoubleType
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
from pyspark.sql import Row

# from pyspark.ml.feature import HashingTF, IDF, RegexTokenizer, StringIndexer, NGram
# from pyspark.ml.classification import LogisticRegression
# from pyspark.ml import Pipeline
# from pyspark.mllib.evaluation import MulticlassMetrics

spark = SparkSession.builder.master("local[*]").getOrCreate()
# num_samples = 100000000

# def inside(p):
#     x, y = random.random(), random.random()
#     return x*x + y*y < 1

# count = spark.sparkContext.parallelize(range(0, num_samples)).filter(inside).count()
# pi = 4 * count / num_samples
# print(pi)

# !pip install --user pandas 
# !pip install --user matplotlib
# !pip install --user fuzzywuzzy
# !pip install --user jellyfish
import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
from jellyfish import soundex
from jellyfish import levenshtein_distance as ld
import re
