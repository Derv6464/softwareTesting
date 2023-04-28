from fullmoon import NextFullMoon
from fullmoon import IsFullMoon
import datetime
i = IsFullMoon()
date = str((datetime.datetime.now()).date())
print(date)
print(i.set_date_string(date, '%Y-%m-%d').is_full_moon())