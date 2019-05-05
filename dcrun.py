#!/usr/bin/env python

# docker-compose run --service-ports  web
# docker exec -it <mycontainer> bash
from subprocess import call, STDOUT
import sys

BASE_COMPOSE = "docker-compose run"

# remove the initial dcrun command from the argv
del sys.argv[0]

if sys.argv:
    argv_base = sys.argv[0]

    if argv_base == "manage":
        if len(sys.argv) > 1:
            call("docker-compose run web python manage.py " + sys.argv[1], shell=True, stderr=STDOUT)
        else:
            ENTRYPOINT = "--entrypoint='python manage.py'"
            call("docker-compose run web python manage.py", shell=True, stderr=STDOUT)
    elif argv_base == "run":
        call("docker-compose run --service-ports web", shell=True)
    else:
        print("Unkown command " + argv_base)
