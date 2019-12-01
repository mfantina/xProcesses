from random import randint
import cycle as cycle
from multiprocessing import Pool

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def creator_plotting_files(var):
    plot = open('output-graphs/plotting/plotting_{0}.txt'.format(var), 'w')
    plot.close()

def create_plotting_files(num_islands, num_threads):
    p = Pool(num_threads)
    p.map(creator_plotting_files, num_islands)
    p.close()

def set_broadcast(population, sortedEvaluatedPopulation, islandNumber, percentageOfBestIndividualsForMigrationPerIsland, broadcast):
    allBests = []
    for i in range(int((len(population)) * percentageOfBestIndividualsForMigrationPerIsland)):
        allBests.append([population[sortedEvaluatedPopulation[i][5]], [sortedEvaluatedPopulation[i][0]]])
    broadcast[islandNumber] = allBests

def reset_broadcast(islandNumber, broadcast):
    broadcast[islandNumber] = []
    return

def pick_island(island_number, island_size, num_islands, percentageOfBestIndividualsForMigrationPerIsland, migration_index, broadcast, islandSizes, percentageOfBestIndividualsForMigrationAllIslands):
    pickedIsland = randint(0, num_islands - 1)
    count = 0
    while (pickedIsland == island_number) or (migration_index[pickedIsland] >= int(percentageOfBestIndividualsForMigrationAllIslands[pickedIsland]*islandSizes[pickedIsland])) or (len(broadcast[pickedIsland]) == 0):
        if count == 10:
            return -1
        else:
            count = count + 1
            pickedIsland = randint(0, num_islands - 1)
    return pickedIsland

def send_individuals(population, island_number, num_islands, sortedEvaluatedPopulation, messenger):
    pickedIsland = randint(0, num_islands - 1)
    count = 0
    while (pickedIsland == island_number):
        if count == 10:
            pickedIsland = -1
        else:
            count = count + 1
            pickedIsland = randint(0, num_islands - 1)
    if pickedIsland != -1:
        messenger[pickedIsland] = [sortedEvaluatedPopulation[0][0], population[sortedEvaluatedPopulation[0][5]], island_number]

def receive_individuals(population, island_number, sortedEvaluatedPopulation, messenger):
    if messenger[island_number] != [[], [], []]:
        best_fit = messenger[island_number]
        messenger[island_number] = [[], [], []]
    else:
        return 0
    population[sortedEvaluatedPopulation[-1][5]] = best_fit[1]
    return 1

def reset_receive_individuals(island_number, messenger):
    messenger[island_number] = [[], [], []]

def do_migration(island_population, island_number, num_islands, island_fitness, percentageOfIndividualsForMigrationPerIsland, percentageOfBestIndividualsForMigrationPerIsland, broadcast, islandSizes, percentageOfBestIndividualsForMigrationAllIslands):
    migration_index = []
    for i in range(num_islands):
        migration_index.append(0)
    worst_gen_list = []
    count = 0
    for individuo in range(len(island_fitness)):
        worst_gen_list.append([island_fitness[individuo], count])
        count += 1
    sorted_worst_gen_list = sorted(worst_gen_list, reverse=False, key=cycle.takeFirst)
    iter = 0
    while iter < percentageOfIndividualsForMigrationPerIsland * (len(island_population)):
        picked_island = pick_island(island_number, len(island_population), num_islands, percentageOfBestIndividualsForMigrationPerIsland, migration_index, broadcast, islandSizes, percentageOfBestIndividualsForMigrationAllIslands)
        if picked_island != -1:
            island_selected = broadcast[picked_island]
            best_ind = island_selected[migration_index[picked_island]]
            migration_index[picked_island] += 1
            island_population[sorted_worst_gen_list[iter][1]] = best_ind[0]
            iter = iter + 1
        else:
            break
    return


























