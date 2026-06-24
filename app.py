from flask import Flask, request
import random

app = Flask(__name__)

travel_data = {
    "東區": {
        "spots": [
            {"name": "巴克禮紀念公園", "pet": True},
            {"name": "南紡購物中心", "pet": False},
            {"name": "平實公園", "pet": True},
            {"name": "成大榕園", "pet": True},
            {"name": "大東夜市", "pet": False},
            {"name": "德光公園", "pet": True},
            {"name": "崇學公園", "pet": True},
            {"name": "東區寵物友善咖啡廳", "pet": True}
        ],
        "veg_food": ["養聖齋蔬食", "小東路素食", "慈香庭", "菩提園素食"],
        "food": ["毛丼", "府城騷烤家", "丹丹漢堡", "小豪洲沙茶爐"],
        "souvenir": ["葡吉麵包", "鳳梨酥", "牛軋糖"]
    },
    "南區": {
        "spots": [
            {"name": "水交社文化園區", "pet": True},
            {"name": "竹溪寺", "pet": False},
            {"name": "竹溪水岸園區", "pet": True},
            {"name": "鹽埕天后宮", "pet": False},
            {"name": "新興園區", "pet": True},
            {"name": "南山公墓", "pet": True}
        ],
        "veg_food": ["天品素食", "慈蓮素食"],
        "food": ["周氏蝦捲", "丹丹漢堡", "牛肉湯"],
        "souvenir": ["依蕾特", "阿美麻糬"]
    },
    "中西區": {
        "spots": [
            {"name": "藍晒圖文創園區", "pet": True},
            {"name": "河樂廣場", "pet": True},
            {"name": "司法博物館", "pet": False},
            {"name": "美術館二館", "pet": False},
            {"name": "國華街", "pet": False},
            {"name": "神農街", "pet": True}
        ],
        "veg_food": ["赤崁璽樓蔬食", "清心緣"],
        "food": ["阿堂鹹粥", "度小月"],
        "souvenir": ["銀波布丁", "花生糖"]
    },
    "北區": {
        "spots": [
            {"name": "臺南公園", "pet": True},
            {"name": "321巷藝術聚落", "pet": True},
            {"name": "小北夜市", "pet": False},
            {"name": "開元寺", "pet": False},
            {"name": "勝安宮", "pet": False},
            {"name": "台南轉運站", "pet": True}
        ],
        "veg_food": ["天心岩蔬食", "慈香庭"],
        "food": ["阿輝炒鱔魚", "文章牛肉湯"],
        "souvenir": ["依蕾特", "花生糖"]
    },
    "安平區": {
        "spots": [
            {"name": "安平古堡", "pet": True},
            {"name": "安平樹屋", "pet": False},
            {"name": "安平老街", "pet": False},
            {"name": "漁光島", "pet": True},
            {"name": "觀夕平台", "pet": True},
            {"name": "林默娘公園", "pet": True},
            {"name": "安平港濱公園", "pet": True}
        ],
        "veg_food": ["妙緣素食", "慈香庭"],
        "food": ["周氏蝦捲", "豆花"],
        "souvenir": ["蝦餅", "蜜餞"]
    },
    "安南區": {
        "spots": [
            {"name": "台江國家公園", "pet": True},
            {"name": "四草綠色隧道", "pet": False},
            {"name": "鹿耳門聖母廟", "pet": False},
            {"name": "安順鹽田", "pet": True},
            {"name": "台江遊客中心", "pet": True}
        ],
        "veg_food": ["安南素食坊", "慈蓮素食"],
        "food": ["鱔魚意麵", "小籠包"],
        "souvenir": ["古早味蛋糕", "蜂蜜蛋糕"]
    }
}

def generate_plan(area, is_veg, people, with_pet):
    data = travel_data[area]

    spots = [s for s in data["spots"] if s["pet"]] if with_pet else data["spots"]

    if len(spots) < 4:
        return ["⚠️ 此區景點不足"]

    selected = random.sample(spots, 4)

    foods = data["veg_food"] if is_veg else data["food"]

    return [
        f"🌞 上午：{selected[0]['name']}、{selected[1]['name']}",
        f"🍱 午餐：{random.choice(foods)}",
        f"🌇 下午：{selected[2]['name']}、{selected[3]['name']}",
        f"🍽️ 晚餐：{random.choice(foods)}",
        f"🎁 伴手禮：{random.choice(data['souvenir'])}"
    ]


@app.route("/")
def home():
    return """
    <html>
    <head>
    <style>
    body {
        font-family: Arial;
        background: linear-gradient(135deg, #74ebd5, #ACB6E5);
        display:flex; justify-content:center; align-items:center;
        height:100vh;
    }
    .card {
        background:white; padding:30px; border-radius:15px;
        width:350px; box-shadow:0 10px 25px rgba(0,0,0,0.2);
    }
    select,input,button {
        width:100%; margin:8px 0; padding:10px;
        border-radius:8px;
    }
    button {background:#4CAF50;color:white;border:none;}
    </style>
    </head>

    <body>
    <div class="card">
    <h2>🌴 台南旅遊行程</h2>

    <form action="/result">
    區域：
    <select name="area">
    <option>東區</option><option>南區</option>
    <option>中西區</option><option>北區</option>
    <option>安平區</option><option>安南區</option>
    </select>

    是否吃素：
    <select name="veg">
    <option value="是">是</option>
    <option value="否">否</option>
    </select>

    是否帶寵物：
    <select name="pet">
    <option value="是">是</option>
    <option value="否">否</option>
    </select>

    <input name="people" placeholder="人數">
    <button type="submit">🚀 產生行程</button>
    </form>
    </div>
    </body>
    </html>
    """


@app.route("/result")
def result():
    area = request.args.get("area")
    is_veg = request.args.get("veg") == "是"
    with_pet = request.args.get("pet") == "是"
    people = request.args.get("people")

    plan = generate_plan(area, is_veg, people, with_pet)
    items = "".join(f"<li>{p}</li>" for p in plan)

    return f"""
    <html>
    <head>
    <style>
    body {{
        font-family: Arial;
        background: linear-gradient(135deg,#89f7fe,#66a6ff);
        display:flex; justify-content:center; align-items:center;
        height:100vh;
    }}
    .card {{
        background:white; padding:30px; border-radius:15px;
        width:400px; box-shadow:0 10px 25px rgba(0,0,0,0.2);
    }}
    a {{
        display:block; text-align:center; margin-top:20px;
        background:#4CAF50;color:white;padding:10px;border-radius:8px;
        text-decoration:none;
    }}
    </style>
    </head>

    <body>
    <div class="card">
    <h2>🎉 你的行程</h2>
    <ul>{items}</ul>
    <a href="/">⬅️ 返回</a>
    </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
