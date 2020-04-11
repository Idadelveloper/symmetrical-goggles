def timeToElapse(data):
    if data['periodType'] == 'days':
        return 2**(data['timeToElapse']//3)
    elif data['periodType'] == 'weeks':
         return 2**(data['timeToElapse']*7//3)
    elif data['periodType'] == 'months':
        return 2**(data['timeToElapse']*30//3)


def estimator(data):
    data = dict(data)
    impact = {}
    severeImpact = {}
    
    #CHALLENGE 1
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * timeToElapse(data)
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * timeToElapse(data)
    
    #CHALLENGE 2
    #Severe impact
    severeCasesByRequestedTime = int((15/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['severeCasesByRequestedTime'] =  severeCasesByRequestedTime
    bedsByRequestedTime = int((35/100) * data['totalHospitalBeds'])
    severeImpact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - severeCasesByRequestedTime
    #Impact
    impact['severeCasesByRequestedTime'] = int((15/100) * impact['infectionsByRequestedTime'])
    impact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - impact['severeCasesByRequestedTime']
    
    #CHALLENGE 3
    #Severe impact
    severeImpact['casesForICUByRequestedTime'] = int((5/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['casesForVentilatorsByRequestedTime'] = int((2/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['dollarsInFlight'] = int((severeImpact['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) // data['timeToElapse'])
    #Impact
    impact['casesForICUByRequestedTime'] = int((5/100) * impact['infectionsByRequestedTime'])
    impact['casesForVentilatorsByRequestedTime'] = int((2/100) * impact['infectionsByRequestedTime'])
    impact['dollarsInFlight'] = int((impact['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) // data['timeToElapse'])
    
    #Output Data
    data = {'data': data, 
            'impact': impact, 
            'severeImpact': severeImpact}
    return data
