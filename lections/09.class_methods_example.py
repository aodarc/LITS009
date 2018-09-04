class Base:
	def __init__(self, *args, **kwargs):
		self.props = [i for i in args]



class BaseIterator:
	attrs = (i for i in range(10))

	def __iter__(self):
		return self

	def __next__(self):
		return 42



class Indexer(Base):
	def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.settings = {'default': 42}

	def __getitem__(self, index):
		if isinstance(index, int):
			return self.props[-index]
		elif isinstance(index, str):
			return self.settings.get(index, '')

	def __setitem__(self, index, value):
		self.props[index] = value

	def __containse__(self, value):
		return not value in self.props


	def slice_example(self, conf):
		slicer = {
			'first': slice(0),
			'middle': slice(1, -1),
			'reversed': slice(None, None, -1)
		}
		return self.props[slicer[conf]]

	@property
	def sum_of_my(self):
		return sum(self.props)


	def sum_of_my2(self):
		return sum(self.props)

	@staticmethod
	def print_hello(value=42):
		print('hello')
		return 44442222

	@classmethod
	def some_class_method(cls, value):
		return -value

	def __new__(self, *args, **kwargs):
		# return Indexer(*args, **kwargs)
		return 'dick'



i = Indexer(1,2,3,4,5)  # init was called 

print(i)

# print(i[-2])  # __getitem__
# print(i['default'])  # __getitem__
# i[-2] = 42 # __setitem__


# print(i.sum_of_my)
# print(i.sum_of_my2)
# print(i.sum_of_my2())

# print(Indexer.print_hello())

