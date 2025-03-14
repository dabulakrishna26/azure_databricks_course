# Databricks notebook source
# MAGIC %scala
# MAGIC spark.conf.set(
# MAGIC     "fs.azure.account.key.kkformuladl.dfs.core.windows.net",
# MAGIC     dbutils.secrets.get(scope="data-lake-key1",key="kkformuladl"))

# COMMAND ----------

# MAGIC %md
# MAGIC #secrets/createScope is used to enter the   Vault key name and reosurce id
# MAGIC #data-lake-key1 is created in DATABRICKS scope
# MAGIC #key is secret in key value

# COMMAND ----------

# MAGIC %scala
# MAGIC val df = spark.read.format("csv").option("header","true").load("abfss://raw@kkformuladl.dfs.core.windows.net/log.csv")
# MAGIC 
# MAGIC display(df)

# COMMAND ----------

# MAGIC %scala
# MAGIC spark.conf.set(
# MAGIC     "fs.azure.account.key.kkformuladl.dfs.core.windows.net",
# MAGIC     "uY6oAZ2Mkz8054Ie7NaoVm0/IM6mhLXyEy+BCPTqAtw+Fr8dnAZ74mKkQKfD9xK+O0MWHCzleBwf+AStys1egg==")

# COMMAND ----------

df=spark.read.csv(path="abfss://raw@kkformuladl.dfs.core.windows.net/log.csv",header=True)
display(df)
