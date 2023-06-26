# 1472. Design Browser History

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current_page = homepage
        self.current_index = 0
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[0:self.current_index + 1]
        self.history.append(url)
        self.current_page = url
        self.current_index = len(self.history) - 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index -= steps
        if self.current_index <= 0:
            self.current_index = 0
        self.current_page = self.history[self.current_index]
        return self.current_page

        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index += steps
        if self.current_index > len(self.history) - 1:
            self.current_index = len(self.history) - 1
        self.current_page = self.history[self.current_index]
        return self.current_page