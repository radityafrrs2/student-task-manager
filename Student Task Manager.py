from flask import Flask, render_template, request, redirect
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


tasks = []


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
        "status": "Belum Selesai"
    })

    return redirect("/")


@app.route("/status/<int:index>", methods=["POST"])
def ubah_status(index):
    if 0 <= index < len(tasks):

        if tasks[index]["status"] == "Belum Selesai":
            tasks[index]["status"] = "Selesai"
        else:
            tasks[index]["status"] = "Belum Selesai"

    return redirect("/")


@app.route("/hapus/<int:index>", methods=["POST"])
def hapus_tugas(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )