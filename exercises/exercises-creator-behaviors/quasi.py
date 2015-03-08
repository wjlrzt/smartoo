from __future__ import unicode_literals
from knowledge.utils.sparql import prepared_query
from exercises import ExercisesCreatorBehavior
from exercises.models import Exercise
from exercises.utils.distractors import generate_similar_terms
from exercises.utils.distractors import create_choice_list


class Quasi(ExercisesCreatorBehavior):
    """
    Quasi Exercises Creator Behavior
    --------------------------------

    Uses quasi-facts (i.e. facts which encodes a single exercise and are
    useless for anything else).
    """

    def create_exercises(self, knowledge_graph):
        #print knowledge_graph
        TERM_IN_SENTENCE_QUERY = prepared_query("""
            SELECT ?before ?term ?after
            WHERE {
                ?quasifact a "term-in-sentence" .
                ?quasifact smartoo:part-before-term ?before .
                ?quasifact smartoo:part-after-term ?after .
                ?quasifact smartoo:term ?term .
            }
        """)

        terms_in_sentence = knowledge_graph.query(TERM_IN_SENTENCE_QUERY)
        for before, term, after in terms_in_sentence:
            distractors = generate_similar_terms(term, knowledge_graph)
            choices, correct_answer_label = create_choice_list(
                correct=term,
                distractors=distractors,
                knowledge_graph=knowledge_graph)
            #correct_answer_label = knowledge_graph.label(term)
            exercise = Exercise(data={
                'question': '{before} _______ {after}'.format(
                    before=unicode(before),
                    after=unicode(after)),
                'choices': choices,
                'correct-answer': correct_answer_label
            })
            yield exercise
