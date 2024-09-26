from pysus.ftp.databases.sim import SIM
from fastparquet import ParquetFile

UF = ["SC"]
YEARS = ["2010"]

sim = SIM().load()

files = sim.get_files("CID10", uf=UF, year=YEARS)

for file in files:
    parquet = sim.download(file)

    pf = ParquetFile(f"{parquet}")

    df = pf.to_pandas()

    df.to_csv(f"{parquet}".split("/")[-1].split(".")[0] + ".csv")

    print(df.columns)
