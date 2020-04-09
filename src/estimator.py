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
    severeCasesByRequestedTime = round((15/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['severeCasesByRequestedTime'] =  severeCasesByRequestedTime
    bedsByRequestedTime = round((35/100) * data['totalHospitalBeds'])
    severeImpact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - severeCasesByRequestedTime
    #Impact
    impact['severeCasesByRequestedTime'] = round((15/100) * impact['infectionsByRequestedTime'])
    impact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - impact['severeCasesByRequestedTime']
    
    #CHALLENGE 3
    #Severe impact
    severeImpact['casesForICUByRequestedTime'] = round((5/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['casesForVentilatorsByRequestedTime'] = round((2/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['dollarsInFlight'] = round(severeImpact['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'], 2)
    #Impact
    impact['casesForICUByRequestedTime'] = round((5/100) * impact['infectionsByRequestedTime'])
    impact['casesForVentilatorsByRequestedTime'] = round((2/100) * impact['infectionsByRequestedTime'])
    impact['dollarsInFlight'] = round(impact['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'], 2)
    
    #Output Data
    data = {'data': data, 
            'impact': impact, 
            'severeImpact': severeImpact}
    return data
