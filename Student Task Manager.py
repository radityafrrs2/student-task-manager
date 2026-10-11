
from flask import Flask, render_template, request, redirect, url_for
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")

DAFTAR_STATUS = [
    "Belum Dikerjakan",
    "Sedang Dikerjakan",
    "Selesai"
]


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


tasks = load_tasks()


@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    status_filter = request.args.get("status", "").strip()

    if status_filter not in DAFTAR_STATUS:
        status_filter = ""

    # Statistik dihitung dari seluruh tugas
    statistik = {
        "total": len(tasks),
        "belum": sum(
            1 for task in tasks
            if task.get("status") == "Belum Dikerjakan"
        ),
        "sedang": sum(
            1 for task in tasks
            if task.get("status") == "Sedang Dikerjakan"
        ),
        "selesai": sum(
            1 for task in tasks
            if task.get("status") == "Selesai"
        )
    }

    # Gabungkan pencarian nama dan filter status
    displayed_tasks = []

    for index, task in enumerate(tasks):
        nama_tugas = str(task.get("nama", ""))
        status_tugas = task.get(
            "status", "Belum Dikerjakan"
        )

        cocok_nama = query.casefold() in nama_tugas.casefold()
        cocok_status = (
            not status_filter or status_tugas == status_filter
        )

        if cocok_nama and cocok_status:
            displayed_tasks.append({
                "task": task,
                "index": index
            })

    return render_template(
        "index.html",
        tasks=tasks,
        displayed_tasks=displayed_tasks,
        statistik=statistik,
        query=query,
        status_filter=status_filter,
        daftar_status=DAFTAR_STATUS
    )


@app.route("/tambah", methods=["POST"])
def tambah():
    nama = request.form.get("nama", "").strip()
    matkul = request.form.get("matkul", "").strip()
    deadline = request.form.get("deadline", "").strip()

    if nama and matkul and deadline:
        tasks.append({
            "nama": nama,
            "matkul": matkul,
            "deadline": deadline,
            "status": "Belum Dikerjakan"
        })

        save_tasks()

    return redirect(url_for("home"))


def redirect_ke_daftar(query, status_filter):
    parameter = {}

    if query:
        parameter["q"] = query

    if status_filter in DAFTAR_STATUS:
        parameter["status"] = status_filter

    return redirect(url_for("home", **parameter))


@app.route("/status/<int:index>", methods=["POST"])
def ubah_status(index):
    if 0 <= index < len(tasks):
        status = tasks[index].get(
            "status", "Belum Dikerjakan"
        )

        if status == "Belum Dikerjakan":
            tasks[index]["status"] = "Sedang Dikerjakan"
        elif status == "Sedang Dikerjakan":
            tasks[index]["status"] = "Selesai"
        else:
            tasks[index]["status"] = "Belum Dikerjakan"

        save_tasks()

    query = request.form.get("q", "").strip()
    status_filter = request.form.get("status", "").strip()

    return redirect_ke_daftar(query, status_filter)


@app.route("/hapus/<int:index>", methods=["POST"])
def hapus_tugas(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()

    query = request.form.get("q", "").strip()
    status_filter = request.form.get("status", "").strip()

    return redirect_ke_daftar(query, status_filter)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
