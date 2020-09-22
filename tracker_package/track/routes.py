from flask import jsonify, Blueprint, request
from tracker_package.src.tracker import Tracker

track = Blueprint('track', __name__)

@track.route("/track/<string:category>", methods=['POST'])
def track_category(category):
    if'?' in category:
        category = category[:category.index('?')]

    tr = Tracker(category)
    data = tr.track(dry_run=request.args.get("dry_run", False))
    d = [x.to_dict() for x in data]
    return jsonify(d)