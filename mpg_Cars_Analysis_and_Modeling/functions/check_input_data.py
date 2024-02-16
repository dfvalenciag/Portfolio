def origin_verify(input_data):
    if input_data['origin'] == 1:
        input_data['origin_1'] = input_data.pop('origin')
        input_data['origin_2'] = 0
        input_data['origin_3'] = 0
    elif input_data['origin'] == 2:
        input_data['origin_1'] = 0
        input_data['origin_2'] = input_data.pop('origin')
        input_data['origin_2'] = 1
        input_data['origin_3'] = 0
    else:
        input_data['origin_1'] = 0
        input_data['origin_2'] = 0
        input_data['origin_3'] = input_data.pop('origin')
        input_data['origin_3'] = 1
    return input_data