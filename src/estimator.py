def estimator(data):
    output = {'data':data, 'impact': {}, 'severeImpact': {}}
    output['impact']['currentlyInfected'] = data['reportedCases'] * 10
    output['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50
    if data['periodType'] == 'weeks':
        data['timeToElapse'] = data['timeToElapse'] * 7
    elif data['periodType'] == 'months':
        data['timeToElapse'] = data['timeToElapse'] * 30
    output['impact']['infectionsByRequestedTime'] = output['impact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    output['severeImpact']['infectionsByRequestedTime'] = output['severeImpact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    output['impact']['severeCasesByRequestedTime'] = int(15/100 * (output['impact']['infectionsByRequestedTime']))
    output['severeImpact']['severeCasesByRequestedTime'] = int(15/100 * (output['severeImpact']['infectionsByRequestedTime']))
    output['impact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['impact']['severeCasesByRequestedTime'])
    output['severeImpact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['severeImpact']['severeCasesByRequestedTime'])
    output['impact']['casesForICUByRequestedTime'] = int(5/100 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForICUByRequestedTime'] = int(5/100 * output['severeImpact']['infectionsByRequestedTime'])
    output['impact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['severeImpact']['infectionsByRequestedTime'])
    output['impact']['dollarsInFlight'] = int((output['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']) /data['timeToElapse'])
    output['severeImpact']['dollarsInFlight'] = int((output['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'])/data['timeToElapse'])
    return output

