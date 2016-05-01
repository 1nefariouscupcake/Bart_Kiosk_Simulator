

DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

def load_card(ones, fives, tens, twenties):
	return ones + (5 * fives) + (10 * tens) + (20 * twenties)

def travel_to_destination(fare_price, card_value):

	if fare_price <= card_value:
		print "Welcome aboard, enjoy your trip!"
	else:
		print "You need more Money!"

clipper_card = load_card(3, 0, 0, 0)
travel_to_destination(FREMONT_TO_COLMA, clipper_card)

clipper_card = load_card(0, 0, 0, 1)
travel_to_destination(HAYWARD_TO_CONCORD, clipper_card)

clipper_card = load_card(1, 1, 0, 0)
travel_to_destination(DUBLIN_TO_POWELL, clipper_card)

clipper_card = load_card(2, 0, 1, 0)
travel_to_destination(FRUITVALE_TO_UNION_CITY, clipper_card)