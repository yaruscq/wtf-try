
from flask_login import UserMixin

class User(UserMixin):
	"""docstring for User"""

	def __init__(self, id, username, email):
		
		self.id = str(id)
		self.username = username
		self.email = email

	def get_id(self):
		return str(self.id)


# Create in-memory user storage
users = {
    '1': User(1, 'user1', 'user1@example.com'),
    '2': User(2, 'user2', 'user2@example.com'),
    '3': User(3, 'user3', 'user3@example.com'),
    '4': User(4, 'user4', 'user4@example.com')
}



# (user for user in users.values() if user.username == username) iterates through users.values(), checking each User object’s username attribute against the provided username.

# python dictionary values() returns a list of values from keys

# next() Function: next() retrieves the first item in this generator that satisfies the condition. If no items match, it returns the default value, which in this case is None.

def get_user_by_username(username):
	return next((user for user in users.values() if user.username == username), None)


def get_user_by_email(email):
	return next((user for user in users.values() if user.email == email), None)