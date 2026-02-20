from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Page principale
@app.route("/")
def home():
    return render_template("index.html")

# API Chatbot
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    # ⚡ هنا تحط منطق الشات بوت تاعك (RAG / LLM / rules...)
    response = generate_response(question)

    return jsonify({"answer": response})


def generate_response(question):
    # مثال بسيط (بدلها بالـ RAG تاعك)
    if "salem" in question.lower():
        return "Wa alikoum salam 👋"
    elif "merci" in question.lower():
        return "Avec plaisir 😊"
    else:
        return "هذا رد تجريبي من الشات بوت 🤖"


if __name__ == "__main__":
    app.run(debug=True)
