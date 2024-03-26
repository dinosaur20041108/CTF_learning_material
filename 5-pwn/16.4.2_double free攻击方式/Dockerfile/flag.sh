#!/bin/bash
echo $DASFLAG > /home/ctf/flag
export DASFLAG=not_flag
DASFLAG=not_flag
chown root:ctf /home/ctf/flag 
chmod 740 /home/ctf/flag
