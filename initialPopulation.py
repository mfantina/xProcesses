import random as ran
import fitness as fitn
import copy

testCrom1 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
testCrom2 = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], #
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]
testCrom = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def getTaskID(task, alphabet):
    i = 0
    while alphabet[i] != task:
        i = i + 1
    return i

def createEmptyIndividualTask(numberOfTasks):                                                                           # era "(alphabet)" [hiddenTasks]
    task = [0 for _ in range((2 * numberOfTasks) + 3)]                                                                  # era "len(alphabet)" [hiddenTasks]
    return task

def createAuxiliaryCromossome(usedLog, alphabet):
    auxCrom = [createEmptyIndividualTask(len(alphabet)) for _ in range((2 * len(alphabet)) + 3)]                        # era "len(alphabet)" [hiddenTasks]
    for i in range(len(alphabet)):
        for j in range(len(usedLog)):
            for k in range(len(usedLog[j]) - 1):
                if usedLog[j][k] == alphabet[i]:
                    auxCrom[(i * 2)][(getTaskID(usedLog[j][k + 1], alphabet) * 2)] = 1
                    auxCrom[(i * 2)][(getTaskID(usedLog[j][k + 1], alphabet) * 2) + 1] = 1
                    auxCrom[(i * 2) + 1][(getTaskID(usedLog[j][k + 1], alphabet) * 2)] = 1
                    auxCrom[(i * 2) + 1][(getTaskID(usedLog[j][k + 1], alphabet) * 2) + 1] = 1
    enabledTasks = 0
    for j in range(len(auxCrom) - 2):
        for k in range(1, len(auxCrom[j]) - 1):
            if auxCrom[j][k] == 1:
                enabledTasks = enabledTasks + 1
    return (auxCrom, enabledTasks / 4)

def DMmeasures(t1, t2, log):
    l2l = 0 #the number of times that the substring "t1t2t1" occurs in a log.
    follows = 0 #the number of times that a task is directly followed by another one. That is, how often the substring "t1t2" occurs in a log.
    for i in range(len(log)):
        for j in range(len(log[i]) - 2):
            if (log[i][j] == t1) and (log[i][j + 1] == t2):
                follows = follows + 1
                if (log[i][j + 2] == t1):
                    l2l = l2l + 1
    return (l2l, follows)

def dependencyMeasure(t1, t2, log):
    dependencyMeasure = 0
    (l2l_t1_t2, follows_t1_t2) = DMmeasures(t1, t2, log)
    (l2l_t2_t1, follows_t2_t1) = DMmeasures(t2, t1, log)
    if (t1 == t2):
        dependencyMeasure = (follows_t1_t2 / (follows_t1_t2 + 1))
    else:
        if (t1 != t2):
            if (l2l_t1_t2 == 0):
                dependencyMeasure = ((follows_t1_t2 - follows_t2_t1) / (follows_t1_t2 + follows_t2_t1 + 1))
            else:
                if (l2l_t1_t2 > 0):
                    dependencyMeasure = ((l2l_t1_t2 + l2l_t2_t1) / (l2l_t1_t2 + l2l_t2_t1 + 1))
                else:
                    quit()
    return dependencyMeasure

def createInitialIndividual(auxCrom, alphabet, log):
    influenceControl = 2 #control the "influence" of the dependency measure in the probability of setting a causality relation. Higher values for p lead to the inference of fewer causality relations among the tasks in the event log, and vice-versa.
    for i in range(len(alphabet) - 1):
        for j in range(1, len(alphabet)):
            if ran.random() < pow(dependencyMeasure(alphabet[i], alphabet[j], log), influenceControl):
                if ran.random() < 0.5:
                    if ran.random() < 0.5:
                        auxCrom[(i * 2)][(j * 2)] = 1
                    else:
                        auxCrom[(i * 2)][(j * 2) + 1] = 1
                else:
                    if ran.random() < 0.5:
                        auxCrom[(i * 2) + 1][(j * 2)] = 1
                    else:
                        auxCrom[(i * 2) + 1][(j * 2) + 1] = 1
    for i in range(len(alphabet)):
        if ran.random() < 0.5:
            auxCrom[i * 2][-3] = 1
        if ran.random() < 0.5:
            auxCrom[i * 2][-2] = 1
        if ran.random() < 0.5:
            auxCrom[i * 2][-1] = 1
        if ran.random() < 0.5:
            auxCrom[-3][i * 2] = 1
        if ran.random() < 0.5:
            auxCrom[-2][i * 2] = 1
        if ran.random() < 0.5:
            auxCrom[-1][i * 2] = 1
    return auxCrom

def initializeIndividual(numberOfTasks):                                                                                # era "alphabet" [hiddenTasks]
    individual = [createEmptyIndividualTask(numberOfTasks) for _ in range((2 * numberOfTasks) + 3)]                     # era "alphabet / len(alphabet)" [hiddenTasks]
    return individual

def createAlphabet(log, alphabet):
    k = 0
    for i in range(len(log)):
        for j in range(len(log[i])):
            if alphabet.count(log[i][j]) == 0:
                alphabet.append(log[i][j])
            k = k + 1
    alphabet.sort()
    alphabet.insert(0,'Begin')
    alphabet.append('End')
    return

def processLog(log, logSizeAndMaxTraceSize):
    for i in range(len(log)):
        log[i].insert(0,'Begin')
        log[i].append('End')
        if logSizeAndMaxTraceSize[1] > len(log[i]):
            logSizeAndMaxTraceSize[1] = len(log[i])
        if logSizeAndMaxTraceSize[2] < len(log[i]):
            logSizeAndMaxTraceSize[2] = len(log[i])
    logSizeAndMaxTraceSize[0] = len(log)
    return logSizeAndMaxTraceSize

def addRandomTransitions(newIndividual):                                                                                # added [hiddenTasks]
    for i in range(len(newIndividual) - 3):
        if ran.random() < 0.025:
            newIndividual[i][-5] = 1
        if ran.random() < 0.025:
            newIndividual[i][-4] = 1
        if ran.random() < 0.025:
            newIndividual[-5][i] = 1
        if ran.random() < 0.025:
            newIndividual[-4][i] = 1
    return

def updateReferenceCromossomeWithHiddenTask(referenceCromossome):                                                       # added [hiddenTasks]
    newReferenceCromossome = [createEmptyIndividualTask(int(((len(referenceCromossome) - 3) / 2) + 1)) for _ in range(len(referenceCromossome) + 2)]
    for j in range(len(referenceCromossome[0])):
        if j < (len(referenceCromossome[0]) - 3):
            l = j
        else:
            l = j + 2
        for k in range(len(referenceCromossome[0])):
            if k < (len(referenceCromossome[0]) - 3):
                newReferenceCromossome[l][k] = copy.deepcopy(referenceCromossome[j][k])
            else:
                newReferenceCromossome[l][k + 2] = copy.deepcopy(referenceCromossome[j][k])
    return newReferenceCromossome

def addHiddenTask(population, population_size):                                                                         # added [hiddenTasks]
    newPopulation = [initializeIndividual(int(((len(population[0]) - 3) / 2) + 1)) for _ in range(population_size)]
    for i in range(len(population)):
        for j in range(len(population[i][0])):
            if j < (len(population[i][0]) - 3):
                l = j
            else:
                l = j + 2
            for k in range(len(population[i][0])):
                if k < (len(population[i][0]) - 3):
                    newPopulation[i][l][k] = copy.deepcopy(population[i][j][k])
                else:
                    newPopulation[i][l][k + 2] = copy.deepcopy(population[i][j][k])
        addRandomTransitions(newPopulation[i])
    return newPopulation

def initializePopulation(population_size, TPweight, precisenessWeight, simplicityWeight, evaluatePrecisenesscompletenessWeight, completenessAttemptFactor1, completenessAttemptFactor2, selectionOp, alphabet, log, numberOfHiddenTask):    # added "numberOfHiddenTask" [hiddenTasks]
    population = [initializeIndividual(len(alphabet)) for _ in range(population_size)]                                  # era "alphabet" [hiddenTasks]
    (referenceCromossome, averageEnabledTasks) = createAuxiliaryCromossome(log, alphabet)
    for i in range(len(population)):                                                                                    # era "len(population) - 1" [hiddenTasks]
        population[i] = createInitialIndividual(population[i], alphabet, log)
    #for i in range(len(population)): #usado para teste com uma população inicial específica
    #    population[i] = copy.deepcopy(testCrom)
    return (population, fitn.evaluationPopulation(population, referenceCromossome, TPweight, precisenessWeight, simplicityWeight, evaluatePrecisenesscompletenessWeight, completenessAttemptFactor1, completenessAttemptFactor2, selectionOp, alphabet, log, numberOfHiddenTask), referenceCromossome, averageEnabledTasks)    # added "numberOfHiddenTask" [hiddenTasks]     