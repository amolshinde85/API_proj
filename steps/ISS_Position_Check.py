# Step definitions for verifying one time platform setup.
import json
import API_Calls, steps.common
from behave import given, when, then


@given(u"the user queried for TLE data for a satellite {id}")
def step_check_query_satellite(context, id):
    context.resp = context.api.call_rest_api(id + '/tles', 'GET')


@then(u"the TLE identifier data matches with {name}, {id}, {header}")
def step_check_identifiers_valid_satellite(context, name, id, header):
    resp_entry = json.loads(context.resp.text)
    # Assert the response body with the desired values
    print("<<====================  Assertions ====================>> ")
    print("Assert name in response body expected =>> " + name + " Actual =>>" + resp_entry['name'])
    assert (name == resp_entry['name'])
    print("Assert id in response body expected =>> " + id + " Actual =>>" + resp_entry['id'])
    assert (id == resp_entry['id'])
    print("Assert header in response body expected =>> " + header + " Actual =>>" + resp_entry['header'])
    assert (header == resp_entry['header'])
    context.resp = resp_entry


@then("other TLE data values are verified for {id}, {sub_id}")
def step_check_valid_satellite_tle_data(context, id, sub_id):
    # Convert date now to timestamp
    timestamp_now = API_Calls.API.datetime_to_timestamp()
    # Assert timestamp matches with the today's date time
    print("Assert requested timestamp in response body expected =>> " + str(timestamp_now) + " Actual =>>" + str(
        context.resp['requested_timestamp']))
    assert (str(context.resp['requested_timestamp']) in str(timestamp_now))

    # Storing data returned by line1 in a list
    line1_list = context.resp['line1'].split(" ")
    # Removing blank spaces
    line1_list = API_Calls.API.remove_empty_element_from_list(line1_list)
    print("<===================  Assert line data ==============>")
    print("Assert requested line 1 id + U  =>> " + str(id) + "U" + " Actual =>>" + str(
        line1_list[1]))
    assert (str(id) + "U" == line1_list[1])
    print("Assert requested Sub id =>> " + str(sub_id) + " Actual =>>" + str(
        line1_list[2]))
    assert (sub_id == line1_list[2])
    print("Assert value at position 5 =>> 00000-0" + " Actual =>>" + str(
        line1_list[5]))
    assert ("00000-0" == line1_list[5])
    print("Assert value at position 6 =>> 39053-4" + " Actual =>>" + str(
        line1_list[6]))
    assert ("39053-4" == line1_list[6])
    print("Assert value at position 7 =>> 0" + " Actual =>>" + str(
        line1_list[7]))
    assert ("0" == line1_list[7])
    print("Assert value at position 8 =>> 9999" + " Actual =>>" + str(
        line1_list[8]))
    assert ("9999" == line1_list[8])
    # resp_dict = json.dumps(context.resp['line1'])
    # context.resp = json.loads(resp_dict)
    # print(context.resp[3])

    # # Assert timestamp matches with the today's date time
    # time_now = datetime.now()
    # tle_to_date = timestamp_to_datetime(context.resp['tle_timestamp'])
    # print("Assert tle timestamp in response body expected =>> " + str(time_now) + " Actual =>>" + str(tle_to_date))
    # assert (time_now in str(tle_to_date))


@then("the response body has {error}, {status}")
def step_check_invalid_satellite_data(context, error, status):
    resp_entry = json.loads(context.resp.text)
    resp_error = resp_entry['error']
    resp_status_code = resp_entry['status']
    print("<===================  Assert line data ==============>")
    print("Assert response Error, Expected  =>> " + str(error) + " Actual =>>" + str(resp_error))
    assert (str(error) == str(resp_error))
    print("Assert Status Code, Expected  =>> " + str(status) + " Actual =>>" + str(resp_status_code))
    assert (str(status) == str(resp_status_code))


@given(u"the user queried for the satellite position using {id}")
def step_check_query_satellite_position_now(context, id):
    timestamp_now = API_Calls.API.datetime_to_timestamp()
    context.resp = context.api.call_rest_api(str(id) + '/positions?timestamps=' + str(timestamp_now), 'GET')


@then("the satellite position values are returned {name}, {id}, {unit}")
def step_check_valid_satellite_position_data(context, name, id, unit):
    resp_entry = json.loads(context.resp.text)
    resp_name = resp_entry[0]['name']
    resp_id = resp_entry[0]['id']
    resp_units = resp_entry[0]['units']

    print("<===================  Assert satellite position data ==============>")
    print("Assert response Name, Expected  =>> " + str(name) + " Actual =>>" + str(resp_name))
    assert (str(name) == resp_name)
    print("Assert response Id, Expected  =>> " + str(id) + " Actual =>>" + str(resp_id))
    assert (str(id) == str(resp_id))
    print("Assert response unit, Expected  =>> " + str(unit) + " Actual =>>" + str(resp_units))
    assert (str(unit) == str(resp_units))
