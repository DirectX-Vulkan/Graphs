from dataclasses import dataclass


@dataclass
class Log:
    timestamp: int
    pc_id: str
    engine: str
    render_object: str
    cpu: float

    def equal_settings(self, other):
        if not type(self) is type(other):
            return NotImplemented
        return self.pc_id == other.pc_id and self.engine == other.engine and self.render_object == other.render_object


@dataclass
class RtLog(Log):
    fps: float

    def __init__(self, timestamp: int,
                 pc_id: str,
                 engine: str,
                 render_object:str,
                 fps: float,
                 cpu: float):
        self.timestamp = timestamp
        self.pc_id = pc_id
        self.engine = engine
        self.render_object = render_object
        self.fps = fps
        self.cpu = cpu


@dataclass
class NrtLog(Log):
    spf: float

    def __init__(self, timestamp: int,
                 pc_id: str,
                 engine: str,
                 render_object:str,
                 spf: float,
                 cpu: float):
        self.timestamp = timestamp
        self.pc_id = pc_id
        self.engine = engine
        self.render_object = render_object
        self.spf = spf
        self.cpu = cpu


@dataclass
class Logs:
    nrt_logs: []
    rt_logs: []

    def __init__(self):
        self.nrt_logs = []
        self.rt_logs = []

    def add_log(self, type: str, data: []):
        if type == 'rt':
            self.rt_logs.append(RtLog(int(data[0]),
                                      data[1],
                                      data[2],
                                      data[3],
                                      float(data[4]),
                                      float(data[5])))
        elif type == 'nrt':
            self.nrt_logs.append(NrtLog(int(data[0]),
                                        data[1],
                                        data[2],
                                        data[3],
                                        float(data[4]),
                                        float(data[5])))
