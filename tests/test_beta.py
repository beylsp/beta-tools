from urllib import urlopen
from flask_app import create_app
from flask_betatools.test import LiveServerTestCase


class TestLiveServer(LiveServerTestCase):
    def create_app(self):
        return create_app()

    def test_server_process_is_spawned(self):
        thread = self.server_thread

        self.assertNotEqual(thread, None)
        self.assertTrue(thread.is_alive())

    def test_server_process_listening(self):
        response = urlopen(self.live_server_url)
        self.assertTrue(b'OK' in response.read())
        self.assertEqual(response.code, 200)
