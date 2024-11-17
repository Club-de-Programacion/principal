# List of event probabilities
response = input("Enter the probabilities separated by a space: ").split(" ")
for i in range(len(response)):
    response[i] = float(response[i]) / 100
probabilities = response

# Calculate the probability of none of the events happening
prob_none = 1
for p in probabilities:
    prob_none *= (1 - p)

# Calculate the probability of at least one event happening
prob_at_least_one = 100 * (1 - prob_none)

print(f"{prob_at_least_one:.2f}%")

while True:
    if input() == "exit":
        exit(0)