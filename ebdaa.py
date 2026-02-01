import subprocess
import os

PROJECT_PATH = "/home/taqieldein/ebdaa"
COUNTER_FILE = "counter.txt"

# لو ملف العداد مش موجود، أنشئه وابدأ من 1
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        f.write("1")

# قراءة العداد الحالي
with open(COUNTER_FILE, "r") as f:
    counter = int(f.read().strip())

commit_message = f"counter {counter}"

# تنفيذ أوامر git
subprocess.run(["git", "add", PROJECT_PATH])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "-u", "origin", "main"])

# زيادة العداد وحفظه
with open(COUNTER_FILE, "w") as f:
    f.write(str(counter + 1))

print(f"Done ✔ Commit message: {commit_message}")
