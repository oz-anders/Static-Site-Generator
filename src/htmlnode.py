class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("Not implemented yet")
		
	def props_to_html(self):
		if self.props is None:
			return ""
		props_html = ""
		for prop in self.props:
			props_html += f' {prop}="{self.props[prop]}"'
		return props_html

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
	"""LeafNode is a type of HTML tag with no children <p> tag with no children"""
	def __init__(self, tag, value, props=None):
		super(LeafNode, self).__init__(tag, value, None, props)
		

	def to_html(self):
		if self.value is None:
			raise ValueError("Leaf nodes requires a value")
		if self.tag == None:
			return self.value

		html_string = self.props_to_html()

		return f"<{self.tag}{html_string}>{self.value}</{self.tag}>"

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
	"""docstring for ParentNode"""
	def __init__(self, tag, children, props=None):
		super(ParentNode, self).__init__(tag, children, props)
		if self.tag == None:
			raise ValueError("Parent nodes need tags")
		if self.children == None:
			raise ValueError("Parent nodes need children")

	def to_html(self):

		children_list = []
		for child in self.children:
			children_list.append(child.to_html())
		children_html = "".join(children_list)
		
		return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
		