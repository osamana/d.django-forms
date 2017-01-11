these keys are generated using "ssh-keygen -t rsa" command.
see (https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)

you can generate your own keys, but for the development this is good enough

just apply these keys to the target linux machine like this:
ssh-copy-id user@123.45.56.78
or
cat ~/.ssh/id_rsa.pub | ssh user@123.45.56.78 "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"

follow the tutorial on the above line to enable root ssh 

