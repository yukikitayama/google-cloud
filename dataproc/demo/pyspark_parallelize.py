import pyspark


def main():

    # Make a sequential array
    numbers = [i for i in range(100)]

    # Make PySpark object
    sc = pyspark.SparkContext()

    # Make parallel object with the array input
    parallel = sc.parallelize(numbers)

    # Run lambda function or supply a function to
    # execute the function in parallel to the elements in the array
    parallel.foreach(lambda number: print(number))


if __name__ == '__main__':
    main()
