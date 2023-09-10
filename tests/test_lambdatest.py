import allure
import pytest

from utils.converters import json_to_dict
from utils.file_utils import read_data_file


@allure.suite("Lambdatest API tests")
@allure.title("JSON to XML conversion")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_xml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_xml = read_data_file(f"xml/{file_name}.xml")
        mini_expected_xml = lambdatest_service.minify_xml(expected_xml)

    with allure.step("Convert JSON to XML via API"):
        actual_xml = lambdatest_service.json_to_xml(input_json)
        mini_actual_xml = lambdatest_service.minify_xml(actual_xml)

    with allure.step("Compare expected and actual XML"):
        assert mini_actual_xml == mini_expected_xml


@allure.suite("Lambdatest API tests")
@allure.title("Extract text from JSON")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-text")
@allure.link("https://jira.com/TEST-1234")
@allure.description(
    """
    This test case verifies that the API endpoint "Extract Text from JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from JSON via API.
    3. Compare expected and actual text.
"""
)
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_extract_text_from_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_text = read_data_file(f"txt/{file_name}.txt")

    with allure.step("Extract text from JSON via API"):
        actual_text = lambdatest_service.extract_text_from_json(input_json)

    with allure.step("Compare expected and actual text"):
        assert actual_text == expected_text


@allure.suite("Lambdatest API tests")
@allure.title("Validate YAML")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_validate_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")
        expected_text = "Valid YAML"

    with allure.step("Validate YAML via API"):
        actual_text = lambdatest_service.validate_yaml(input_yaml)

    with allure.step("Compare expected and actual text"):
        assert actual_text == expected_text


@allure.suite("Lambdatest API tests")
@allure.title("Validate YAML with invalid file")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_validate_yaml_invalid_input(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_file = read_data_file(f"xml/{file_name}.xml")
        expected_text = 'Unable to parse at line 1 (near "<?xml version="1.0"?>").'

    with allure.step("Validate YAML via API"):
        actual_text = lambdatest_service.validate_yaml(input_file)

    with allure.step("Compare expected and actual text"):
        assert actual_text == expected_text


@allure.suite("Lambdatest API tests")
@allure.title("Convert JSON to YAML")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert JSON to YAML via API"):
        actual_yaml = lambdatest_service.json_to_yaml(input_json)

    with allure.step("Compare expected and actual YAML"):
        assert actual_yaml == expected_yaml


@allure.suite("Lambdatest API tests")
@allure.title("YAML to JSON conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-to-json")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_yaml_to_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")
        expected_json = read_data_file(f"json/{file_name}.json")
        expected_dict = json_to_dict(expected_json)

    with allure.step("Convert YAML to JSON via API"):
        actual_dict = lambdatest_service.yaml_to_json(input_yaml)

    with allure.step("Compare expected and actual dict"):
        assert actual_dict == expected_dict


@allure.suite("Lambdatest API tests")
@allure.title("YAML to XML conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-to-xml")
def test_yaml_to_xml(lambdatest_service, file_name="2"):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")
        expected_xml = read_data_file(f"xml/{file_name}.xml")
        mini_expected_xml = lambdatest_service.minify_xml(expected_xml)

    with allure.step("Convert YAML to XML via API"):
        actual_xml = lambdatest_service.yaml_to_xml(input_yaml)
        mini_actual_xml = lambdatest_service.minify_xml(actual_xml)

    with allure.step("Compare expected and actual XML"):
        assert mini_actual_xml == mini_expected_xml


@pytest.mark.xfail(reason="Bug in the API")
@allure.suite("Lambdatest API tests")
@allure.title("XML to YAML conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/xml-to-yaml")
def test_xml_to_yaml(lambdatest_service, file_name="2"):
    with allure.step("Prepare test data"):
        input_xml = read_data_file(f"xml/{file_name}.xml")
        expected_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert XML to YAML via API"):
        actual_yaml = lambdatest_service.xml_to_yaml(input_xml)

    with allure.step("Compare expected and actual YAML"):
        assert actual_yaml == expected_yaml


@pytest.mark.xfail(reason="Bug in the API")
@allure.suite("Lambdatest API tests")
@allure.title("XML to YAML via YAML to XML conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/xml-to-yaml")
def test_xml_to_yaml_via_yaml_to_xml(lambdatest_service, file_name="2"):
    with allure.step("Prepare test data"):
        expected_xml = read_data_file(f"xml/{file_name}.xml")
        mini_expected_xml = lambdatest_service.minify_xml(expected_xml)
        expected_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert YAML to XML via API"):
        actual_xml = lambdatest_service.yaml_to_xml(expected_yaml)
        mini_actual_xml = lambdatest_service.minify_xml(actual_xml)

    with allure.step("Convert XML to YAML via API"):
        actual_yaml = lambdatest_service.xml_to_yaml(mini_actual_xml)

    with allure.step("Compare expected and actual YAML and XML"):
        assert mini_actual_xml == mini_expected_xml
        assert actual_yaml == expected_yaml
