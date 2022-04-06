import time

import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from urllib.request import urlopen
import pandas as pd
import pyspark
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, TimestampType, ArrayType, DateType
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame

spark = (SparkSession
         .builder
         .appName("streamingSpark")
         .getOrCreate()
        )

spark.sparkContext.setLogLevel("ERROR")

lines = (
	spark.readStream
	.format("socket")
	.option("host", "localhost")
	.option("port", 22223)
	.load()
)

stream_df = lines.selectExpr("CAST(value AS STRING) AS payload")

writer = (
	stream_df.writeStream
	.queryName('iss')
	.format('memory')
	.outputMode('append')
)

streamer = writer.start()

for i in range(5):
	all_df = spark.sql("select * from iss")
	all_df.show()
	temp_df = spark.sql("""
SELECT
	get_json_object(payload, '$.iss_position.latitude') AS latitude,
	get_json_object(payload, '$.iss_position.longitude') AS longitude
FROM iss
""").toPandas()

	print(temp_df)
	time.sleep(5)

streamer.awaitTermination(timeout=30)
print('streaming done')




geometry = temp_df(x='latitude', y='longitude')
gdf = GeoDataFrame(geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)




plt.savefig('hw06_map.jpg')

