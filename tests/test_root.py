import falcon

from . import base


class TestRoot(base.TestBase):
    def setUp(self):
        super(TestRoot, self).setUp()
        self.entry_path = "/"

    def tearDown(self):
        super(TestRoot, self).tearDown()

    def test_get_returns_200_and_message(self):
        body = self.simulate_get(self.entry_path)
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.assertIn("message", body)

    def test_wrong_method_returns_405(self):
        self.simulate_post(self.entry_path)
        self.assertEqual(self.srmock.status, falcon.HTTP_405)


class TestRootName(base.TestBase):
    def setUp(self):
        super(TestRootName, self).setUp()
        self.entry_path = "/"

    def tearDown(self):
        super(TestRootName, self).tearDown()

    def test_post_returns_200_and_name(self):
        body = self.simulate_post(self.entry_path + "Bob")
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.assertIn("Bob", body["message"])

    def test_wrong_method_returns_405(self):
        self.simulate_put(self.entry_path + "Bob")
        self.assertEqual(self.srmock.status, falcon.HTTP_405)
