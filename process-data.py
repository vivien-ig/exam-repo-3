
import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
job = Job(glueContext)

job.init(args["JOB_NAME"], args)

print("AWS Glue data processing job started")
print("Data processing completed successfully")

job.commit()
