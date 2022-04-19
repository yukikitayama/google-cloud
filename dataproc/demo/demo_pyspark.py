import pyspark


def main():
    numbers = [i for i in range(100)]
    sc = pyspark.SparkContext()
    parallel = sc.parallelize(numbers)
    parallel.foreach(lambda number: print(number))


if __name__ == '__main__':
    main()
