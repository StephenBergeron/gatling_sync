# gatling_sync

This (hobby) project allow to do performance testing for web application and REST service in the cloud with [Gatling](https://gatling.io/).

It assume that your application/service is out there somewhere, and that you have access to a remote server.

This project use Rsync over ssh with public/private key authentication to synchronize Gatling folders over the network.

* push - Upload executables, jars, classes and simulation to the `test_server`.
* pull - Download results.


## Getting Started

You need to setup ssh login on the remote `test_server` with public/private keys. 
This is a common procedure and I prefer it over tools such as sshpass.

* From your `workstation`, push your public key to the `test_server`: For example
~~~~
scp $HOME/.ssh/id_rsa.pub username@${test_server}
~~~~

* Then append the public key to the authorized keys on your remote `test_server`:
```
ssh -l username@${test_server}
cat id_rsa.pub >> .ssh/authorized_keys
```

The intended workflow is to use your workstation (local machine) for development and debugging purposes. 
Once you are satisfied with your performance simulation, these instructions will get you a copy of Gatling up and running on your `test_server`. 
That allow to isolate the simulation from network noise.

Again, this is a personal project...
