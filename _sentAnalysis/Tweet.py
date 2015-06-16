
class Tweet:

    def __init__(self, user, screen_name, text):

        self.user = user,
        self.screen_name = screen_name,
        self.text = texto

    def toDBCollection (self):
        return {
            "user": self.user,
            "screen_name": self.screen_name,
            "text": self.text
        }

    def __str__(self):
        return "user: %s - screen_name: %s, text: %s" \
               %(self.user, self.screen_name, self.text)
