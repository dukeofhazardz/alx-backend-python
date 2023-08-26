#!/usr/bin/python3

from utils import memoize
from client import GithubOrgClient


class TestClass:
            
    def a_method(self):
                return 42

    @memoize
    def a_property(self):
        return self.a_method()

@memoize
def test_memo():
    return 3

'''test = TestClass()
for i in range(10):
    print(type(test.a_property))
    print(test.a_property)
    print(test.a_method())
for i in range(10):
    print(test_memo)'''

apple = GithubOrgClient('google')
print(apple._public_repos_url)
print(apple.public_repos)
for repo in apple.public_repos('MIT'):
    print(repo)
#print(apple.repos_payload)