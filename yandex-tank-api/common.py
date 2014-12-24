"""
Commands from HTTP Server (from manager_queue):
    Run the test to the next break:
        {
        'session': '1a2b4f3c'
        'cmd':'run',
        'break': --- see break requests for tank
        'test': --- only when creating new session
        'config': --- only when creating new  session
        }
    Stop the test
        {
        'session': '1a2b4f3c'
        'cmd':'stop'
        }
            

Status reported by tank (from manager_queue):
    {
     'status': 'running'|'success'|'failure'
     'current_stage': --- current stage (from test_stage_order)
     'break': --- stage to make a break before
     'failures': --- [ {'stage': stage-at-which-failed,'reason': reason of failure }, 
                       {'stage':stage-of-next-failure,'reason':...}, 
                       ... ]
     }    
=====

Break requests (into tank_queue):
    {'break': --- any stage from test_stage_order }

====
Status reported to HTTP Server (into webserver_queue):
    {
    'session': '1a2b4f3c'
    'test': 'DEATHSTAR-10-12345'
    'status': 'running'|'success'|'failed' (from tank or from  manager)
    'stage': --- optional, from tank only
    'reason' : --- optional (from tank or from manager)
    }
"""

test_stage_order=['lock','configure','prepare','start','poll','end','postprocess','unlock','finish']

def is_A_earlier_than_B(stage_A,stage_B):
    """Slow but reliable"""
    return test_stage_order.index(stage_A) < test_stage_order.index(stage_B)

