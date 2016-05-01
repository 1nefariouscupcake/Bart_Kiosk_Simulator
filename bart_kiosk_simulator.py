def load_card(ones, fives, tens, twenties):
	return ones + (5 * fives) + (10 * tens) + (20 * twenties)

print load_card(0, 0, 0, 0)
print load_card(0, 0, 0, 9)
print load_card(2, 3, 0, 0)
print load_card(3, 1, 1, 3)