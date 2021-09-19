init -900 python:
    class Event():
        def __init__(self, name, location, label, repeat = False, time = None, prior = 1):
            global events
            self.name     = name
            self.location = location
            self.label    = label
            self.prior    = prior
            self.time     = time
            self.repeat   = repeat
            self.complete = False
            events[self.name] = self
        def check(self, check_location = True, check_time = True):
            global time_now
            if self.complete:
                return False
            if check_location:
                if self.location != location_now:
                    return False
            if check_time:
                if self.time:
                    if time_now not in self.time:
                        return False
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
