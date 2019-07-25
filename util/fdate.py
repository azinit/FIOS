from datetime import datetime
"""
..............................................................................................................
................................................ METHODS SUMMARY .............................................
..............................................................................................................
"""
# TODO: rewrite!
# def to_time(h, m, s):
#     """ Convert (h, m, s) format to datetime type """
#     return datetime.time(h, m, s)
#
#
# def to_hms(s):
#     """ Convert to (h, m, s) format """
#     s = to_seconds(s) if isinstance(s, datetime.datetime) else s
#     return [s // 3600, s // 60 % 60, s % 60]
#
#
# def to_seconds(time):
#     """ Convert any time type to seconds """
#     if isinstance(time, str):
#         cur = datetime.datetime.strptime(time, '%H:%M:%S')
#     elif isinstance(time, list):
#         cur = to_time(time[0], time[1], time[2])
#     elif isinstance(time, datetime.datetime):
#         cur = time
#     else:       # condition
#         cur = time
#     return int(cur.hour) * 3600 + int(cur.minute) * 60 + int(cur.second)
#
#
# # =====    Time    ===== #
# def time(start_time, end_time):
#     if not isinstance(start_time, int):
#         start_time, end_time = _to_s(start_time), _to_s(end_time)
#     i, j = min(start_time, end_time), max(start_time, end_time)
#     for i in range(i, j+1):
#         yield _to_hms(i)
#
# # =====    Time    ===== #
# def hms(time='', end=''):
#     time = [d.now().hour, d.now().minute, d.now().second] if not time else time
#     hour, minute, second = time
#     converted = _to_time(hour, minute, second)
#     converted = converted.strftime('%H:%M:%S')
#     end = '\n' if not end else end
#     return _beige2 + converted + _end, end=end)


def from_timestamp(timestamp):
    from datetime import datetime
    # print(1563811175.168 - 1557003600.000)
    # 6807575.167999983
    return datetime.fromtimestamp(timestamp / 1000)


"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""

if __name__ == '__main__':
    # print(to_time(h=18, m=46, s=13))
    # print(to_hms(s=datetime.datetime.now()))
    # print(to_seconds(time="18:47:20"))
    pass