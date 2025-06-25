# 1. Create the paintings list
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# 2. Create the dates list
dates = [1939, 1933, 1946, 1940]

# 3. Zip paintings and dates together and convert to list
paintings = list(zip(paintings, dates))
print(paintings)  # Check the zipped list

# 4. Append last minute additions
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)  # Check after additions

# 5. Find the length of the paintings list
num_paintings = len(paintings)
print("Number of paintings:", num_paintings)

# 6. Generate a list of audio tour ID numbers starting at 1
audio_tour_number = list(range(1, num_paintings + 1))
print(audio_tour_number)

# 7. Zip audio_tour_number with paintings and save as master_list
master_list = list(zip(audio_tour_number, paintings))
print(master_list)
