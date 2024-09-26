from pysus.ftp.databases.cnes import CNES
from fastparquet import ParquetFile

cnes = CNES()

UF = ["SC"]
YEARS = ["2023"]
MONTHS = [1]

cnes.load()

files = cnes.get_files("LT", uf=UF, year=YEARS, month=MONTHS)

for file in files:
    parquet = cnes.download(file)

    pf = ParquetFile(f"{parquet}")

    df = pf.to_pandas()

    df.to_csv(f"{parquet}".split("/")[-1].split(".")[0] + ".csv")

    print(df.columns)
