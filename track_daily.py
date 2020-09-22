from tracker_package.src.models import Category, PlaylistTracker
from tracker_package import db, create_app
import requests
app = create_app()
app.app_context().push()

TRACK_URI = "http://localhost:5000/track/{}"
REMOVE_URI = "http://localhost:5000/entity/remove/{}"
CREATE_URI = "http://localhost:5000/entity/create/{}"

if __name__ == '__main__':
    categories = Category.query.all()
    for _, category in enumerate(categories):
        requests.post(TRACK_URI.format(category.name))