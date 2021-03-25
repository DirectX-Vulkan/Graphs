import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from llg_results import Result, RtResult, NrtResult
from llg_renderdata import RenderData
from llg_renderstats import RtRenderStats, NrtRenderStats
from llg_rendertype import RenderType


def compare(render_type: RenderType, result: Result):
    return render_type.pc_id == result.pc_id() and render_type.render_object == result.render_object()

def show_subgraph(render_data: RenderData):
    x = np.arange(len(render_data.labels))
    width = 0.35

    fix, ax = plt.subplots()
    rects = [
        ax.bar(x-width/2, render_data.v_maxs, width, label='Vulkan max', color='#ff5555'),
        ax.bar(x-width/2, render_data.v_avgs, width, label='Vulkan avg', color='#cc4444'),
        ax.bar(x-width/2, render_data.v_mins, width, label='Vulkan min', color='#993333'),
        ax.bar(x+width/2, render_data.d_maxs, width, label='DirectX max', color='#aaff55'),
        ax.bar(x+width/2, render_data.d_avgs, width, label='DirectX avg', color='#88cc44'),
        ax.bar(x+width/2, render_data.d_mins, width, label='DirectX min', color='#669933')
        ]
    ax.set_ylabel('Scores')
    ax.set_title('Scores by pc, object & render engine')
    ax.set_xticks(x)
    ax.set_xticklabels(render_data.labels)
    ax.legend()
    
    # requires ax, so needs to be inside 
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{:0.2f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2,
                            height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center',
                        va='center')

    for rect in rects:
        autolabel(rect)

    # tutorial says to use this, but they never defined fig
    #fig.tight_layout()

    plt.show()

def show_graphs(results: []):
    # --- prepare data for graphs ---
    # region
    render_types = []
    for result in results:
        existing_type = False
        for render_type in render_types:
            if compare(render_type, result):
                existing_type = True
        if not existing_type:
            render_types.append(RenderType(result.pc_id(), result.render_object()))

    for render_type in render_types:
        if isinstance(results[0], RtResult):
            render_type.init_rt();
        elif isinstance(results[0], NrtResult):
            render_type.init_nrt();
        for result in results:
            if compare(render_type, result):
                # should only find one of each at most, as they should've been merged earlier
                # (1 vulkan & 1 directx)
                render_type.change_result(result)
    # endregion prepare data for graphs

    # --- cpu graph ---
    # region
    render_data = RenderData()

    for render_type in render_types:
        render_data.labels.append(render_type.pc_id + "\n" + render_type.render_object + "\ncpu")
        # for readability's sake
        v_stats = render_type.vulkan_stats
        d_stats = render_type.directx_stats
        # vulkan stats
        render_data.v_mins.append(v_stats.cpu_min)
        render_data.v_avgs.append(v_stats.cpu_avg)
        render_data.v_maxs.append(v_stats.cpu_max)
        # directx stats
        render_data.d_mins.append(d_stats.cpu_min)
        render_data.d_avgs.append(d_stats.cpu_avg)
        render_data.d_maxs.append(d_stats.cpu_max)

    show_subgraph(render_data)
    # endregion cpu graph
    
    # --- secondary graph ---
    # region
    render_data = RenderData()

    # --- fps graph ---
    # region
    if isinstance(results[0], RtResult):
        for render_type in render_types:
            render_data.labels.append(render_type.pc_id + "\n" + render_type.render_object + "\nfps")
            # for readability's sake
            v_stats = render_type.vulkan_stats
            d_stats = render_type.directx_stats
            # vulkan stats
            render_data.v_mins.append(v_stats.fps_min)
            render_data.v_avgs.append(v_stats.fps_avg)
            render_data.v_maxs.append(v_stats.fps_max)
            # directx stats
            render_data.d_mins.append(d_stats.fps_min)
            render_data.d_avgs.append(d_stats.fps_avg)
            render_data.d_maxs.append(d_stats.fps_max)
    # endregion fps graph

    # --- spf graph ---
    # region
    if isinstance(results[0], NrtResult):
        for render_type in render_types:
            render_data.labels.append(render_type.pc_id + "\n" + render_type.render_object + "\nspf")
            # for readability's sake
            v_stats = render_type.vulkan_stats
            d_stats = render_type.directx_stats
            # vulkan stats
            render_data.v_mins.append(v_stats.spf_min)
            render_data.v_avgs.append(v_stats.spf_avg)
            render_data.v_maxs.append(v_stats.spf_max)
            # directx stats
            render_data.d_mins.append(d_stats.spf_min)
            render_data.d_avgs.append(d_stats.spf_avg)
            render_data.d_maxs.append(d_stats.spf_max)
    # endregion spf graph

    show_subgraph(render_data)
    # endregion secondary graph
