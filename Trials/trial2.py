try:
	from google_searching import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "formula of Sin   cos theta the whole square"
z = []
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	z.append(j)
print(z)

