student = {"key": ["playerName", "teamName"], "value": ["schoolName", "favoriteSport"]}
student_test = dict.fromkeys(student["key"], student["value"])
print(student_test)
