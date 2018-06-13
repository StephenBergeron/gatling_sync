# gatling_sync

This (hobby) project allow to do performance testing for web application and REST service in the cloud with [Gatling](https://gatling.io/).

It assume that your application/service is out there somewhere, and that you have access to a remote server.

This project use Rsync over ssh with public/private key authentication to synchronize Gatling folders over the network.

* push - Upload executables, jars, classes and simulation to the `test_server`.
* pull - Download results.


## Getting Started

The intended workflow is to use your `workstation` (local machine) for development and debugging purposes. 
Once you are satisfied with your performance simulation, you copy Gatling and simulations classes to your `test_server`. 
That allow to isolate the simulation from network noise.

You need to setup ssh login on the remote `test_server` with public/private keys. 
This can be done with [ssh-copy-id](https://www.ssh.com/ssh/copy-id).

The tools contained in this project assume that the `$USER` on the `workstation` and the `test_server` are identical.
This can be modified if there is a need to be more flexible.
However I found that to streamline the workflow.

~~~~
sample usage here for push test infrastructure
~~~~

~~~~
sample launch on the $test_server
~~~~

~~~~
sample usage here for pull results
~~~~

Again, this is a personal project...
