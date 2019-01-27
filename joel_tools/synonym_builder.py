"""
SynonymBuilder
--------------

Build 'synonyms' (terms connected by substrings) in the following manner:

Initial set of terms:

    ["joel", "joel klinger", "joel klinger codes"]

build recursive relations such as

    "joel" --> "joel klinger"
    "joel klinger" --> "joel klinger codes"

and then

    "joel" --> ["joel klinger", "joel klinger codes"]

such that the term "joel" is taken as a synonym for the other terms.

    Args:
        startswith_factor (int): How much longer a term should be to be
                                 considered a synonym of a substring,
                                 if it starts with the substring.
        contains_factor (int): How much longer a term should be to be
        min_size (int): Minimum size of terms to be considered to synonyms.
"""


class SynonymBuilder:
    def __init__(self, startswith_factor=2, contains_factor=1.3, min_size=6):
        self.startswith_factor = startswith_factor
        self.contains_factor = contains_factor
        self.min_size = min_size

    def is_synonym(self, a, b):
        """Is b a synonym of a, such that a is a substring of b?"""
        len_a = len(a)
        len_b = len(b)
        if len_b <= self.startswith_factor*len_a and b.startswith(a):
            return True
        return len_b <= self.contains_factor*len_a and a in b

    def fit_transform(self, X):
        """Wrapper method for fit and transform, to be consistent with
        sklearn pipelines.
        """
        self.fit(X)
        return self.transform(X)

    def fit(self, X):
        """Find all synonyms in array X."""
        # Find all vocab of valid size
        _vocab = set(term for term in set(X)
                     if (len(term) > self.min_size
                         and not term.isalpha()))
        # Sort the vocab in size order to speed up comparisons
        _vocab = sorted(list(_vocab), key=lambda x: len(x))
        self.reverse_synonynms = {}   # A mapping of large term --> small term
        # O(N2) iteration
        for i, term in enumerate(_vocab):
            for j, _term in enumerate(_vocab):
                # Ignore itself
                if i == j:
                    continue
                # Don't double match terms
                if _term in self.reverse_synonynms:
                    continue
                # Check if the terms are synonyms
                if not self.is_synonym(term, _term):
                    continue
                # If so, record the match
                self.reverse_synonynms[_term] = term

    def transform(self, X):
        """Apply the transformation described in
        _transform to each element of X"""
        return list(map(self._transform, X))

    def _transform(self, term):
        """Recursively find the smallest synonym
        representation of term `term`"""
        # If the term has a synonym
        if term in self.reverse_synonynms:
            synonym = self.reverse_synonynms[term]
            # Check if it's synonym also has a synonym
            return self._transform(synonym)
        return term
