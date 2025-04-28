

"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

trie树，即字典树，又称单词查找树或键树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计
和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：最大
限度地减少无谓的字符串比较，查询效率比哈希表高。” 

因为限定都是由a-z小写字母构成，所以这棵树是一棵26叉树。前缀树的构造过程，通过不断插入新的字符串来
丰富这棵26叉树。前缀树的功能很强大，可以做文本词频统计，例如我们在搜索框中的搜索提示，就可以利用前缀
树实现。因此，前缀树基本的操作是字符串的插入insert，搜索search，删除delete，查找前缀startsWith等。
https://blog.csdn.net/weixin_42077402/article/details/98174130
"""


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
            print(node)
        node["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
            print(node)
        return "end" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

























