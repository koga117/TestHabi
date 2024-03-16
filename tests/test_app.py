import unittest
from app import app

class TestApp(unittest.TestCase):

    def test_get_inmuebles(self):
        response = app.test_client().get("/inmuebles")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
