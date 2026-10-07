from flask import Flask, render_template, request, redirect
import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


tasks = load_tasks()

print("TASKS FILE:", TASKS_FILE)
print("TASKS:", tasks)


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/tambah", methods=["POST"])
def tambah():
    nama = request.form["nama"]
    matkul = request.form["matkul"]
    deadline = request.form["deadline"]

    tasks.append({
        "nama": nama,
        "matkul": matkul,
        "deadline": deadline,
        "status": "Belum Dikerjakan"
    })

    save_tasks()

    return redirect("/")


@app.route("/status/<int:index>", methods=["POST"])
def ubah_status(index):
    if 0 <= index < len(tasks):

        if tasks[index]["status"] == "Belum Dikerjakan":
            tasks[index]["status"] = "Sedang Dikerjakan"

        elif tasks[index]["status"] == "Sedang Dikerjakan":
            tasks[index]["status"] = "Selesai"

        else:
            tasks[index]["status"] = "Belum Dikerjakan"

        save_tasks()

    return redirect("/")


@app.route("/hapus/<int:index>", methods=["POST"])
def hapus_tugas(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()

    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )