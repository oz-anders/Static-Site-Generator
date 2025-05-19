import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node1", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_node_text(self):
        """
        Tests conversion of TextType.TEXT.
        """
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode) # Check it's a LeafNode
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None) # Ensure no props

    def test_text_node_to_html_node_bold(self):
        """
        Tests conversion of TextType.BOLD.
        """
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode) # Check it's a LeafNode
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None) # Ensure no props

    def test_text_node_to_html_node_italic(self):
        """
        Tests conversion of TextType.ITALIC.
        """
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode) # Check it's a LeafNode
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None) # Ensure no props

    def test_text_node_to_html_node_code(self):
        """
        Tests conversion of TextType.CODE.
        """
        node = TextNode("code block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode) # Check it's a LeafNode
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code block")
        self.assertEqual(html_node.props, None) # Ensure no props

    def test_text_node_to_html_node_link(self):
        """
        Tests conversion of TextType.LINK.
        """
        node = TextNode("Google", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode) # Check it's a LeafNode
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google") # Anchor text is the value
        self.assertEqual(html_node.props, {"href": "https://www.google.com"}) # URL is href prop

    def test_text_node_to_html_node_image(self):
        """
        Tests conversion of TextType.IMAGE.
        """
        node = TextNode("Python Logo", TextType.IMAGE, "https://www.python.org/static/logo.png")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode) # Check it's a LeafNode
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "") # Value should be empty string for images
        self.assertEqual(html_node.props, {"src": "https://www.python.org/static/logo.png", "alt": "Python Logo"}) # URL is src prop, text is alt prop

    def test_text_node_to_html_node_raises_error(self):
        """
        Tests that text_node_to_html_node raises ValueError for invalid text type.
        """
        class UnknownTextType:
            value = "unknown"
        node = TextNode("Some text", UnknownTextType())

        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertIn("Invalid text type:", str(cm.exception))

if __name__ == "__main__":
    unittest.main()