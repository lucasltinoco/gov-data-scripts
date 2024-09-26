import sidrapy

COD_MUN = "4205407"
PERIOD = "2019"

data = sidrapy.get_table(
    table_code="5938",
    territorial_level="6",
    ibge_territorial_code=COD_MUN,
    period=PERIOD,
)

print(data.head())
data.to_csv(f"pib_{COD_MUN}.csv")
