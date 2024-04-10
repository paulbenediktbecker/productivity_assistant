text_in_Block = input()

from Assistant import Assistant
assi = Assistant()


def run_cmds_in_new_process(cmds):
    import subprocess
    import sys
    import os
   

    cmds = [
        "python",
        "Assistant.py",
        cmds
    ]

    #make window disappear in windows 
    if 'nt' == os.name:
        flags = 0
        flags |= 0x00000008  # DETACHED_PROCESS
        flags |= 0x00000200  # CREATE_NEW_PROCESS_GROUP
        flags |= 0x08000000  # CREATE_NO_WINDOW

        pkwargs = {
            'close_fds': True,  # close stdin/stdout/stderr on child
            'creationflags': flags,
        }
       

    p = subprocess.Popen(cmds,start_new_session=True, **pkwargs)
    #subprocess.Popen(cmds, start_new_session=True,
    #                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    #                 )

    # proc_exe = subprocess.Popen(cmds, shell=True)
    # proc_exe.send_signal(subprocess.signal.SIGTERM)
    sys.exit()

works_isolated, action = assi.works_input_isolated(text_in_Block)
if works_isolated:
    run_cmds_in_new_process(text_in_Block)
else:
    run_cmds_in_new_process(action(text_in_Block))
    