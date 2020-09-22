import unittest
import requests
from tracker_package.src.models import Category, PlaylistTracker
from tracker_package import db, create_app

class TrackerTester(unittest.TestCase):
    TRACK_URI = "http://localhost:5000/track/{}"
    REMOVE_URI = "http://localhost:5000/entity/remove/{}"
    CREATE_URI = "http://localhost:5000/entity/create/{}"

    def setUp(self) -> None:
        app = create_app()
        app.app_context().push()


    def test_category_registration(self):
        requests.post(self.REMOVE_URI.format('indie'))
        response = requests.post(self.CREATE_URI.format('indie'))
        self.assertEqual("insert category successfully", response.json()['message'])

    def test_category_remove(self):
        requests.post(self.CREATE_URI.format('hiphop'))
        response = requests.post(self.REMOVE_URI.format('indie'))
        self.assertEqual("removed category successfully", response.json()['message'])

    def test_dry_run(self):
        total_rows = len(PlaylistTracker.query.all())
        response = requests.post(self.TRACK_URI.format('hiphop?dry_run=true'))
        self.assertEqual(total_rows, len(PlaylistTracker.query.all()))