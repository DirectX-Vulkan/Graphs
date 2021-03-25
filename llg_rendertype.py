from dataclasses import dataclass

from llg_renderstats import RenderStats, RtRenderStats, NrtRenderStats
from llg_results import Result, RtResult, NrtResult


@dataclass
class RenderType:
    pc_id: str
    render_object: str
    vulkan_stats: RenderStats
    directx_stats: RenderStats

    def __init__(self, pc_id:str, render_object:str):
        self.pc_id = pc_id
        self.render_object = render_object

    def init_rt(self):
        self.vulkan_stats = RtRenderStats(0,0,0,0,0,0)
        self.directx_stats = RtRenderStats(0,0,0,0,0,0)

    def init_nrt(self):
        self.vulkan_stats = NrtRenderStats(0,0,0,0,0,0)
        self.directx_stats = NrtRenderStats(0,0,0,0,0,0)

    def __change_vulkan_result(self, result: Result):
        # replace the zero-filled stats with the actual stats
        if isinstance(result, RtResult):
            self.vulkan_stats = RtRenderStats(result.cpu_min(),
                                              result.cpu_avg(),
                                              result.cpu_max(),
                                              result.fps_min(),
                                              result.fps_avg(),
                                              result.fps_max())
        elif isinstance(result, NrtResult):
            self.vulkan_stats = NrtRenderStats(result.cpu_min(),
                                              result.cpu_avg(),
                                              result.cpu_max(),
                                              result.spf_min(),
                                              result.spf_avg(),
                                              result.spf_max())

    def __change_directx_result(self, result: Result):
        # replace the zero-filled stats with the actual stats
        if isinstance(result, RtResult):
            self.directx_stats = RtRenderStats(result.cpu_min(),
                                               result.cpu_avg(),
                                               result.cpu_max(),
                                               result.fps_min(),
                                               result.fps_avg(),
                                               result.fps_max())
        elif isinstance(result, NrtResult):
            self.directx_stats = NrtRenderStats(result.cpu_min(),
                                                result.cpu_avg(),
                                                result.cpu_max(),
                                                result.spf_min(),
                                                result.spf_avg(),
                                                result.spf_max())


    def change_result(self, result: Result):
        if result.engine() == "vulkan":
            self.__change_vulkan_result(result)
        elif result.engine() == "directx11":
            self.__change_directx_result(result)
