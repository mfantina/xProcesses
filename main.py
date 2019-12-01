import plotting as plot
import recording as record
import cycle as cycle
import initialPopulation as iniPop
import operators as op
import fitness as fit
import islands as isl
import addressLog as adLog
import multiprocessing
import paramSelfTunning as pst
import pandas as pd
import copy
from ast import literal_eval
from datetime import datetime
from functools import partial

numberOfParametersCombinations = 1
numberOfThreads = 1
numberOfRounds = 222

def runRound(par, parComb, parCount, numberOfThreads, round, broadcast, messenger, islandSizes, percentageOfBestIndividualsForMigrationAllIslands, taskAddition, sampledLog, fullLog, alphabet, islandNumber):              # added "messenger" + "taskAddition"  [hiddenTasks]
    islandStart = datetime.now()
    population_size = int(par[islandNumber + parCount][1])
    numberOfGenerations = int(par[islandNumber + parCount][2])
    crossoverType = int(par[islandNumber + parCount][3])
    crossoverTasksNumPerc = float(par[islandNumber + parCount][4])
    crossoverProbability = float(par[islandNumber + parCount][5])
    mutationType = int(par[islandNumber + parCount][6])
    mutationTasksNumPerc = float(par[islandNumber + parCount][7])
    tasksMutationStartProbability = float(par[islandNumber + parCount][8])
    tasksMutationEndProbability = float(par[islandNumber + parCount][9])
    operatorsMutationStartProbability = float(par[islandNumber + parCount][10])
    operatorsMutationEndProbability = float(par[islandNumber + parCount][11])
    changeMutationRateType = int(par[islandNumber + parCount][12])
    changeMutationRateExpBase = float(par[islandNumber + parCount][13])
    drivenMutation = int(par[islandNumber + parCount][14])
    drivenMutationPart = float(par[islandNumber + parCount][15])
    limitBestFitnessRepetionCount = int(par[islandNumber + parCount][16])
    numberOfcyclesAfterDrivenMutation = int(par[islandNumber + parCount][17])
    completenessWeight = float(par[islandNumber + parCount][18])
    TPweight = float(par[islandNumber + parCount][19])
    precisenessStart = float(par[islandNumber + parCount][22])
    simplicityStart = int(par[islandNumber + parCount][23])
    evolutionEnd = int(par[islandNumber + parCount][24])
    completenessAttemptFactor1 = int(par[islandNumber + parCount][25])
    completenessAttemptFactor2 = float(par[islandNumber + parCount][26])
    elitismPerc = float(par[islandNumber + parCount][27])
    selectionOp = int(par[islandNumber + parCount][28])
    selectionTp = int(par[islandNumber + parCount][29])
    lambdaValue = int(par[islandNumber + parCount][30])
    HammingThreshold = int(par[islandNumber + parCount][31])
    migrationtime = int(par[islandNumber + parCount][32])
    percentageOfBestIndividualsForMigrationPerIsland = float(par[islandNumber + parCount][34])
    percentageOfIndividualsForMigrationPerIsland = float(par[islandNumber + parCount][35])
    fitnessStrategy = int(par[islandNumber + parCount][37])
    ### pst ### maxTempGen = 100                                                                                         # Depois deve existir no Excel
    ### pst ### satime = 1                                                                                              # Depois deve existir no Excel
    ### pst ### expectedProgression = 0.5                                                                               # Depois deve existir no Excel    
    ### pst ### names = ['[8] tasksMutationStartProbability', '[10] operatorsMutationStartProbability', '[32] migrationtime','[34] percentageOfBestIndividualsForMigrationPerIsland', '[35] percentageOfIndividualsForMigrationPerIsland']
    if fitnessStrategy == 0:
        precisenessWeight = float(par[islandNumber + parCount][20])
        simplicityWeight = float(par[islandNumber + parCount][21])
    else:
        precisenessWeight = 0
        simplicityWeight = 0
    islandSizes[islandNumber] = population_size
    percentageOfBestIndividualsForMigrationAllIslands[islandNumber] = percentageOfBestIndividualsForMigrationPerIsland
    highestValueAndPosition = [[0, 0, 0], -1]
    if highestValueAndPosition[0][1] >= precisenessStart:
        precisenessWeight = float(par[islandNumber + parCount][20])
    numberOfHiddenTask = 0                                                                                              # Added [hiddenTasks]
    (population, evaluatedPopulation, referenceCromossome, averageEnabledTasks) = iniPop.initializePopulation(population_size, TPweight, precisenessWeight, simplicityWeight, completenessWeight, completenessAttemptFactor1, completenessAttemptFactor2, selectionOp, alphabet, sampledLog[0], numberOfHiddenTask)
    fitnessEvolution = []
    (highestValueAndPosition, sortedEvaluatedPopulation) = cycle.chooseHighest(evaluatedPopulation)
    lowestValue = cycle.chooseLowest(sortedEvaluatedPopulation)
    averageValue = cycle.calculateAverage(evaluatedPopulation)
    fitnessEvolution.append([lowestValue, highestValueAndPosition[0][0], averageValue, 0, highestValueAndPosition[0][1], highestValueAndPosition[0][2], highestValueAndPosition[0][3], highestValueAndPosition[0][4], 0, 0, 0, 0])
    if (fitnessEvolution[0][10] >= simplicityStart) and (precisenessWeight > 0):
        simplicityWeight = float(par[islandNumber + parCount][21])
    print('NLI:', sampledLog[2], '| COMB:', parComb, '| RND:', round, '| TF:', '%.5f' % highestValueAndPosition[0][0], '| C:', '%.5f' % highestValueAndPosition[0][1], '| TP:', '%.5f' % highestValueAndPosition[0][2], '| P:', '%.8f' % highestValueAndPosition[0][3], '| S:', '%.5f' % highestValueAndPosition[0][4], '| ISL:', '{:>2}'.format(islandNumber), '| GEN:', '{:>5}'.format('0'), '| REP:', '{:>3}'.format(fitnessEvolution[0][3]), '{:>3}'.format(fitnessEvolution[0][8]), '{:>3}'.format(fitnessEvolution[0][9]), '{:>3}'.format(fitnessEvolution[0][10]), '{:>3}'.format(fitnessEvolution[0][11]))
    drivenMutatedIndividuals = [0 for _ in range(len(population))]
    drivenMutatedGenerations = 0
    for currentGeneration in range(1, numberOfGenerations):
        if highestValueAndPosition[0][1] >= precisenessStart:
            precisenessWeight = float(par[islandNumber + parCount][20])
        (tasksMutationProbability, operatorsMutationProbability) = op.defineMutationProbability(tasksMutationStartProbability, tasksMutationEndProbability, operatorsMutationStartProbability, operatorsMutationEndProbability, numberOfGenerations, currentGeneration, changeMutationRateType, changeMutationRateExpBase)
        (population, evaluatedPopulation, drivenMutatedIndividuals, drivenMutatedGenerations) = cycle.generation(population, referenceCromossome, evaluatedPopulation, crossoverType, crossoverProbability, crossoverTasksNumPerc, mutationType, mutationTasksNumPerc, tasksMutationProbability, operatorsMutationProbability, drivenMutation, drivenMutationPart, limitBestFitnessRepetionCount, fitnessEvolution[currentGeneration - 1][3], drivenMutatedIndividuals, drivenMutatedGenerations, TPweight, precisenessWeight, simplicityWeight, completenessWeight, elitismPerc, sortedEvaluatedPopulation, selectionOp, selectionTp, lambdaValue, HammingThreshold, currentGeneration, completenessAttemptFactor1, completenessAttemptFactor2, numberOfcyclesAfterDrivenMutation, alphabet, sampledLog[0], numberOfHiddenTask)
        (highestValueAndPosition, sortedEvaluatedPopulation) = cycle.chooseHighest(evaluatedPopulation)
        lowestValue = cycle.chooseLowest(sortedEvaluatedPopulation)
        averageValue = cycle.calculateAverage(evaluatedPopulation)
        fitnessEvolution.append([lowestValue, highestValueAndPosition[0][0], averageValue, 0, highestValueAndPosition[0][1], highestValueAndPosition[0][2], highestValueAndPosition[0][3], highestValueAndPosition[0][4], 0, 0, 0, 0])
        if fitnessEvolution[currentGeneration][1] == fitnessEvolution[currentGeneration - 1][1]:
            fitnessEvolution[currentGeneration][8] = fitnessEvolution[currentGeneration - 1][8] + 1
        if fitnessEvolution[currentGeneration][4] == fitnessEvolution[currentGeneration - 1][4]:
            fitnessEvolution[currentGeneration][3] = fitnessEvolution[currentGeneration - 1][3] + 1
        if fitnessEvolution[currentGeneration][5] == fitnessEvolution[currentGeneration - 1][5]:
            fitnessEvolution[currentGeneration][9] = fitnessEvolution[currentGeneration - 1][9] + 1
        if fitnessEvolution[currentGeneration][6] == fitnessEvolution[currentGeneration - 1][6]:
            fitnessEvolution[currentGeneration][10] = fitnessEvolution[currentGeneration - 1][10] + 1
        if fitnessEvolution[currentGeneration][7] == fitnessEvolution[currentGeneration - 1][7]:
            fitnessEvolution[currentGeneration][11] = fitnessEvolution[currentGeneration - 1][11] + 1
        if (fitnessEvolution[currentGeneration][10] >= simplicityStart) and (precisenessWeight > 0):
            simplicityWeight = float(par[islandNumber + parCount][21])
        print('NLI:', sampledLog[2], '| COMB:', parComb, '| RND:', round, '| TF:', '%.5f' % highestValueAndPosition[0][0], '| C:', '%.5f' % highestValueAndPosition[0][1], '| TP:', '%.5f' % highestValueAndPosition[0][2], '| P:', '%.8f' % highestValueAndPosition[0][3], '| S:', '%.5f' % highestValueAndPosition[0][4], '| ISL:', '{:>2}'.format(islandNumber), '| GEN:', '{:>5}'.format(currentGeneration), '| REP:', '{:>3}'.format(fitnessEvolution[currentGeneration][8]), '{:>3}'.format(fitnessEvolution[currentGeneration][3]), '{:>3}'.format(fitnessEvolution[currentGeneration][9]), '{:>3}'.format(fitnessEvolution[currentGeneration][10]), '{:>3}'.format(fitnessEvolution[currentGeneration][11]))
        isl.set_broadcast(population, sortedEvaluatedPopulation, islandNumber, percentageOfBestIndividualsForMigrationPerIsland, broadcast)                     # Added [hiddenTasks]
        if (highestValueAndPosition[0][1] >= 0.9):
            if len(fullLog[0]) > 0:
                (sampledLog[0], fullLog[0]) = adLog.sampleLog(sampledLog[0], fullLog[0])
                sampledLog[2] = sampledLog[2] + 1
                (referenceCromossome, averageEnabledTasks) = iniPop.createAuxiliaryCromossome(sampledLog[0], alphabet)
                #print('fullLog[0]', fullLog[0])                                                                        # NÃO LEMBRO O QUE É ISSO!
                #print('sampledLog[0]', sampledLog[0])                                                                  # NÃO LEMBRO O QUE É ISSO!
            #if len(fullLog[0]) > 0:                                                                                    # NÃO LEMBRO O QUE É ISSO!
            #    if sampledLog[1] == numberOfThreads:                                                                   # NÃO LEMBRO O QUE É ISSO!
            #        sampledLog[1] = sampledLog[1] - 1                                                                  # NÃO LEMBRO O QUE É ISSO!
            #        sampledLog[2] = sampledLog[2] + 1                                                                  # NÃO LEMBRO O QUE É ISSO!
            #        (sampledLog[0], fullLog[0]) = adLog.sampleLog(sampledLog[0], fullLog[0])                           # NÃO LEMBRO O QUE É ISSO!
            #    else:                                                                                                  # NÃO LEMBRO O QUE É ISSO!
            #        sampledLog[1] = sampledLog[1] - 1                                                                  # NÃO LEMBRO O QUE É ISSO!
            #        if sampledLog[1] == 0:                                                                             # NÃO LEMBRO O QUE É ISSO!
            #            sampledLog[1] = numberOfThreads                                                                # NÃO LEMBRO O QUE É ISSO!
        if ((fitnessStrategy == 0) and ((highestValueAndPosition[0][1] == 0.5) and (fitnessEvolution[currentGeneration][8] >= evolutionEnd))) or ((fitnessStrategy == 1) and ((highestValueAndPosition[0][1] == 0.5) and (highestValueAndPosition[0][3] > 0) and (highestValueAndPosition[0][4] > 0) and (fitnessEvolution[currentGeneration][10] >= evolutionEnd) and (fitnessEvolution[currentGeneration][11] >= evolutionEnd))):
            break
            #if (highestValueAndPosition[0][1] == 1.0):                                                                 # Não me lembro para que serve esse if-else. Da forma como está, nunca entra no "else"
            #    broadcast[-1] = 0                                                                                      # Não me lembro para que serve esse if-else. Da forma como está, nunca entra no "else"
            #else:                                                                                                      # Não me lembro para que serve esse if-else. Da forma como está, nunca entra no "else"
            #    if taskAddition[-2] == 0:                                                                              # Não me lembro para que serve esse if-else. Da forma como está, nunca entra no "else"
            #        for nt in range(numberOfThreads + 1):                                                              # Não me lembro para que serve esse if-else. Da forma como está, nunca entra no "else"
            #            taskAddition[nt] = 1                                                                           # Não me lembro para que serve esse if-else. Da forma como está, nunca entra no "else"
        if (currentGeneration == -1):   #if (currentGeneration % 70 == 0):                                              # hiddenTasks está desligado!
            if (taskAddition[-2] == 0) and (taskAddition[-1] == numberOfThreads):                                       # hiddenTasks está desligado!
                for nt in range(numberOfThreads + 1):                                                                   # hiddenTasks está desligado!
                    taskAddition[nt] = 1                                                                                # hiddenTasks está desligado!
            taskAddition[-1] = taskAddition[-1] - 1                                                                     # hiddenTasks está desligado!
            if taskAddition[-1] == 0:                                                                                   # hiddenTasks está desligado!
                taskAddition[-1] = numberOfThreads                                                                      # hiddenTasks está desligado!
        #if broadcast[-1] == 0:                                                                                         # NÃO LEMBRO O QUE É ISSO!
        #    break                                                                                                      # NÃO LEMBRO O QUE É ISSO!
        if taskAddition[islandNumber] == 1:                                                                             # hiddenTasks está desligado!
            population = iniPop.addHiddenTask(population, population_size)                                              # hiddenTasks está desligado!
            numberOfHiddenTask = numberOfHiddenTask + 1                                                                 # hiddenTasks está desligado!
            referenceCromossome = iniPop.updateReferenceCromossomeWithHiddenTask(referenceCromossome)                   # hiddenTasks está desligado!
            isl.reset_receive_individuals(islandNumber, messenger)                                                      # hiddenTasks está desligado!
            isl.reset_broadcast(islandNumber, broadcast)                                                                # hiddenTasks está desligado!
            taskAddition[islandNumber] = 0                                                                              # hiddenTasks está desligado!
            sumTaskAdditions = 0                                                                                        # hiddenTasks está desligado!
            for nt in range(numberOfThreads + 1):                                                                       # hiddenTasks está desligado!
                sumTaskAdditions = sumTaskAdditions + taskAddition[nt]                                                  # hiddenTasks está desligado!
            if sumTaskAdditions == 1:                                                                                   # hiddenTasks está desligado!
                taskAddition[-2] = 0                                                                                    # hiddenTasks está desligado!
        if taskAddition[-2] == 0:                                                                                       # Esse é o caminho tradicional (original)
            if isl.receive_individuals(population, islandNumber, sortedEvaluatedPopulation, messenger) == 1:
                evaluatedPopulation = fit.evaluationPopulation(population, referenceCromossome, TPweight, precisenessWeight, simplicityWeight, completenessWeight, completenessAttemptFactor1, completenessAttemptFactor2, selectionOp, alphabet, sampledLog[0], numberOfHiddenTask)
                (highestValueAndPosition, sortedEvaluatedPopulation) = cycle.chooseHighest(evaluatedPopulation)
            if (currentGeneration > 0) and (currentGeneration % migrationtime == 0):
                island_fitness = []
                for i in range(len(evaluatedPopulation[1])):
                    island_fitness.append(evaluatedPopulation[1][i][0])
                isl.do_migration(population, islandNumber, numberOfThreads, island_fitness, percentageOfIndividualsForMigrationPerIsland, percentageOfBestIndividualsForMigrationPerIsland, broadcast, islandSizes, percentageOfBestIndividualsForMigrationAllIslands)
                isl.send_individuals(population, islandNumber, numberOfThreads, sortedEvaluatedPopulation, messenger)
                evaluatedPopulation = fit.evaluationPopulation(population, referenceCromossome, TPweight, precisenessWeight, simplicityWeight, completenessWeight, completenessAttemptFactor1, completenessAttemptFactor2, selectionOp, alphabet, sampledLog[0], numberOfHiddenTask)
                (highestValueAndPosition, sortedEvaluatedPopulation) = cycle.chooseHighest(evaluatedPopulation)
        #if (currentGeneration % 10 == 0):
        record.record_evolution(sampledLog[2], sampledLog[0], str(parComb), str(islandNumber), str(round), par[islandNumber + parCount], islandNumber, highestValueAndPosition[0], fitnessEvolution, alphabet, population[highestValueAndPosition[1]], islandStart, datetime.now(), datetime.now() - islandStart, currentGeneration)
        ### pst ### if (currentGeneration > 0 and (numberOfGenerations-currentGeneration > 10) and currentGeneration%satime == 0):
            ### pst ### print("ISLAND: ", islandNumber, "currently at Simulated Annealing")
            ### pst ### #Simulated Annealing
            ### pst ### island_fitness = []
            ### pst ### for i in range(len(evaluatedPopulation[1])):
                ### pst ### island_fitness.append(evaluatedPopulation[1][i][0])
            ### pst ### currentFitness = max(island_fitness)
            ### pst ### parametersTP = [tasksMutationStartProbability,operatorsMutationStartProbability,
                             ### pst ### migrationtime,percentageOfBestIndividualsForMigrationPerIsland,
                             ### pst ### percentageOfIndividualsForMigrationPerIsland]
            ### pst ### pst.SA(islandNumber, expectedProgression, currentGeneration, maxTempGen,
                  ### pst ### definitions, progressions, parametersTP, currentFitness)
            ### pst ### tasksMutationStartProbability = parametersTP[0]
    #Update altered parameters (somente para [10] operatorsMutationStartProbability)
    ### pst ### df = pd.read_csv("input-parameters.csv", sep=";")
    ### pst ### parI = 0
    ### pst ### for name in names:
        ### pst ### df.at[islandNumber + parCount - 1, name] = parametersTP[parI]
        #print("changed", name, 'of island', islandNumber, 'to', parametersTP[parI])
        ### pst ### parI += 1
    ### pst ### df.to_csv("input-parameters.csv", sep=";", index= False)
    ### pst ### print("ISLAND: ", islandNumber, "finished with Simulated Annealing")
    cycle.postProcessing(population, alphabet)
    #plot.plot_evolution_per_island(fitnessEvolution, str(islandNumber), str(round), islandNumber)
    prevPlot = []
    with open('output-graphs/plotting/plotting_{0}.txt'.format(islandNumber), 'r') as plott:
        for line in isl.nonblank_lines(plott):
            prevPlot.append(literal_eval(line))
    plott.close()
    prevPlot.extend(fitnessEvolution)
    with open('output-graphs/plotting/plotting_{0}.txt'.format(islandNumber), 'w') as plott:
        for ini in range(len(prevPlot)):
            plott.write(str(prevPlot[ini]) + '\n')
    plott.close()
    islandEnd = datetime.now()
    islandDuration = islandEnd - islandStart
    record.record_evolution(sampledLog[2], sampledLog[0], str(parComb), str(islandNumber), str(round), par[islandNumber + parCount], islandNumber, highestValueAndPosition[0], fitnessEvolution, alphabet, population[highestValueAndPosition[1]], islandStart, islandEnd, islandDuration, currentGeneration)
    #pn.createPetriNet(population[highestValueAndPosition[1]], islandNumber, alphabet)
    print('Final results ==>', 'ISL:', islandNumber, '| ISL-DURANTION:', islandDuration, '| TF:', '%.10f' % highestValueAndPosition[0][0], '| C:', '%.10f' % highestValueAndPosition[0][1], '| TP:', '%.10f' % highestValueAndPosition[0][2], '| P:', '%.10f' % highestValueAndPosition[0][3], '| S:', '%.10f' % highestValueAndPosition[0][4], '| ALPHABET:', alphabet, '| BEST INDIVIDUAL:', population[highestValueAndPosition[1]])
    return

if __name__ == '__main__':
    par = []
    with open('input-parameters/input-parameters.csv', 'r') as parameters:
        for line in isl.nonblank_lines(parameters):
            par.append(line.split(';'))
    parameters.close()
    ### pst ### definitions = [['[8] tasksMutationStartProbability',0.001, 0, 0.1, "float"], ["[10] operatorsMutationStartProbability", 0.01, 0, 1, "float"], ['[32] migrationtime', 1, 1, 50, "int"], ['[34] percentageOfBestIndividualsForMigrationPerIsland', 0.1, 0, 1, "float"], ['[35] percentageOfIndividualsForMigrationPerIsland', 0.1, 0, 1, "float"]]
    globalStart = datetime.now()
    for logID in range(1):
        fullLog0 = adLog.importLog()
        alphabet = []
        logSizeAndMaxTraceSize = [0, float('inf'), 0]
        iniPop.createAlphabet(fullLog0, alphabet)
        iniPop.processLog(fullLog0, logSizeAndMaxTraceSize)
        sampledLog0 = []
        (sampledLog0, fullLog0) = adLog.sampleLog(sampledLog0, fullLog0)
        parCount = 1
        for parComb in range(numberOfParametersCombinations):
            num_islands = []
            for thread in range(numberOfThreads):
                num_islands.append(thread)
            isl.create_plotting_files(num_islands, numberOfThreads)
            p = multiprocessing.Pool(numberOfThreads)
            m = multiprocessing.Manager()
            broadcast = m.list()
            messenger = m.list()
            ### pst ### progressions = m.list()
            ### pst ### for i in range(numberOfThreads):
                ### pst ### progressions.append([['[8] tasksMutationStartProbability',0,0], ['[10] operatorsMutationStartProbability',0,0], ['[32] migrationtime',0,0], ['[34] percentageOfBestIndividualsForMigrationPerIsland',0,0], ['[35] percentageOfIndividualsForMigrationPerIsland',0,0]])
            islandSizes = m.list()
            percentageOfBestIndividualsForMigrationAllIslands = m.list()
            taskAddition = m.list()                                                                                     # Added [hiddenTasks]
            sampledLog = m.list()
            fullLog = m.list()
            func = partial(runRound, par, parComb, parCount, numberOfThreads)
            for round in range(numberOfRounds):
                for thread in range(numberOfThreads):
                    broadcast.append([])
                    messenger.append([[],[],[]])                                                                        # Era "messenger.append([])"  [hiddenTasks]
                    islandSizes.append(0)
                    percentageOfBestIndividualsForMigrationAllIslands.append(0)
                    taskAddition.append(0)                                                                              # Added [hiddenTasks]
                broadcast.append(1)
                taskAddition.append(0)                                                                                  # Added [hiddenTasks]
                taskAddition.append(numberOfThreads)
                sampledLog.append(sampledLog0)
                sampledLog.append(numberOfThreads)
                sampledLog.append(0)
                fullLog.append(fullLog0)
                func2 = partial(func, round, broadcast, messenger, islandSizes, percentageOfBestIndividualsForMigrationAllIslands, taskAddition, sampledLog, fullLog, alphabet)
                ### pst ### func2 = partial(func, round, broadcast, messenger, progressions, definitions, islandSizes, percentageOfBestIndividualsForMigrationAllIslands, taskAddition, sampledLog, fullLog, alphabet)         # New "taskAddition" [hiddenTasks]
                p.map(func2, num_islands)
                #plot.plot_evolution_integrated(str(round), numberOfThreads)
                globalEnd = datetime.now()
                globalDuration = globalEnd - globalStart
                print('Global Start:    ', globalStart)
                print('Global End:      ', globalEnd)
                print('Global Duration: ', globalDuration)
            p.close()
            parCount = parCount + numberOfThreads