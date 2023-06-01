import Metadata
import PicksBans
import MatchHistory
import Positions
from db import Database
from tqdm import tqdm

# Inicializo el objeto DataBase
db = Database()

# 2019 LEC
league = "LEC"
season = ['2020','2021','2022','2023']

""" for i in tqdm(range(len(season))):
    db.insert_dataframe(PicksBans.getDF_picksBans(
        league, season), "PicksBans_{}_{}".format(league, season[i]))
    
    db.insert_dataframe(MatchHistory.getDF_MH(league, season[i]),
                        "MatchHistory_{}_{}".format(league, season[i]))
    # db.insert_dataframe(Positions.getDF_positions(league,season),"Positions_{}_{}".format(league, season))
    db.insert_dataframe(Positions.getDF_positions(league, season[i]),
                        "Positions_{}_{}".format(league, season[i])) """

db.insert_dataframe(MatchHistory.getDF_MH(league, "2022"),
                        "MatchHistory_{}_{}".format(league, "2022"))

db.close
