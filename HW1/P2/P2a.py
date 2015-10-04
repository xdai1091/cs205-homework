from P2 import *
#import findspark; findspark.init();
import pyspark as py
import matplotlib.pyplot as plt
def location(x):
	return x/500.0 -2 ;

#initiate spark
#create sparkConf and a new Spark
conf = py.SparkConf().setAppName("CS205HW1")
sc = py.SparkContext();
#create a 2000 rdd, it has 10 partitions
rdd1 = sc.parallelize(range(2000),10);
#get a 2000 * 2000 rdd
rdd2 = rdd1.cartesian(rdd1);
#map the function
rdd2 = rdd2.map(lambda (x,y): ((x,y),mandelbrot(location(y),location(x))));
draw_image(rdd2);
#use this to produce an histogram for each paritition
result = sum_values_for_partitions(rdd2);
#collect data and plot it
plt.hist(result.collect());
plt.title("effort on each partition");
plt.xlabel("iteration counts");
plt.ylabel("numbers of partitions");
plt.show();
plt.savefig("P2a_hit.png");
