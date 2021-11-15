import difflib
import re

class Evaluation:
    def __init__(self, reference, sample):
        self.reference = reference
        self.sample = sample
        self.words_counter = 0
        self.error_counter = 0
        self.grade = ""
    
    def discriminate(self, string):
        return "".join([u'\u0336{}'.format(c) for c in string])

    def tokenize(self, string):
        return re.split("\s+", string)

    def untokenize(self, tokens):
        return " ".join(tokens)
            
    def compare(self):
        reference = self.tokenize(self.reference)
        sample = self.tokenize(self.sample)
        self.words_counter = len(reference)

        self.error_counter = 0
        aux_value = 0
        result = []

         
        prev = difflib.Match(0,0,0)
        for match in difflib.SequenceMatcher(a=reference, b=sample).get_matching_blocks():

            if (prev.a + prev.size != match.a):
                # word exist in the reference, but not found in the sample
                self.error_counter += len(reference[prev.a + prev.size:match.a])

                result += [self.discriminate(reference[prev.a + prev.size])]
                result += reference[prev.a + prev.size + 1:match.a]


            if (prev.b + prev.size != match.b):
                # word exist in the sample, but not found in the reference

                self.error_counter += len(sample[prev.b + prev.size:match.b])

                if(prev.b + prev.size < len(reference) and match.a <= len(reference)):
                    aux_value = 1
                    result += [self.discriminate(reference[match.a])] 

            result += reference[match.a+aux_value:match.a+match.size]
            aux_value = 0

            prev = match
        return self.untokenize(result)

    def grader(self):
        percent = (self.error_counter * 100) / self.words_counter
        
        if percent == 0:
            self.grade = "A"
        if percent > 0 and percent < 50:
            self.grade = "B"
        if percent > 50 and percent < 80:
            self.grade = "C"
        if percent > 80:
            self.grade = "D"
        
        return self.grade
