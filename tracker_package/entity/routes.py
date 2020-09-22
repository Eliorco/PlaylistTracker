from flask import Blueprint, jsonify
from tracker_package.src.models import Category
from tracker_package import db


entity = Blueprint('entity', __name__)


@entity.route("/entity/create/<string:category>", methods=['POST'])
def create_cat(category):
    status = "ok"
    cat = Category.query.filter_by(name=category).first()
    if not cat:
        try:
            cat = Category(name=category)
            db.session.add(cat)
            db.session.commit()
            msg = "insert category successfully"
        except Exception as e:
            status = "error"
            msg = e
    else:
        msg = "category already exist."

    return jsonify(status=status,
                   message=msg)


@entity.route("/entity/remove/<string:category>", methods=['POST'])
def remove_cat(category):
    status = "ok"
    cat = Category.query.filter_by(name=category).first()
    if cat:
        try:
            db.session.delete(cat)
            db.session.commit()
            msg = "removed category successfully"
        except Exception as e:
            status = "error"
            msg = e
    else:
        msg = "category doesn't exist"

    return jsonify(status=status,
                   message=msg)
