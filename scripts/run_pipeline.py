import subprocess

def run():
    subprocess.run(["poetry", "run", "python", "data/collect.py"])
    subprocess.run(["poetry", "run", "python", "features/engineer.py"])
    subprocess.run(["poetry", "run", "python", "models/train.py"])

if __name__ == "__main__":
    run()
