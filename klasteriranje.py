from random import shuffle

def klasteriranje(podaci):
	print "sadf"
	podaci = suffle(podaci)
	dim = len(podaci)/6
	klasteri = []
	for i in range(5):
		klasteri.append(podaci[i*dim:(i+1)*dim])
	klasteri.append(podaci[5*dim:])
	print len(klasteri)