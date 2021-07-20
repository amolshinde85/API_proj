# Step definitions for common features.
from behave import When


@When(u'the response status code is {code:d}')
def step_get_response_code(context, code):
    print("<<====================  Assertion ====================>> ")
    print(
        "Assert name in response body Expected =>> " + str(code) + " Actual =>>" + str(context.api.last_response_code))
    assert (code == context.api.last_response_code)
