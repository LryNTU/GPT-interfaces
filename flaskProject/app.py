from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)

# 配置设置
app.config['SECRET_KEY'] = "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"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            r = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": request.form.get("question")
                    }
                ]
            )
            print(r)
            result = r.choices[0].message['content']  # 提取回答内容
            return render_template("index.html", result=result)
        except openai.error.OpenAIError as e:
            print("OpenAI API request error:", e)
    else:
        return render_template("index.html", result="waiting")


if __name__ == "__main__":
    app.run(port=5001)
