import Metadata
import PicksBans
import MatchHistory
import Positions
from db import Database
from tqdm import tqdm



def main():    
    
    """
    La función inserta marcos de datos de picks y bans, historial de partidos, metadatos
    y posiciones para una liga y temporada determinadas en una base de datos.
    """
    # Se instancia la liga y las temporadas
    league = input("Inserte una liga válida: (LEC,LCS,LCK,LJL,PCS,VCS)")
    season = ['2020', '2021', '2022', '2023']

    # Recorro la lista de los años, obtengo el dataframe de esa temporada
    # y la inserto en la BBDD
    for i in tqdm(range(len(season))):
        #Picks y Bans
        db.insert_dataframe(PicksBans.getDF_picksBans(league, season[i]), "PicksBans_{}_{}".format(league, season[i]))

        # Historial de partida
        db.insert_dataframe(MatchHistory.getDF_MH(league, season[i]),
                            "MatchHistory_{}_{}".format(league, season[i]))

        # Metadata
        db.insert_dataframe(Metadata.getDF_positions(
            league, season), "Metadata_{}_{}".format(league, season[i]))

        # Posiciones
        db.insert_dataframe(Positions.getDF_positions(league, season[i]),
                            "Positions_{}_{}".format(league, season[i]))

    db.close

if __name__ == "__main__":
    # Inicializo el objeto DataBase
    db = Database()
    main()