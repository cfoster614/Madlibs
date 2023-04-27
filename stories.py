

"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title
        self.code = code

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    "history",
    "Once upon a time...",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "one day",
    "One day...",
    ["place", "noun", "adjective", "verb", "plural_noun"],
    """One day, a {adjective} {noun} decided it was time they told their {plural_noun} about their secret {adjective} {noun}. They {verb} over to their {plural_noun} {place} and gave them the {adjective} {noun}."""
)

story3 = Story(
    "happily",
    "The ___ happily...",
    ["noun", "verb", "adjective"],
    """The {noun} happily {verb} over their least favorite {noun}. It was a {adjective} piece of {noun} that needed to be gotten rid of."""
)

stories = {s.code: s for s in [story, story2, story3]}