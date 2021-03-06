import csv
import pandas as pd
from data_preprocessing import merge_country_and_avg_rating, data_set_processing, FINAL_DATASET_WITH_COUNTRY_FILE_PATH, FINAL_DATASET_FILE_PATH, FINAL_DATASET_CUSTOM_RATING_FILE_PATH
from data_preprocessing import merge_country_and_avg_rating, data_set_processing, FINAL_DATASET_WITH_COUNTRY_FILE_PATH, FINAL_DATASET_FILE_PATH, FINAL_DATASET_CUSTOM_RATING_FILE_PATH
from data_preprocessing import FINAL_DATASET_PLAYERS_WITH_CLUSTER_FILE_PATH,average_rating_for_players_for_kmeans,PLAYERS_AVG_K_MEANS_DATA_FILE_PATH, PLAYERS_WITH_KMEANS_CLUSTER_PATH
# from algorithms.neural_network import NeuralNetwork
from algorithms.neural_network import NeuralNetwork
from data_preprocessing import get_country_percentage_in_dataset, data_set_processing, \
    FINAL_DATASET_WITH_COUNTRY_FILE_PATH, FINAL_DATASET_FILE_PATH

from random_forest import RandomForestRegressorAlgorithm

from algorithms.factory import AlgorithmFactory
from algorithms.kmeans import KmeansAlgorithm


# from algorithms.neural_network import NeuralNetwork

class PlayerBasicStatistic:
    def __init__(self, playerCountry, avgNumberOfKils, avgNumberOfAssits, avgNumberOfDeath, avgMatchRating):
        self.playerCountry = playerCountry
        self.avgNumberOfKils = avgNumberOfKils
        self.avgNumberOfAssits = avgNumberOfAssits
        self.avgNumberOfDeath = avgNumberOfDeath
        self.avgMatchRating = avgMatchRating

    def __str__(self):
        return "Player: " + self.playerCountry + "\nAverage kills: " + str(
            self.avgNumberOfKils) + "\nAverage assists: " + str(self.avgNumberOfAssits) + "\nAverage deaths: " + str(
            self.avgNumberOfDeath) + "\nAverage match 2.0 rating: " + str(self.avgMatchRating)


# Indeksi za pristup podacima vezanih za igraca
# 1 - Naziv igraca, 2 - Tim, 3 - Protivnik, 4- Drzava, 9- broj mapa koje su igrane
# 13 - Broj kilova igraca, 14 - Broj asistencija, 15 - Broj smrti, 22 - 2.0 rating u mecu
# 10 - Mapa1, 23 - mapa1 kills, 24 - mapa1 assists, 25 - mapa 1 deaths, 26 - mapa1 hs, 32 - mapa1 rating 2.0
# 11 - Mapa2, 33 - mapa2 kills, 34 - mapa2 assists, 35 -mapa2 deaths, 36 - mapa2 hs, 42 - mapa2 rating 2.0
# 12 - Mapa3, 43 - mapa3 kills, 44 - mapa3 asissts, 45 - mapa3 deaths, 46 -mapa3 hs, 52 - mapa3 rating 2.0
# 16 - Headshots, , 23 - mapa1 kills, 24 mapa1 deaths
# 53 - kill in CT, 54 - death in CT, 58 - rating 2.0 in CT
# 59 - kill in TT, 60 - death in TT, 64 - rating 2.0 in TT

def readStatisticsForPlayer(playerName):
    playerCountry = ''
    sumNumberOfKils = 0
    sumNumberOfAssits = 0
    sumNumberOfDeath = 0
    sumMatchRating = 0.0
    numberOfRecords = 0

    with open('datasets/players.csv', newline='', encoding="utf8") as csvfile:
        players = csv.reader(csvfile, delimiter=',', quotechar='|')
        for playerData in players:
            if playerData[1].lower() == playerName.lower():
                # print(playerData[1] + '-' + playerData[4] +'-'+ playerData[13]+'-'+playerData[14]+'-'+playerData[15]+'-'+playerData[22])
                numberOfRecords = numberOfRecords + 1
                playerCountry = playerData[4]
                sumNumberOfKils = sumNumberOfKils + int(playerData[13])
                sumNumberOfAssits = sumNumberOfAssits + int(playerData[14])
                sumNumberOfDeath = sumNumberOfDeath + int(playerData[15])
                sumMatchRating = sumMatchRating + float(playerData[22])

    return PlayerBasicStatistic(playerCountry, sumNumberOfKils / numberOfRecords, sumNumberOfAssits / numberOfRecords,
                                sumNumberOfDeath / numberOfRecords, sumMatchRating / numberOfRecords)



def main():
    data_set_processing()

    #kmeans = KmeansAlgorithm('datasets/players_avg_kmeans_data.csv')
    #kmeans.fit(5)
    #kmeans.visualizing_results()
    #kmeans.predict_and_save_to_file_player_clusters('datasets/players_avg_kmeans_data.csv','datasets/players_kmeans_cluster.csv')
    # team1 = input('Unesi prvi tim: ')
    # team2 = input('Unesi drugi tim: ')
    # team1players = []
    # team2players = []

    # for i in range(1):
    #    team1players.append(input(f'Unesi {i+1}. igraca iz ' + team1 +': '))

    # for i in range(1):
    #    team2players.append(input(f'Unesi {i+1}. igraca iz ' + team2 +': '))

    # playerStatisticsFirstTeam = []
    # playerStatisticsSecondTeam = []

    # for playerName in team1players:
    #    playerStatisticsFirstTeam.append(readStatisticsForPlayer(playerName))

    # for playerName in team2players:
    #    playerStatisticsSecondTeam.append(readStatisticsForPlayer(playerName))

    # print('Za tim: ' + team1 + ' igraju sledeci igraci sa statistikama: \n')
    # for playerWithStatistics in playerStatisticsFirstTeam:
    #    print(playerWithStatistics)

    # print('Za tim: ' + team2 + ' igraju sledeci igraci sa statistikama: \n')
    # for playerWithStatistics in playerStatisticsSecondTeam:
    #    print(playerWithStatistics)


if __name__ == "__main__":
    #average_rating_for_players_for_kmeans()

    #kmeans = KmeansAlgorithm(PLAYERS_AVG_K_MEANS_DATA_FILE_PATH)
    #kmeans.fit(11)
    #kmeans.visualizing_results()
    #kmeans.predict_and_save_to_file_player_clusters(PLAYERS_AVG_K_MEANS_DATA_FILE_PATH, PLAYERS_WITH_KMEANS_CLUSTER_PATH)
    
    #data_set_processing()

    # average_ranking_for_players()
    # convert_country_to_num()
    # convert_country_to_num()
    # data_set_processing()
    # rfalg = RandomForestRegressorAlgorithm('datasets/final.csv')#.with_country()
    # rfalg.load_data()
    # rfalg.fit()
    # rfalg.predict()
    # merge_country_and_avg_rating()
    # print(get_country_percentage_in_dataset(5))

    # use_players_country=False, use_avg_country_rating=False,
    #                 use_commonness=False, use_players_country_percentage=False,
    #                 use_avg_team_country_rating=False
    #random_forest_alg = AlgorithmFactory.create(AlgorithmFactory.get_algorithm_names()[1],
    #                                             FINAL_DATASET_PLAYERS_WITH_CLUSTER_FILE_PATH)#.with_country(use_commonness=True)
    # # False, True, False,
    # #                                                                                                False, False)
    # random_forest_alg.load_data()
    # random_forest_alg.fit()
    # random_forest_alg.predict()

    # nnetwork = NeuralNetwork(FINAL_DATASET_WITH_COUNTRY_FILE_PATH)
    # nnetwork.load_data()
    # nnetwork.fit()
    # nnetwork.predict()

    #extreme_gradient_boosting_alg = AlgorithmFactory.create("XG_BOOST_REGRESSOR", FINAL_DATASET_CUSTOM_RATING_FILE_PATH)
    #extreme_gradient_boosting_alg.load_data()
    #extreme_gradient_boosting_alg.fit()
    #extreme_gradient_boosting_alg.predict()


    # random_forest_alg = AlgorithmFactory.create("RANDOM_FOREST_REGRESSOR", FINAL_DATASET_WITH_COUNTRY_FILE_PATH)
    # random_forest_alg.load_data()
    # random_forest_alg.fit()
    # random_forest_alg.predict()

    # for algorithm_name in AlgorithmFactory.get_algorithm_names():
    #     # alg = AlgorithmFactory.create(algorithm_name, FINAL_DATASET_CUSTOM_RATING_FILE_PATH)#.with_custom_rating()
    #     # alg.with_country(use_players_country=True, use_avg_country_rating=True, use_commonness=True,
    #     #                  use_players_country_percentage=True, use_avg_team_country_rating=True)
    #     if algorithm_name == "RANDOM_FOREST_REGRESSOR":
    #         for i in range(5):
    #             alg = AlgorithmFactory.create(algorithm_name, FINAL_DATASET_CUSTOM_RATING_FILE_PATH).with_custom_rating()
    #
    #             if i == 0:
    #                 alg.with_country(use_players_country=True)
    #             elif i == 1:
    #                 alg.with_country(use_avg_country_rating=True)
    #             elif i == 2:
    #                 alg.with_country(use_commonness=True)
    #             elif i == 3:
    #                 alg.with_country(use_players_country_percentage=True)
    #             elif i == 4:
    #                 alg.with_country(use_avg_team_country_rating=True)
    #
    #             alg.load_data()
    #             alg.fit()
    #             alg.predict()

    # nnetwork = NeuralNetwork(FINAL_DATASET_WITH_COUNTRY_FILE_PATH).with_country(use_commonness=True)
    # nnetwork.load_data()
    # nnetwork.fit()
    # nnetwork.predict()

    # bst = ExtremeGradientBoostingAlgorithm('datasets/final.csv')
    # bst.train()
    # bst.predict()

    # extreme_gradient_boosting_alg = AlgorithmFactory.create(AlgorithmFactory.get_algorithm_names()[1],
    #                                                         FINAL_DATASET_CUSTOM_RATING_FILE_PATH).with_custom_rating()
    # extreme_gradient_boosting_alg.load_data()
    # extreme_gradient_boosting_alg.fit()
    # extreme_gradient_boosting_alg.predict()

    random_forest_alg = AlgorithmFactory.create(AlgorithmFactory.get_algorithm_names()[1],
                                                FINAL_DATASET_CUSTOM_RATING_FILE_PATH)#.with_custom_rating()#.with_country()
    random_forest_alg.load_data()
    random_forest_alg.fit()
    random_forest_alg.predict()


