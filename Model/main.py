import Metadata
import PicksBans
import MatchHistory
import Positions
from db import Database
from tqdm import tqdm

# Inicializo el objeto DataBase
db = Database()

# Se instancia la liga y las temporadas
league = "LEC"
season = ['2020', '2021', '2022', '2023']

# Recorro la lista de los años, obtengo el dataframe de esa temporada
# y la inserto en la BBDD
for i in tqdm(range(len(season))):
    db.insert_dataframe(PicksBans.getDF_picksBans(
        league, season), "PicksBans_{}_{}".format(league, season[i]))

    db.insert_dataframe(MatchHistory.getDF_MH(league, season[i]),
                        "MatchHistory_{}_{}".format(league, season[i]))

    db.insert_dataframe(Metadata.getDF_positions(
        league, season), "Metadata_{}_{}".format(league, season))

    db.insert_dataframe(Positions.getDF_positions(league, season[i]),
                        "Positions_{}_{}".format(league, season[i]))

db.close
