import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestEmailAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_urgent_triage(self):
        email = {"sender": "client@enterprise.com", "subject": "Critical Outage: API Down", "body": "Our server is throwing error 500!"}
        res = self.client.post("/triage", json=email)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["priority_level"], "P1_HIGH")
        self.assertEqual(res.json()["category"], "URGENT_SUPPORT")

if __name__ == "__main__":
    unittest.main()
