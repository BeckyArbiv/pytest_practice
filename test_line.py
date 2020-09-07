def test_findpoint():
	from line import findpoint
	answer = findpoint((0,0),(1,1),3)
	expected = 3
	assert answer == expected
