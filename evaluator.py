# 
# MODIFY get_data() AS YOU LIKE.
# DO NOT SEND THIS FILE TO US

import random
random.seed(111)  #remove hash-sign to get randomization seed we will be using at evaluation
#                    (if you fix the seed you get always the same probabilty choice sequence)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	# @TODO: Update this function just for your own testing. We will use our own get_data().
	       #[M, N,   D,   K, LAMBDA, MU,    universal_state]
	return [50, 100, 5, 80, 30, 0.55, [[(10,10), 0, 'masked', 'notinfected'], [(20, 10), 1, 'notmasked', 'notinfected'], [(30, 10), 7, 'notmasked', 'notinfected'], [(40, 10), 2, 'notmasked', 'notinfected'], [(50, 10), 6, 'notmasked', 'notinfected'], [(60, 10), 2, 'masked', 'notinfected'], [(70, 10), 6, 'notmasked', 'notinfected'], [(80, 10), 1, 'notmasked', 'notinfected'], [(90, 10), 0, 'notmasked', 'notinfected'], [(99, 10), 6, 'notmasked', 'notinfected'], [(10, 20), 7, 'notmasked', 'notinfected'],[(20, 20), 0, 'notmasked', 'notinfected'], [(30, 20), 1, 'notmasked', 'notinfected'], [(40, 20), 7, 'notmasked', 'notinfected'], [(50, 20), 2, 'notmasked', 'notinfected'], [(60, 20), 6, 'masked', 'notinfected'], [(70,20), 2, 'notmasked', 'notinfected'], [(80, 20), 6, 'notmasked', 'notinfected'], [(90, 20), 1, 'masked', 'notinfected'], [(99, 20), 0, 'notmasked', 'notinfected'], [(10, 30), 6, 'notmasked', 'notinfected'], [(20, 30), 7, 'notmasked', 'notinfected'],[(30, 30), 0, 'masked', 'notinfected'], [(40, 30), 1, 'notmasked', 'notinfected'], [(50, 30), 7, 'notmasked', 'infected'], [(60, 30), 2, 'notmasked', 'notinfected'], [(70, 30), 6, 'notmasked', 'notinfected'], [(80, 30), 2, 'notmasked', 'notinfected'], [(90, 30), 6, 'masked', 'notinfected'], [(99, 30), 1, 'notmasked', 'notinfected'], [(10, 40), 0, 'notmasked', 'notinfected'], [(20, 40), 6, 'masked', 'notinfected'], [(30, 40), 7, 'notmasked', 'notinfected'],[(40, 40), 0, 'notmasked', 'notinfected'], [(50, 40), 1, 'masked', 'notinfected'], [(60, 40), 7, 'notmasked', 'notinfected'], [(70, 40), 2, 'notmasked', 'notinfected'], [(80, 40), 6, 'notmasked', 'notinfected'], [(90, 40), 2, 'masked', 'notinfected'], [(99, 40), 6, 'notmasked', 'notinfected'], [(10, 49), 1, 'notmasked', 'notinfected'], [(20, 49), 0, 'notmasked', 'notinfected'], [(30, 49), 6, 'notmasked', 'notinfected'], [(40, 49), 7, 'notmasked', 'notinfected'],[(50, 49), 0, 'notmasked', 'notinfected'], [(60, 49), 1, 'notmasked', 'notinfected'], [(70, 49), 7, 'notmasked', 'notinfected'], [(80, 49), 2, 'notmasked', 'notinfected'], [(90, 49), 6, 'masked', 'notinfected']]]