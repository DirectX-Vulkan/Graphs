from llg_results import Result, RtResult, NrtResult

def getResultCategory(result: Result):
    first_log = result.logs[0]
    return first_log.pc_id + "\t" + first_log.engine + "\t" + first_log.render_object

def test_scores(results: []):
    for result in results:
        if isinstance(result, RtResult):
            print("rt:\t" + getResultCategory(result))
        elif isinstance(result, NrtResult):
            print("nrt:\t" + getResultCategory(result))

        print("\tcpu:\t{:0.1f}".format(result.cpu_min()) 
              + "\t" + "{:0.1f}".format(result.cpu_avg()) 
              + "\t" + "{:0.1f}".format(result.cpu_max()))
            
        if isinstance(result, RtResult):
            print("\tfps:\t{:0.1f}".format(result.fps_min()) 
                  + "\t" + "{:0.1f}".format(result.fps_avg()) 
                  + "\t" + "{:0.1f}".format(result.fps_max()))
        elif isinstance(result, NrtResult):
            print("\tspf:\t" + "{:0.1f}".format(result.spf_min()) 
                  + "\t" + "{:0.1f}".format(result.spf_avg()) 
                  + "\t" + "{:0.1f}".format(result.spf_max()))
