from dataclasses import dataclass


@dataclass
class RenderData:
    labels: []
    v_mins: []
    v_avgs: []
    v_maxs: []
    d_mins: []
    d_avgs: []
    d_maxs: []

    def __init__(self):
        self.labels = []
        self.v_mins = []
        self.v_avgs = []
        self.v_maxs = []
        self.d_mins = []
        self.d_avgs = []
        self.d_maxs = []
