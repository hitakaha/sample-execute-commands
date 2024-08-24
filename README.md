# Sample code to execute show commands in series

This is a sample code to execute commands in series.
To add a new command, copy a file in verify_cmds and edit it.
After that, add the file in \_\_init\_\_.py

You don't need to modify main.py to add a new command.
Scalable design for network operations.

# Sample output

```
% python3 main.py 
Executed commands                       Results
--------------------------------------- ----------------------------------------
show_bgp_neighbor                       BGP neighbors are up!                   
show_ip_int_brief                       Interfaces are up!                      
show_ospf_neighbor                      OSPF neighbors are up!   
```


