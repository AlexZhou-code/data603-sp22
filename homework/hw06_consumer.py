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

#returns a new DataFrame.
stream_df = lines.selectExpr("CAST(value AS STRING) AS payload")

writer = (
	stream_df.writeStream
	.queryName('iss')
	.format('memory')
	.outputMode('append')
)

streamer = writer.start()

#read lat and lon
for i in range(10):
	df = spark.sql("select * from iss")
	df.show()
    
    #json files, so sql easy to do this
	final_df = spark.sql("""
SELECT
	get_json_object(payload, '$.iss_position.latitude') AS latitude,
	get_json_object(payload, '$.iss_position.longitude') AS longitude
FROM iss
""").toPandas()
    
	print(final_df)
	time.sleep(5)

 #30mins
streamer.awaitTermination(timeout=30*60,TimeUnit.SECONDS)

print('streaming finish')



#build plot
geometry = final_df(x='latitude', y='longitude')
gdf = GeoDataFrame(geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)




plt.savefig('hw06_map.jpg')

