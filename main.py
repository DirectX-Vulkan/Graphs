# --- imports ---
# region
import getopt
import sys

from llg_filereader import read_files
from llg_graphs import show_graphs
from llg_rendertype import RenderType
from llg_results import RtResult, NrtResult
from llg_test_scores import test_scores
# endregion imports


def main(argv):
    consoleOutput = False
    disableGraphs = False

    try:
        opts, args = getopt.getopt(argv, "c", ["console", "no-graph"])
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    for opt, arg in opts:
        if opt in ["-c", "--console"]:
            consoleOutput = True
        if opt in ["-c", "--no-graph"]:
            disableGraphs = True

    return [consoleOutput, disableGraphs]

consoleOutput = False
disableGraphs = False

if __name__ == "__main__":
    args = main(sys.argv[1:])
    consoleOutput = args[0]
    disableGraphs = args[1]

# read all csv files and extract the logs
logs = read_files('data\\')
nrt_logs = logs.nrt_logs
rt_logs = logs.rt_logs

rt_results = []
nrt_results = []

# categorize logs (RT)
for rt_log in rt_logs:
    # check if a correspondent result class exists
    existingResult = False
    for rt_result in rt_results:
        if rt_log.equal_settings(rt_result.logs[0]):
            rt_result.logs.append(rt_log)
            existingResult = True
            pass
    if not existingResult:
        rt_result = RtResult([rt_log])
        rt_results.append(rt_result)

# categorize logs (NRT)
for nrt_log in nrt_logs:
    # check if a correspondent result class exists
    existingResult = False
    for nrt_result in nrt_results:
        if nrt_log.equal_settings(nrt_result.logs[0]):
            nrt_result.logs.append(nrt_log)
            existingResult = True
            pass
    if not existingResult:
        nrt_result = NrtResult([nrt_log])
        nrt_results.append(nrt_result)

if consoleOutput:
    results = []
    for rt_result in rt_results:
        results.append(rt_result)
    for nrt_result in nrt_results:
        results.append(nrt_result)
    test_scores(results)

if not disableGraphs:
    show_graphs(rt_results)
    #show_graphs(nrt_results)
