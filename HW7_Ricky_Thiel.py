def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name
    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {machine: {"INFO": 0, "WARNING": 0, "Error":0} for machine in machines}
    
    with open("info.log", "w") as f_info, \
        open("warning.log", "w") as f_warn, \
        open("error.log", "w") as f_err:

        for machine, filename in sorted(machines.items()):
            try:
                with open(filename, "r") as f_log:
                    for line in f_log:
                        stripped = line.strip()
                        if not stripped:
                             pass

                        if "[INFO]" in stripped:
                            level = "INFO"
                            f_info.write(f"{machine} | {stripped}\n")
                        elif "[WARNING]" in stripped:
                            level = "ERROR"
                            if not stripped:
                                continue

                            if "[INFO]" in stripped:
                                level = "INFO"
                                f_info.write(f"{machine} | {stripped}\n")
                            elif "[WARNING]" in stripped:
                                level = "WARNING"
                                f_warn.write(f"{machine} | {stripped}\n")
                            elif "[ERROR]" in stripped:
                                level = "ERROR"
                                f_err.write(f"{machine} | {stripped}\n")
                            else:
                                continue

                            counts[machine][level] += 1
                        else: 
                            pass

                        counts[machine][level] += 1
            except FileNotFoundError:
                pass 
    return counts

def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("=" * 40)
    print("SYSTEM LOG STATUS REPORT")
    print("=" * 40)

    total_entries = 0
    total_info = 0
    total_warn = 0
    total_err = 0

    for machine in sorted(counts.keys()):
        info = counts[machine].get("INFO", 0)
        warn = counts[machine].get("WARNING", 0)
        err = counts[machine].get("ERROR", 0)
        total = info + warn + err

        total_entries += total
        total_info += info
        total_warn += warn
        total_err += err

        if err>= 2:
            status = "CRITICAL"
        elif err >= 1 or warn >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"
        print(f"{machine}: {total} entries (INFO: {info}, WARNING: {warn}, ERROR: {err}) - {status}")

    print("-" * 40)

    if total_err >= 2:
        tot_status = "CRITICAL"
    elif total_err >= 1 or total_warn >= 1:
        tot_status = "NEEDS ATTENTION"
    else: 
        tot_status = "OK"
    print(f"Total: {total_entries} entries (INFO: {total_info}, WARNING: {total_warn}, ERROR: {total_err}) - {tot_status}")
    print("-" * 40)

    try:
        with open(error_file, "r") as f:
            for line in f:
                print(f"  {line.rstrip()}")
    except FileNotFoundError:
        pass
# Test cases
def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name
    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {
        machine: {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for machine in machines
    }

    output_files = {
        "INFO": open("info.log", "w"),
        "WARNING": open("warning.log", "w"),
        "ERROR": open("error.log", "w"),
    }

    try:
        for machine, log_file in machines.items():
            with open(log_file, "r") as source:
                for line in source:
                    for level in counts[machine]:
                        if f"[{level}]" in line:
                            counts[machine][level] += 1
                            output_files[level].write(
                                f"{machine} | {line.strip()}\n"
                            )
                            break
    finally:
        for output_file in output_files.values():
            output_file.close()

    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("Security Status Report")
    for machine, levels in counts.items():
        print(
            f"{machine}: INFO={levels['INFO']}, "
            f"WARNING={levels['WARNING']}, ERROR={levels['ERROR']}"
        )

    try:
        with open(error_file, "r") as file:
            errors = file.read().strip()
        if errors:
            print("\nErrors:")
            print(errors)
    except FileNotFoundError:
        print(f"\nError log not found: {error_file}")

with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({
    "server_a": "server_a.log",
    "server_b": "server_b.log",
})
print(counts)

with open("warning.log", "r") as f:
    print(f.read())

print_report(counts)

import json
import pickle
import os
import csv

with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")

def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    with open(csv_file, "r", newline="", encoding="utf-8") as f:
        incidents = list(csv.DictReader(f))

    for incident in incidents:
        incident["id"] = int(incident["id"])

    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": [],
    }

    for incident in incidents:
        machine = incident.get("machine", "unknown")
        severity = str(incident.get("severity", "unknown")).lower()

        summary["by_machine"][machine] = summary["by_machine"].get(machine, 0) + 1
        summary["by_severity"][severity] = summary["by_severity"].get(severity, 0) + 1

        if severity == "high":
            summary["high_ids"].append(incident.get("id"))

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    return summary


def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)

    filenames = ["incidents.pkl"]
    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    machine_incidents = {}
    for incident in incidents:
        machine = incident.get("machine", "unknown")
        machine_incidents.setdefault(machine, []).append(incident)

    for machine, items in machine_incidents.items():
        filename = f"{machine}.json"
        with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)
        filenames.append(filename)

    return filenames


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)
# 5
incidents = load_incidents("incidents.csv")
print(incidents[0])
# {'id': 1, 'machine': 'server_a', 'severity': 'high', 'description': 'Account root locked'}
summary = save_summary(incidents, "summary.json")
print(summary)
# {'total': 5, 'by_machine': {'server_a': 2, 'server_b': 3},
# 'by_severity': {'high': 3, 'low': 1, 'medium': 1}, 'high_ids': [1, 2, 5]}
with open("summary.json", "r") as f:
    print(json.load(f) == summary)
# True
print(archive(incidents, "archive"))
# ['incidents.pkl', 'server_a.json', 'server_b.json']
with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])
# [1, 4]
restored = load_archive("archive")
print(restored == incidents)
