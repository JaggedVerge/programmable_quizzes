"""
This module supplies code to handle arbitrary choices in the question input.
This is done via a class that handles how a specific location in the text is filled in.

When a question can have multiple inputs of an arbitrary nature we wish to make it convienent
to pass that directly to the templating engine but the difficulty arises when we must
deal with choices.

For example say we have the following template:

    what is {{ parameter1 }} combined with {{ parameter2 }}?
    
That we wish to pass in the following input parameters:

{
"parameter1": ['a', 'b', 'c'],
"parameter2": ['z'],
}

If no choices are possible then simple substitution can occur.
However if as is desired with this package we wish to have multiple questions
generated from the given input we have ambiguity in substituting here.

When substituting into the template is `parameter1` here the whole list or
just an element from the list?

Without a wrapper class or other metadata we cannot simultaneously make that distinction
and allow for choices to be taken from the items.
"""


class Variation:
    """This class manages choice based inputs"""
    SEQUENTIAL = 1
    RANDOM = 2

    def __init__(self, items, selection_method=SEQUENTIAL):
        """
        :selection_method: the strategy to pick items from this group
        """
        self.items = items

    def get(self):
        """Yield next item"""
        for item in self.items:
            yield item
