from flask import Blueprint, request, jsonify
from agents.news_agent import get_news_agent

news_bp = Blueprint('news', __name__)
news_agent = get_news_agent()

@news_bp.route("/news", methods=["POST"])
def handle_news_query():
    try:
        data = request.get_json()
        query = data.get("query")

        if not query:
            return jsonify({"error": "Missing query field"}), 400

        result = news_agent.invoke({"input": query})
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
