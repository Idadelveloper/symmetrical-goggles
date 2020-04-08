def estimator(data):
    data = dict(data)
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * 2**(data['timeToElapse']//3)
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * 2**(data['timeToElapse']//3)
    severeCasesByRequestedTime = round((15/100) * severeImpact['infectionsByRequestedTime'])
    bedsByRequestedTime = round((35/100) * data['totalHospitalBeds'])
    severeImpact['hospitalBedsByRequestedTime'] = bedsByRequestedTime - severeCasesByRequestedTime
    severeImpact['casesForICUByRequestedTime'] = round((5/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['casesForVentilatorsByRequestedTime'] = round((2/100) * severeImpact['infectionsByRequestedTime'])
    severeImpact['dollarsInFlight'] = round(severeImpact['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])
    data = {'data': data, 
            'impact': impact, 
            'severeImpact': severeImpact}
    return data
