# Program to find minimum number of platforms
# required on a railway station


def findPlatformNaiveApproach(arr, dep, n):
	# plat_needed indicates number of platforms
	# needed at a time
	plat_needed = 1
	result = 1

	# run a nested loop to find overlap
	for i in range(n):
		# minimum platform needed
		plat_needed = 1

		for j in range(i+1, n):
			# check for overlap
			if (max(arr[i], arr[j]) <= min(dep[i], dep[j])):
				plat_needed += 1

		# update result
		result = max(result, plat_needed)

	return result

# Program to find minimum
# number of platforms
# required on a railway
# station

# Returns minimum number
# of platforms required


def findPlatformOptimised(arr, dep, n):

	# Sort arrival and
	# departure arrays
	arr.sort()
	dep.sort()

	# plat_needed indicates
	# number of platforms
	# needed at a time
	plat_needed = 1
	result = 1
	next = 1
	prev = 0

	# Similar to merge in
	# merge sort to process
	# all events in sorted order
	while (next < n and prev < n):

		# If next event in sorted
		# order is arrival,
		# increment count of
		# platforms needed
		if (arr[next] <= dep[prev]): # arrival of next is less than current departure

			plat_needed += 1
			next += 1

		# Else decrement count
		# of platforms needed
		elif (arr[next] > dep[prev]): # arrival of next is greater than current departure

			plat_needed -= 1
			prev += 1

		# Update result if needed
		if (plat_needed > result):
			result = plat_needed

	return result







arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

n = len(arr)

print("{}".format(
    findPlatformNaiveApproach(arr, dep, n)))

print("Minimum Number of Platforms Required = ",
	findPlatformOptimised(arr, dep, n))

