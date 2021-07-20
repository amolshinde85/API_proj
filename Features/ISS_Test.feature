@ISS_Position_Check
Feature: Verify user gets the TLE data in json or text format
  As an user,
  I want to GET the TLE data in JSON or TXT format via REST API,
  So that correct system behaviour is assured

  Scenario Outline: Verify satellite not found error for invalid satellite id's - NegativePath
    Given the user queried for TLE data for a satellite <id>
    When the response status code is 404
    Then the response body has <error>, <status>
    Examples:
      | id    | error               | status |
      | 25520 | satellite not found | 404    |
      | ab    | satellite not found | 404    |

  Scenario Outline: Verify the TLE data is returned in JSON format - HappyPath
    Given the user queried for TLE data for a satellite <id>
    When the response status code is 200
    Then the TLE identifier data matches with <name>, <id>, <header>
    And other TLE data values are verified for <id>, <sub_id>
    Examples:
      | name | id    | header      | sub_id |
      | iss  | 25544 | ISS (ZARYA) | 98067A |

  Scenario Outline: Verify the satellite position api returns the desired data for current timestamp - HappyPath
    Given the user queried for the satellite position using <id>
    When the response status code is 200
    Then the satellite position values are returned <name>, <id>, <Units>
    Examples:
      | name | id    | Units      |
      | iss  | 25544 | kilometers |
