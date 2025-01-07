Terminal1: docker run -it --rm --net=host ghcr.io/eclipse/kuksa.val/databroker:master --insecure


Terminal2:
 source ~/venvs/kuksa/bin/activate
python pub2.py



Terminal3:
 source ~/venvs/kuksa/bin/activate
python sub2.py
