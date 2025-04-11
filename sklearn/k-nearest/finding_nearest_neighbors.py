from movies import movie_dataset, movie_labels

print(movie_dataset['Bruce Almighty'])
print(movie_labels['Bruce Almighty'])

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance


def classify(unknown, dataset, k):
  distances = []
  for title in dataset:
    distance_to_point = distance(dataset[title], unknown)
    distances.append([distance_to_point, title])
    distances.sort()
    neighbors = distances[0:k]
  return neighbors

print(classify([.4,.2,.9], movie_dataset, 5))

# Output-only Terminal
# Output:

# [0.006630902005283176, 0.21843003412969283, 0.8539325842696629]
# 0
# [[0.08273614694606074, 'Lady Vengeance'], [0.22989623153818367, 'Steamboy'], [0.23641372358159884, 'Fateless'], [0.26735445689589943, 'Princess Mononoke'], [0.3311022951533416, 'Godzilla 2000']]

# to predict

from movies import movie_dataset, movie_labels, normalize_point
print('Transformers' in movie_dataset)
my_movie = [147000000, 144, 2007]
normalized_my_movie = normalize_point(my_movie)

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  if num_good > num_bad:
    return 1
  else:
    return 0

print(classify(normalized_my_movie, movie_dataset, movie_labels, 5))



# from movies import training_set, training_labels, validation_set, validation_labels  
# def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
#   num_correct = 0.0
#   for title in validation_set:
#     guess = classify(validation_set[title], training_set, training_labels, k)
#     if guess == validation_labels[title]:
#       num_correct += 1
#   return num_correct / len(validation_set)


# print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, 3))
