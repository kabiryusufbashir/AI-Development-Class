import json

report = {
    "model":"Fraud_detection",
    "accuracy":0.95,
}

with open("report.json", "w") as file:
    json.dump(report, file)

with open("report.json", "r") as file:
    loaded_report = json.load(file)
print(loaded_report)