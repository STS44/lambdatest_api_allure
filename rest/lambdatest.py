import allure
import requests


class LambdatestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    @allure.step("Send a POST request to {endpoint}")
    def _send_request(self, endpoint, input_key, input_str):
        url = self.BASE_URL + endpoint
        allure.attach(url, "Full URL", allure.attachment_type.TEXT)
        return requests.post(url, data={input_key: input_str})

    @allure.step("Send a POST request to convert JSON to XML")
    def json_to_xml(self, input_str: str) -> str:
        response = self._send_request("json-to-xml", "input-str", input_str).text

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output XML", allure.attachment_type.XML)

        return response

    @allure.step("Send a POST request to minify XML")
    def minify_xml(self, input_str: str) -> str:
        response = self._send_request("minify-xml", "input-str", input_str).json()[
            "minify_data"
        ]

        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Minified XML", allure.attachment_type.XML)

        return response

    @allure.step("Send a POST request to Extract Text from JSON")
    def extract_text_from_json(self, input_str: str) -> str:
        response = self._send_request(
            "extract-text-json", "input-str", input_str
        ).json()["data"]

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Extracted Text", allure.attachment_type.TEXT)

        return response

    @allure.step("Send a POST request to Validate YAML")
    def validate_yaml(self, yaml_str: str) -> str:
        response = self._send_request("yaml-validator", "yaml-str", yaml_str).json()[
            "message"
        ]

        allure.attach(yaml_str, "Input YAML", allure.attachment_type.YAML)
        allure.attach(response, "Verified YAML", allure.attachment_type.TEXT)

        return response

    @allure.step("Send a POST request to convert JSON to YAML")
    def json_to_yaml(self, json_str: str) -> str:
        response = self._send_request("json-to-yaml", "json-str", json_str).json()[
            "data"
        ]

        allure.attach(json_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)

        return response

    @allure.step("Send a POST request to convert YAML to JSON")
    def yaml_to_json(self, yaml_str: str) -> str:
        response = self._send_request("yaml-to-json", "yaml-str", yaml_str).json()[
            "data"
        ]

        return response

    @allure.step("Send a POST request to convert YAML to XML")
    def yaml_to_xml(self, yaml_str: str) -> str:
        response = self._send_request("yaml-to-xml", "yaml-str", yaml_str).json()[
            "data"
        ]

        allure.attach(yaml_str, "Input YAML", allure.attachment_type.YAML)
        allure.attach(response, "Output XML", allure.attachment_type.XML)

        return response

    @allure.step("Send a POST request to convert XML to YAML")
    def xml_to_yaml(self, xml_str: str) -> str:
        response = self._send_request("xml-to-yaml", "xml-str", xml_str).json()["data"]

        allure.attach(xml_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)

        return response
