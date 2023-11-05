"""
Main cli or app entry point
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # extract data
    extract()
    # start spark session
    spark = start_spark("Diabetes")
    # load data into dataframe
    df = load_data(spark)
    # example metrics
    describe(df)
    # query
    query(
        spark,
        df,
        "SELECT * FROM diabetes WHERE  Outcome= 0",
        "diabetes",
    )
    # example transform
    example_transform(df)
    # end spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
