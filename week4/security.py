logs = [("user1", "success"), ("user2", "failed"), ("user2", "failed"), ("user2", "failed")]
fails = {}
for name, status in logs:
    if status == "failed":
        fails[name] = fails.get(name, 0) + 1
for name in fails:
    if fails[name] >= 3:
        print("ALERT: LOCKOUT FOR", name)
