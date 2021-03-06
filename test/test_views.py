import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data


    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{"msg": "Hello World!", "name": "Ola"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEquals('<greetings> <name>Ola</name> <msg>Hello World!</msg> </greetings>', rv.data)

    def test_msg_with_output_name(self):
        rv = self.app.get('/?name=apolonia&output=json')
        self.assertEquals('{"msg": "Hello World!", "name": "apolonia"}', rv.data)
