# Grab src and place into server
multipass transfer index.js compatible-wolffish:.
multipass exec compatible-wolffish -- node index.js &
multipass shell compatible-wolffish