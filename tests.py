from django.http import response
from django.test import SimpleTestCase

# Create your tests here.

class TestNearHundred(SimpleTestCase):
    def test_90(self):
        response = self.client.get("/near-hundred/90")
        self.assertContains(response, True)

class TestStringSplosion(SimpleTestCase):
    def test_abc(self):
        response = self.client.get("/string-splosion/abc")
        self.assertContains(response, "aababc")

class TestLoneSum(SimpleTestCase):
    def test_3_3_2(self):
        response = self.client.get("/lone-sum/3/3/2")
        self.assertContains(response, 2)
        
