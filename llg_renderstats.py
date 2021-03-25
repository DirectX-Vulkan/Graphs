from dataclasses import dataclass


@dataclass
class RenderStats:
    cpu_min: float
    cpu_avg: float
    cpu_max: float


@dataclass
class RtRenderStats(RenderStats):
    fps_min: float
    fps_avg: float
    fps_max: float
    
    def __init__(self, cpu_min:float, cpu_avg:float, cpu_max:float, fps_min:float, fps_avg:float, fps_max:float):
        self.cpu_min = cpu_min
        self.cpu_avg = cpu_avg
        self.cpu_max = cpu_max
        self.fps_min = fps_min
        self.fps_avg = fps_avg
        self.fps_max = fps_max


@dataclass
class NrtRenderStats(RenderStats):
    spf_min: float
    spf_avg: float
    spf_max: float
    
    def __init__(self, cpu_min:float, cpu_avg:float, cpu_max:float, spf_min:float, spf_avg:float, spf_max:float):
        self.cpu_min = cpu_min
        self.cpu_avg = cpu_avg
        self.cpu_max = cpu_max
        self.spf_min = spf_min
        self.spf_avg = spf_avg
        self.spf_max = spf_max
