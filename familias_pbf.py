import requests
import pandas as pd

dt1a = "2004-01-01"
dt2a = "2019-03-01"
dt1b = "2004-01-01"
dt2b = "2024-09-01"
COD_MUN = 420540

url = f"https://aplicacoes.cidadania.gov.br/vis/data3/v.php?q[]=r6JtZJCug7BtxKW25rV%2FfmdhhJFkl21kmK19ZnB1ZXOmaX7KmZO20qfOnJm%2B6IianbSon7SfrrqqkpKcmcuppsK2iKextVi1mpyuwZxNzsmY2F1zyuDAk522pHa2YH9%2BaV6EkmOXbWSEm8GcobZVetufrL%2BrkbbHlNddmMnuslSqvaGmmZ67sliqkseU1rCYmOGuoK%2BtcHXfmrnBnGiS1KjXYK5%2B3q6noWisot6nbY6kksrAlNiscZqif2Rue2JqrGZ9f15Ny8mY2F1zv%2BGspbCslKDapm2zo6C8gaHfqZ994LuYXcVwoNqlwLNyk7jNps94bsPcuaehg3Ct7qZwyViQuNSYirSbwultdKmtqJnap7yKdFSJkWWbamSNqH1lY2ipot6nbY6Zk7bXn4qin9DgbaKxtKFa3qexb7RovcKf3aJuw9y5p6GDcKDapcCzcmjK1qCNuFTA3MCZXL%2Bdn%2BdZjbucoLbCodl7cIStfWZvdWVtpml%2BdVehv8ahin2Vw9rDoFytoa3eWbvDo5l3xqHOXrCY4a6gr61woNqlwLNyaL3Cn92ibpjuwqFfw1ad2qyybq6VvM9TqqqY0NquoquEcmGraX9%2FZF6HjmObZFPR47KiXHCYm%2ByebcWfksWBc8yjks7vsZOiqaJ4qVnBtpybd9Oi36uXhbuvmpu%2BoXSzp8K7nJ%2FAxGKqn5m87MGYm66Wp6Vrdm6cmcrGU9iyn8mbsqKgcVWf5ayybqWiw81Tz6uXfviImp20qJ%2B0n666qpKSnJnLqabCtoinsbVYtZqcrsGcTc7JmNhdc8rgwJOdtqR4tmB%2FfmlghJFml21khJvBnKG2VWLcmsCzV6S%2FxqGKfamPsYFnenhVruGeu26pnMzPl5J9lcPaw6B2gqOv5p6%2Ft5pcl9dloHFmia12VKG0qJ%2BZp8K6o028z5eTXZjJ7rJUqr2hppmeu7JYqpLHlNawmJjhrqCvrXB135q5wZxoktSo17l5vugQ4aixlq2Ze7K8nJPAxJwt3qXG3MBXgqmi%2FSaltq%2BqTaejeYpllNE%2B9lSLvalpq2l%2Ff2BQncKgLeqfxtzAVIyKe1qhmm2%2BmJ%2FLyqWKoZh9yK6ma3plbKxicKSYmcbTU9yio77uwJWgt1X9GaxttJiaGg6f056mfcuPelxwlq484m2drKGGk2OcblyA0a6gq7pVrN6prsGqjrvQUy3dpn3hrqH%2F9aGj2qxtnnlzd4mUiq2Uz%2B%2B2plysmlrGmr99aV2JlFyNk5TJ6r9UoLdVfN6nsrT62rrKooqq9gbftqNccJauPOJtnayhhpNjnG5cgNGuoKu6VZ7oWY%2BzpZK9JODNpqJ96BDdoLGkWqGabb6Yn8vKpYqhmH3IrqZremVsrGLJvnKp091lmm1miqt%2BYWx5iWqpc31%2BcV2Hu24%3D&dt1={dt1a}&dt2={dt2a}&dt1={dt1b}&dt2={dt2b}&ultdisp=1&ultdisp=0&ag=m&codigo={COD_MUN}&wt=json&tp_funcao_consulta=0&rqprocess=0acd806d53d234f5791c360805ddd148"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_gid=GA1.3.385923660.1727199971; lgpdsagi_cookie_status=accept; _ga_69GTL3NVCB=GS1.3.1727199972.1.1.1727200187.0.0.0; PHPSESSID=36n27ostcanmva9gui933msa3o; _ga=GA1.3.2031857240.1727199971; _gat_gtag_UA_17852265_1=1; _ga_GG5CDDLS9P=GS1.1.1727353322.7.1.1727353329.0.0.0",
    "Origin": "https://aplicacoes.cidadania.gov.br",
    "Referer": "https://aplicacoes.cidadania.gov.br/vis/data3/v.php",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
}

data = {
    "draw": 2,
    "columns[0][data]": 0,
    "columns[0][name]": "sigla",
    "columns[0][searchable]": "true",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": 1,
    "columns[1][name]": "mes_ano_formatado",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": 2,
    "columns[2][name]": "(case when t.mes_ano<='2021-10-01' then t.bf_qtd_fam else null)",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": 3,
    "columns[3][name]": "(case when t.mes_ano>='2023-03-01' then t.bf_qtd_fam else null)",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": 4,
    "columns[4][name]": "(case when t.mes_ano<='2021-10-01' then t.bf_vl else null end)",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": 5,
    "columns[5][name]": "(case when t.mes_ano>='2023-03-01' then t.bf_vl else null end)",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": 6,
    "columns[6][name]": "(case when t.mes_ano<='2021-10-01' then (case when t.bf_qtd_fam else null))",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": 7,
    "columns[7][name]": "(case when t.mes_ano>='2023-03-01' then (case when t.v2643>0 then ... else null))",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "order[0][column]": 0,
    "order[0][dir]": "asc",
    "start": 0,
    "length": 50,
    "search[value]": "",
    "search[regex]": "false",
}


response = requests.post(url, headers=headers, data=data)

df = pd.DataFrame(response.json()["data"])
df.columns = [
    "UF",
    "Ref",
    "FPBF (<10/21)",
    "FPBF (>3/23)",
    "Val Rep FPBF (<10/21)",
    "Val Rep FPBF (>3/23)",
    "Val Ben méd (<10/21)",
    "Val Ben méd (>3/23)",
]

print(df.head())
