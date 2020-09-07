def test_celsius_from_far():
	from temp_conv import celsius_from_far
	result = celsius_from_far(20)
	expected = 68
	assert result == expected
