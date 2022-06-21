"""
Exercise No. 99

Create a function that will increment avery time format found in a string (for example 00:42:33,120) by a specific time
(for example 00:00:30,550). The result between the examples is 00:43:03,670.

Rules:
    - The function must take 2 arguments: a string from where to search time format and a string that respects the
    format hours:minutes:seconds,milliseconds.
    - The function must return a string identical to the first argument but with all time format incremented with the
    second argument time format.
    - If the second argument does not respect the given time format (for example 00:00:00 or 0:0:0,00), you must return
    "There is a problem with the second argument"

Examples:
    sync_subs("708 00:44:50,006 --> 00:44:53,007 Hi.", "00:03:30,550) -> 708 00:48:20,556 --> 00:48:23,557 Hi.

    sync_subs("179 00:12:52,766 --> 00:12:55,900 [Door rattling]", "00:11:11,111") ->
                                                                    179 00:24:03,877 --> 00:24:07,011 [Door rattling]

    sync_subs("188 00:13:37,243 --> 00:13:39,744 30 minutes. Everyone's ready. 189 00:13:39,779 --> 00:13:43,548",
                "01:00:51,111") -> 188 01:14:28,354 --> 01:14:30,855 30 minutes. Everyone's ready.
                 189 01:14:30,890 --> 01:14:34,659

Notes:
    - You don't need to worry about a time format being wrong in the first string like 00:13:79,779 or 00:13:39,79
    because there won't be any mistake in it.
"""
import re
from datetime import datetime, timedelta


def sync_subs(subtitles, i):
    timestamps = re.compile(r'(2[0-3]|[01]\d):([5]\d|[0-4]\d):([5]\d|[0-4]\d),(\d{3})')

    if not re.match(timestamps, i):
        return 'There is a problem with the second argument'
    i = timedelta(hours=int(i[:2]), minutes=int(i[3:5]),
                  seconds=int(i[6:8]), milliseconds=int(i[9:]))

    def convert(s):
        s = datetime.strptime(s, '%H:%M:%S,%f')
        return str((s + i).time())[:-3].replace('.', ',')

    return re.sub(timestamps, lambda x: convert(x.group()), subtitles)


print(sync_subs("188 00:13:37,243 --> 00:13:39,744 30 minutes. Everyone's ready. 189 00:13:39,779 --> 00:13:43,548",
                "01:00:51,111"))
