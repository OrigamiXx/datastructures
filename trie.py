class Trie(object):
    def __init__(self, root = None):
        if root == None:
            self.root = TrieNode()
        else:
            self.root = root

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            if char in cur.child.keys():
                cur = cur.child[char]
            else:
                cur.child[char] = TrieNode()
                cur = cur.child[char]
        cur.is_leaf = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            if char in cur.child.keys():
                cur = cur.child[char]
            else:
                return False
        if cur.is_leaf:
            return True
        else:
            return False
        
    def prefixWords(self, prefix):
        out = []
        cur = self.root
        for char in prefix:
            if char in cur.child.keys():
                cur = cur.child[char]
            else:
                return out
        self.DFS(cur, prefix, out)
        return out
        
    def DFS(self, root, curword, out):
        if root.is_leaf:
            out.append(curword)
        for each in sorted(root.child.keys()):
            newword = curword + each
            self.DFS(root.child[each], newword, out)
    
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            if char in cur.child.keys():
                cur = cur.child[char]
            else:
                return False
        return True
    
    def delete(self, word):
        self.remove(self.root, "", word)
    
    def remove(self, root, curword, target):
        if curword == target:
            if not root.is_leaf:
                return False
            if root.is_leaf and len(root.child.keys()) > 0:
                root.is_leaf = False
                return False
            else:
                return True
        else:
            nextchar = target[len(curword)]
            curword += nextchar
            if nextchar in root.child.keys():
                nextRoot = root.child[nextchar]
                res = self.remove(nextRoot, curword, target)
                if res:
                    del root.child[nextchar]
                    if root.is_leaf or len(root.child.keys()) > 0:
                        return False
                    else:
                        return True
            else:
                return False

        
class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_leaf = False
