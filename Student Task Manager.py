from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
    app.run(debug=True)