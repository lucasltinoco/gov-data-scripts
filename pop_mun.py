from sidrapy import get_table

COD_MUN = "4205407"
PERIOD = "all"


data = get_table(
    table_code="6579",
    territorial_level="6",
    ibge_territorial_code=COD_MUN,
    period=PERIOD,
)


print(data.head())
data.to_csv(f"pop_{COD_MUN}.csv")
