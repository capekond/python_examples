from jsonpath_ng import parse
data = {'service_response': {
    '@type': 'r7.pricing/com.eurex.r7.pricing.api.scenario_evaluation.v1.ScenarioEvaluationResponse',
    'snapshot_context': {'snapshot_type': 'SNAPSHOT_TYPE_EOD', 'business_date': {'year': 2013, 'month': 12, 'day': 18},
                         'snapshot_time': '1387407600000'}, 'scenarios': [
        {'instrument_id': {'unique_contract_id': '8'}, 'neutral_price': 3573.52, 'risk_measure_sets': [
            {'risk_measure_set': {'name': 'FILTERED_HISTORICAL_VAR_3', 'id': '9'},
             'scenario_prices': [4785.570335377332, 4398.993201039709, 4636.793655086512, 3956.559326162844,
                                 3285.386830841894, 3168.5599369778843, 2524.812801699998, 2933.8646500295436,
                                 2695.997765315578, 3051.5771104335545, 3371.2327202241136, 3421.315086321501,
                                 2632.0921563686165, 2597.3008669380447, 3337.2557882704823, 3976.2353686181,
                                 4807.81921635591, 4800.525408079911, 4598.245332062547, 4214.656306881945,
                                 3267.144637252521, 3814.987069242262, 2836.3978756923125, 2857.787011865568,
                                 3178.9786125996793, 4418.616308623485, 5106.975306295917, 4825.435289667737,
                                 4059.2316740733995, 3885.0681069048396, 3399.2824271361274, 3133.532215816194,
                                 3338.1086297784154, 4232.093416168042, 5569.532757036813, 5850.1636760091915,
                                 4430.2960952635785, 4772.56877210813, 4183.007032731029, 4210.411689554712,
                                 3240.431535423924, 3054.071071163128, 2978.4163546137784, 3867.122029805533,
                                 4349.711997830407, 4123.559882272144, 3388.4447786090864, 2709.878542596875,
                                 2642.418827518726, 2304.9121164622325, 2554.7826755003584]},
            {'risk_measure_set': {'name': 'SIMPLE_STRESS_VAR_3', 'id': '11'},
             'scenario_prices': [4586.8297740892285, 3934.5759185750835, 3792.320513473226, 3282.981831589014,
                                 3061.5830059835152, 3190.5844220335784, 4026.1802770373524, 4975.177778859007,
                                 5383.136002337203, 4131.126394015721, 4176.13887032719, 3805.6930034554816,
                                 3878.9174400808038, 3034.2646476095597, 2822.6413751548757, 2776.9719415877203,
                                 3554.5522445270185, 3999.862975531924, 3835.9959622090596, 3137.919825454588,
                                 2539.994979404569, 2520.4037436294047, 2369.6069663610733, 2544.69322997295,
                                 2408.085670866605, 2350.42251218881, 2401.244403450338]},
            {'risk_measure_set': {'name': 'FILTERED_HISTORICAL_VAR_3', 'id': '1'},
             'scenario_prices': [3871.0947739142666, 4300.619883515466, 4902.047889922581, 4101.475118652557,
                                 3831.909284508495, 3250.2774206137765, 3099.7728666975327, 2994.8746594678732,
                                 3136.015284175238, 2973.690058848735, 3198.7966702422773, 3822.5443935876488,
                                 3318.6298544461697, 1872.1731714144048, 2900.8853249850713, 3933.8566654034175]},
            {'risk_measure_set': {'name': 'SIMPLE_STRESS_VAR_3', 'id': '3'},
             'scenario_prices': [3135.3571919355286, 3807.2841156502072, 3344.309030622022, 2655.3835417130617,
                                 2972.9957200727467, 3948.2131300242263, 3977.1246339367635, 4222.824024771389,
                                 4879.496822552311, 3745.2677300583255]}]}]}}
columns = {'$.service_response.scenarios[0].instrument_id.unique_contract_id',
           '$.service_response.scenarios[0].neutral_price'}

row = {}
data_table = []
cols_names = set()
for column in columns:
    column_name = column[column.rindex(".") + 1:]
    cols_names.add(column_name)
    js = parse(column)
    for match in js.find(data):
        row[column_name] = match.value
        print(row)
data_table.append(row)
print(data_table)
print(cols_names)
