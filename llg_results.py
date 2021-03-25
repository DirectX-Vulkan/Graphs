from dataclasses import dataclass


@dataclass
class Result:
    logs: []

    def __init__(self, logs = []):
        self.logs = logs
        return self

    def pc_id(self):
        return self.logs[0].pc_id

    def engine(self):
        return self.logs[0].engine

    def render_object(self):
        return self.logs[0].render_object

    def cpu_min(self):
        min:float = self.logs[0].cpu
        for log in self.logs:
            if min > log.cpu:
                min = log.cpu
        return min

    def cpu_avg(self):
        avg:float = 0.0
        i:int = 0
        for log in self.logs:
            if log.cpu > 0:
                avg += log.cpu
                i += 1
        if i > 0:
            return avg / i
        else:
            return 0.0;

    def cpu_max(self):
        max:float = 0.0
        for log in self.logs:
            if log.cpu > max:
                max = log.cpu
        return max


@dataclass
class RtResult(Result):
    def fps_min(self):
        min:float = self.logs[0].fps
        for log in self.logs:
            if log.fps < min:
                min = log.fps
        return min

    def fps_avg(self):
        avg:float = 0.0
        i:int = 0
        for log in self.logs:
            avg += log.fps
            i += 1
        if i > 0:
            return avg / i
        else:
            return 0.0;

    def fps_max(self):
        max:float = 0.0
        for log in self.logs:
            if log.fps > max:
                max = log.fps
        return max


@dataclass
class NrtResult(Result):
    def spf_min(self):
        min:float = self.logs[0].spf
        for log in self.logs:
            if log.spf < min:
                min = log.spf
        return min

    def spf_avg(self):
        avg:float = 0.0
        i:int = 0
        for log in self.logs:
            avg += log.spf
            i += 1
        if i > 0:
            return avg / i
        else:
            return 0.0;

    def spf_max(self):
        max:float = 0.0
        for log in self.logs:
            if log.spf > max:
                max = log.spf
        return max
