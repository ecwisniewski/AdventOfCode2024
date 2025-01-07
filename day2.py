
test_reports = ["12 10 13 16 19 21 22",
                "1 2 7 8 9",
                "9 7 6 2 1",
                "1 3 2 4 5",
                "8 6 4 4 1",
                "1 3 6 7 9"]


def generate_test():
    r = []
    for t in test_reports:
        r.append(t.split())
    return r


def generate_reports_list():
    rep = []
    f = open("reports.txt", "r")
    for i in f:
        rep.append(i.split())
    return rep


def do_check(report,iteration):
    safe = True
    check = True
    for j in range(iteration, len(report)):
        r = report.copy()
        r.pop(j)
        if is_it_safe(r, False):
            check = True
            safe = True
            break
        else:
            check = False
    if not check:
        safe = False

    return safe


def is_it_safe(report,dampener=True):
    safe = True
    decreasing = None
    # All Levels either increasing or decreasing
    for i in range(0, len(report) - 1):
        t = decreasing
        v1 = int(report[i])
        v2 = int(report[i + 1])
        decreasing = v1 > v2
        if t is not None and t is not decreasing:
            safe = False
            break
        elif not (abs(v1 - v2) != 0 and abs(v1 - v2) <= 3):
            safe = False
            break

    # Dampner check
    if not safe and dampener:
        safe = do_check(report,0)

    return safe


def run_day2_answers():
    reports = generate_reports_list()

    count = 0
    for t in range(0, len(reports)):
        #print()
        if is_it_safe(reports[t]):
            count += 1
    print(count)
